# CA cdk8s Constructs

This repository contains a collection of opinionated cdk8s constructs that are commonly used in CA applications.

## Usage

To use the constructs, add the following to your `pyproject.toml` file:

```toml
[tool.poetry.dependencies]
ca-cdk8s-constructs = { git = "https://github.com/citizensadvice/ca-cdk8s-constructs", rev = "<version>" }
```

There are currently constructs available for:

- Horizontal Pod Autoscaler
- Vertical Pod Autoscaler
- Pod Disruption Budget
- Container Resources

Please see their docstrings for usage information.

To request new constructs, please raise an issue in the [GitHub repository](https://github.com/citizensadvice/ca-cdk8s-constructs/issues).

## Custom Resource Definitions

The CRDs are found in the `cdk8s.yaml` file, which contains a list of URLs to the CRD definitions.

The generated classes are imported into the `ca_cdk8s_constructs/imports` directory.

If the CRDs are updated, the imports need to be refreshed. There is an Actions workflow that will run weekly to refresh the imports if there are any changes.

### Manually Refreshing CRD Imports

To refresh the CRD imports, run the following command:

```bash
cdk8s import --output ca_cdk8s_constructs/imports
```

## Versioning

New versions of this library will be released via Github Releases and will follow the [Semantic Versioning](https://semver.org/) wherever possible.

## Contributing

This project uses:

- `poetry` for dependency management
- `pytest` for testing
- `ruff` for linting and formatting

To run the tests and linting, run the following command:

```bash
poetry install --with dev
poetry run pytest
poetry run ruff check
poetry run ruff format
```
