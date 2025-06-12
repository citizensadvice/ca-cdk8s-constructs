from cdk8s import Chart
from cdk8s_plus_32 import Deployment, Topology

from ca_cdk8s_constructs.topology_spread import WhenUnsatisfiable, set_topology_spread


def test_topology_spread_defaults(chart_fixture: Chart, snapshot):
    deployment = Deployment(chart_fixture, "Deployment")
    deployment.add_container(
        image="nginx:latest",
    )
    set_topology_spread(
        target=deployment,
    )
    constraints = chart_fixture.to_json()[0]["spec"]["template"]["spec"][
        "topologySpreadConstraints"
    ]
    assert constraints == snapshot


def test_topology_spread_max_skew(chart_fixture: Chart, snapshot):
    deployment = Deployment(chart_fixture, "Deployment")
    deployment.add_container(
        image="nginx:latest",
    )
    set_topology_spread(
        target=deployment,
        max_skew=2,
    )
    constraints = chart_fixture.to_json()[0]["spec"]["template"]["spec"][
        "topologySpreadConstraints"
    ]
    assert constraints == snapshot


def test_topology_spread_min_domains(chart_fixture: Chart, snapshot):
    deployment = Deployment(chart_fixture, "Deployment")
    deployment.add_container(
        image="nginx:latest",
    )
    set_topology_spread(
        target=deployment,
        min_domains=2,
    )
    constraints = chart_fixture.to_json()[0]["spec"]["template"]["spec"][
        "topologySpreadConstraints"
    ]
    assert constraints == snapshot


def test_topology_spread_when_unsatisfiable(chart_fixture: Chart, snapshot):
    deployment = Deployment(chart_fixture, "Deployment")
    deployment.add_container(
        image="nginx:latest",
    )
    set_topology_spread(
        target=deployment,
        when_unsatisfiable=WhenUnsatisfiable.DO_NOT_SCHEDULE,
    )
    constraints = chart_fixture.to_json()[0]["spec"]["template"]["spec"][
        "topologySpreadConstraints"
    ]
    assert constraints == snapshot


def test_topology_spread_topology_keys(chart_fixture: Chart, snapshot):
    deployment = Deployment(chart_fixture, "Deployment")
    deployment.add_container(
        image="nginx:latest",
    )
    set_topology_spread(
        target=deployment,
        topology_keys=(Topology.ZONE,),
    )
    constraints = chart_fixture.to_json()[0]["spec"]["template"]["spec"][
        "topologySpreadConstraints"
    ]
    assert constraints == snapshot
