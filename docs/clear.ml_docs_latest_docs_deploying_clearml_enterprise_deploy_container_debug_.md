---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/"
title: "Container and Pod Debugging | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The following describes debugging workflows for ClearML deployments on Kubernetes or Docker Compose. These procedures
allow you to inspect running containers, troubleshoot startup and runtime issues, and debug workloads.

## Kubernetes: Ephemeral Debug Containers [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/\#kubernetes-ephemeral-debug-containers "Direct link to Kubernetes: Ephemeral Debug Containers")

Kubernetes supports attaching ephemeral containers to running pods for debugging without modifying the original workload.

### Attach a Debug Container [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/\#attach-a-debug-container "Direct link to Attach a Debug Container")

To attach a temporary debug container to an existing pod and share its process namespace:

```text
kubectl debug -it <pod> \

 --image=busybox \

 --target=<container> \

 -- sh
```

The `--target` flag shares the process namespace of the target container. This allows you to inspect:

- Running processes (`ps`)
- Filesystem (`/proc`, mounted volumes)
- Runtime state of the application container

### Copy-the-pod Debugging [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/\#copy-the-pod-debugging "Direct link to Copy-the-pod Debugging")

If the original pod terminates too quickly to attach a debug container, you can create a copy of the pod instead.
This lets you safely inspect the workload without impacting the original production pod.

```text
kubectl debug <pod> \

 -it \

 --copy-to=debug-pod \

 --container=debug \

 --image=busybox \

 --share-processes \

 -- sh
```

## Air-gapped Kubernetes Environments [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/\#air-gapped-kubernetes-environments "Direct link to Air-gapped Kubernetes Environments")

In restricted or air-gapped environments, all debug images must be available in an internal registry or pre-loaded on
cluster nodes.

When running debug commands:

- Replace the `--image` value with your internal registry path:





```text
  --image=registry.internal.example.com/tools/busybox
```

- Set image pull policy if required:





```text
  --image-pull-policy=IfNotPresent
```









or





```text
  --image-pull-policy=Never
```

- Ensure `imagePullSecrets` are configured if the registry requires authentication.


## Docker Compose: Debug Containers [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/\#docker-compose-debug-containers "Direct link to Docker Compose: Debug Containers")

Docker supports running a separate debug container that shares the target container's network and process namespaces,
allowing you to inspect processes, network configuration, and filesystem state.

```text
docker run -it --rm \

 --pid=container:<target_container_id> \

 --network=container:<target_container_id> \

 busybox sh
```

## Air-gapped Docker Hosts [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/\#air-gapped-docker-hosts "Direct link to Air-gapped Docker Hosts")

If external registries are not available, debug images must be pre-loaded manually.

### Option 1: Load image from tarball [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/\#option-1-load-image-from-tarball "Direct link to Option 1: Load image from tarball")

Use this option when no internal registry is available.

1. On a machine with internet access, run:





```text
docker save <image> -o debug-image.tar
```

2. Transfer the file to the air-gapped host

3. Load the debug image:





```text
docker load -i debug-image.tar
```


### Option 2: Internal registry workflow [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/\#option-2-internal-registry-workflow "Direct link to Option 2: Internal registry workflow")

Use this option when an internal registry is available.

1. Load or build the image
2. Retag and push the image to the internal registry
3. Update debug commands to use the internal image path

- [Kubernetes: Ephemeral Debug Containers](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/#kubernetes-ephemeral-debug-containers)
  - [Attach a Debug Container](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/#attach-a-debug-container)
  - [Copy-the-pod Debugging](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/#copy-the-pod-debugging)
- [Air-gapped Kubernetes Environments](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/#air-gapped-kubernetes-environments)
- [Docker Compose: Debug Containers](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/#docker-compose-debug-containers)
- [Air-gapped Docker Hosts](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/#air-gapped-docker-hosts)
  - [Option 1: Load image from tarball](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/#option-1-load-image-from-tarball)
  - [Option 2: Internal registry workflow](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/container_debug/#option-2-internal-registry-workflow)