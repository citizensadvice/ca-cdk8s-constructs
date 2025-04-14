# CA cdk8s Constructs

This repository contains a collection of opinionated cdk8s constructs that are commonly used in CA applications.

## Custom Resource Definitions

The CRDs are found in the `cdk8s.yaml` file, which contains a list of URLs to the CRD definitions.

The generated classes are imported into the `ca_cdk8s_constructs/imports` directory.

If the CRDs are updated, the imports need to be refreshed.

### Refreshing CRD Imports

To refresh the CRD imports, run the following command:

```bash
cdk8s import --output ca_cdk8s_constructs/imports
```
