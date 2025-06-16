from json import dumps

import pytest
from cdk8s import Chart, Duration
from cdk8s_plus_32 import Deployment

from ca_cdk8s_constructs.blackbox_probe import ca_blackbox_probe


def test_blackbox_probe_ingress(chart_fixture: Chart, snapshot):
    deployment = Deployment(chart_fixture, "deployment")
    deployment.add_container(image="nginx:latest", port=80)
    ingress = deployment.expose_via_ingress("/")
    probe = ca_blackbox_probe(
        chart_fixture,
        "probe",
        ingress,
    )
    print(dumps(probe.to_json(), indent=2))

    spec = probe.to_json()["spec"]
    assert spec["interval"] == "60s"
    assert (
        spec["targets"]["ingress"]["selector"]["matchLabels"][
            "app.kubernetes.io/blackbox-target"
        ]
        == ingress.name
    )
    assert spec == snapshot


def test_blackbox_probe_static(chart_fixture: Chart, snapshot):
    probe = ca_blackbox_probe(chart_fixture, "probe", "http://localhost:8080")
    spec = probe.to_json()["spec"]
    assert spec["targets"]["staticConfig"]["static"] == ["http://localhost:8080"]
    assert spec == snapshot


def test_blackbox_probe_custom_interval_short(chart_fixture: Chart, snapshot):
    probe = ca_blackbox_probe(
        chart_fixture,
        "probe",
        "http://localhost:8080",
        interval=Duration.seconds(30),
    )
    spec = probe.to_json()["spec"]
    assert spec["interval"] == "30s"
    assert spec == snapshot


def test_blackbox_probe_custom_interval_long(chart_fixture: Chart, snapshot):
    probe = ca_blackbox_probe(
        chart_fixture,
        "probe",
        "http://localhost:8080",
        interval=Duration.minutes(30),
    )
    spec = probe.to_json()["spec"]
    assert spec["interval"] == "1800s"
    assert spec == snapshot


def test_blackbox_probe_with_path(chart_fixture: Chart, snapshot):
    probe = ca_blackbox_probe(chart_fixture, "probe", "http://localhost:8080/api/health")
    spec = probe.to_json()["spec"]
    assert spec["targets"]["staticConfig"]["static"] == ["http://localhost:8080/api/health"]
    assert spec == snapshot


def test_blackbox_probe_invalid_target(chart_fixture: Chart):
    with pytest.raises(
        ValueError, match="Invalid target type: <class 'int'>, must be Ingress or str"
    ):
        ca_blackbox_probe(chart_fixture, "probe", 123)  # type: ignore


def test_blackbox_probe_custom_timeout(chart_fixture: Chart, snapshot):
    probe = ca_blackbox_probe(
        chart_fixture,
        "probe",
        "http://localhost:8080",
        timeout=Duration.seconds(30),
    )
    spec = probe.to_json()["spec"]
    assert spec["scrapeTimeout"] == "30s"
    assert spec == snapshot
