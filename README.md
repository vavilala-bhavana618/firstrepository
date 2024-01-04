# codefresh-runtime_internal-shared-config
This repository stores configuration files that can be shared between runtimes.

Configuration definitions that will be stored in this repository:
- Argo CD managed cluster
- Git sources
- Codefresh 3rd party integrations configuration
- Ouath2 Authentications applications

Configurations will be synced and applied to specific runtimes or to all runtimes assoiciated wtih your Codefresh Account.

## Repository structure
The base path of the repository will include 2 directories - resources and runtimes.
The resources directory will include the following sub-directories:
- all-runtimes-all-clusters - every manifest placed under this directory will end up in all the user's clusters
- control-plane - used by managed runtimes. Every manifest placed here will be applied to each runtime's in-cluster
- runtimes/<runtime_name> - a folder for each specific runtime. 
 
Each manifest will be applied to all clusters in a specific runtime
both control-plane and the runtime-specific directories are optional.
The runtimes directory will include a separate sub-directory for each runtime installed in the cluster. Each such runtime-directory will include in-cluster.yaml


```
├── resources <───────────────────┐
│   ├── all-runtimes-all-clusters │
│   │   ├── manifest1.yaml        │
│   │   └── subfolder             │
│   │       └── manifest2.yaml    │
│   ├── control-planes            │
│   │   └── manifest3.yaml        │
│   ├── runtimes                  │
│   │   ├── runtime1              │
│   │   │   └── manifest4.yaml    │
│   │   └── runtime2              │
│   │       └── manifest5.yaml    │
│   └── manifest6.yaml            │
└── runtimes                      │
    ├── runtime1                  │ # references by <install_repo_1>/apps/runtime1/config_dir.json
    │   ├── in-cluster.yaml      ─┤ #      manage 'include' field to decide which dirs/files to sync to cluster
    │   └── other-cluster.yaml   ─┤ #      manage 'include' field to decide which dirs/files to sync to cluster
    └── runtime2                  │ # references by <install_repo_2>/apps/runtime2/config_dir.json
        └── in-cluster.yaml      ─┘ #      manage 'include' field to decide which dirs/files to sync to cluster
```
