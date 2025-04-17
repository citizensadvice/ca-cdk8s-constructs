import builtins
from textwrap import dedent
import typing
from aws_cdk import Duration
from aws_cdk.aws_eks import HelmChart, ICluster
from aws_cdk.aws_s3_assets import Asset
import cdk8s
from constructs import Construct
import yaml
from tempfile import TemporaryDirectory
from pathlib import Path


class HelmChartAsset(Construct):
    """
    Asset for a Helm chart that renders anything passed to `Values.resources` as a helm template
    """

    def __init__(
        self,
        scope: Construct,
        id: str,
        name: str,
        version: str,
        app_version: str,
    ) -> None:
        """
        Create an S3 asset for a cdk8s chart.
        """

        super().__init__(scope, id)

        # Create a temporary directory for the chart
        with TemporaryDirectory() as chart_folder:
            # Write the chart spec to the Chart.yaml file
            with open(Path(chart_folder, "Chart.yaml"), "w+") as chart_spec:
                chart_spec.write(
                    yaml.dump(
                        {
                            "apiVersion": "v2",
                            "name": name,
                            "description": f"Generated chart for {name}",
                            "type": "application",
                            "version": version,
                            "appVersion": app_version,
                        }
                    )
                )

            # Write the values.yaml file. This is a single key which will contain
            # the rendered cdk8s chart.
            with open(Path(chart_folder, "values.yaml"), "w+") as values:
                values.write("resources: {}")

            # Create the templates directory
            template_dir = Path(chart_folder, "templates")
            template_dir.mkdir(parents=True)

            # Write the resources.yaml file. This will contain the rendered cdk8s chart.
            with open(Path(template_dir, "resources.yaml"), "w+") as template:
                template.write(
                    dedent(
                        """\
                        {{- range $v := .Values.resources }}
                        ---
                        {{$v | toYaml }}
                        {{- end }}
                        """
                    )
                )

            # Create the chart asset
            self.asset = Asset(self, "Default", path=chart_folder)


class Cdk8sHelmChart(HelmChart):
    """
    Bundles a cdk8s chart as a Helm chart by rendering all chart resources into a single values item.

    Is used in the same way as the `aws-cdk.aws_eks.HelmChart` resource, but instead of `chart` or
    `chart_asset`, pass an instance of `cdk8s.Chart` to `cdk8s_chart`. This can then be deployed using
    the `aws-cdk.aws_eks.Cluster.add_helm_chart()` method and retains the usual Helm functionality.
    """

    def __init__(
        self,
        scope: Construct,
        id: str,
        *,
        chart_name: str,
        app_version: str,
        cluster: ICluster,
        cdk8s_chart: cdk8s.Chart,
        atomic: typing.Optional[builtins.bool] = None,
        create_namespace: typing.Optional[builtins.bool] = None,
        release: typing.Optional[builtins.str] = None,
        skip_crds: typing.Optional[builtins.bool] = None,
        timeout: typing.Optional[Duration] = None,
        version: typing.Optional[builtins.str] = None,
        wait: typing.Optional[builtins.bool] = None,
    ) -> None:
        chart_asset = HelmChartAsset(
            scope,
            "Package",
            name=chart_name,
            version=version or "1.0",
            app_version=app_version,
        ).asset

        super().__init__(
            scope,
            id,
            cluster=cluster,
            chart_asset=chart_asset,
            atomic=atomic,
            create_namespace=create_namespace,
            namespace=cdk8s_chart.namespace,
            release=release,
            skip_crds=skip_crds,
            timeout=timeout,
            values={"resources": cdk8s_chart.to_json()},
            wait=wait,
        )
