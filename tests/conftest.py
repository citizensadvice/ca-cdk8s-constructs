import pytest
from cdk8s import App, Chart


@pytest.fixture
def chart_fixture():
    app = App()
    chart = Chart(app, "test")
    return chart
