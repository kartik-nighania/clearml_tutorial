---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/"
title: "Kubernetes Deployment | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The AI Application Gateway is available under the ClearML Enterprise plan.

This guide details the installation of the ClearML App Gateway.
The App Gateway enables access to your AI workload applications (e.g. remote IDEs like VSCode and Jupyter, model API interface, etc.).
It acts as a proxy, identifying ClearML Tasks running within its [K8s namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
and making them available for network access.

important

The App Gateway must be installed in the same K8s namespace as a dedicated ClearML Agent.
It can only configure access for ClearML Tasks within its own namespace. This means that if you have multiple agents running
in multiple namespaces, each namespace must have its own App Gateway.

## Requirements [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/\#requirements "Direct link to Requirements")

- Helm installed and configured
- A DockerHub token to access the OCI enterprise Helm charts and Docker images
- A valid ClearML Server installation

## Optional for HTTPS [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/\#optional-for-https "Direct link to Optional for HTTPS")

- A valid DNS entry for the new App Gateway instance
- A valid SSL certificate

## Helm [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/\#helm "Direct link to Helm")

### Log into the ClearML OCI Registry [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/\#log-into-the-clearml-oci-registry "Direct link to Log into the ClearML OCI Registry")

```bash
helm registry login docker.io --username allegroaienterprise --password <CLEARML_DOCKERHUB_TOKEN>
```

### Prepare Values [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/\#prepare-values "Direct link to Prepare Values")

Before installing the App Gateway, create a Helm override `clearml-app-gateway-values.override.yaml` file:

note

The configuration below uses ingress for HTTP(S) traffic. If you plan to expose the App Gateway for non-HTTP(S) workloads without using ingress,
see [Expose App Gateway via NodePort](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/#expose-app-gateway-via-nodeport).

```yaml
imageCredentials:

  password: ""

clearml:

  apiKey: ""

  apiSecret: ""

  apiServerUrlReference: ""

  authCookieName: ""

ingress:

  enabled: true

  hostName: ""

streamSession:

  routerAddress: ""

  service:

    type: LoadBalancer

  portRange:

    start:

    end:
```

**Configuration options:**

- `imageCredentials.password`: ClearML DockerHub Access Token.
- `clearml.apiKey` and `clearml.apiSecret`: [API credentials](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#clearml-api-credentials) created in the ClearML web UI by an Admin user or Service
Account with admin privileges. Make sure to label these credentials clearly, so that they will not be revoked by mistake.
- `clearml.apiServerUrlReference`: ClearML API server URL starting with `https://api.`.
- `clearml.authCookieName`: Cookie used by the ClearML server to store the ClearML authentication cookie.
- `ingress.hostName`: Hostname of App Gateway used by the ingress controller to access it.
- `streamSession.routerAddress`: The external App Gateway address (can be an IP, hostname, or load balancer address) depending on your network setup. Ensure this address is accessible for TCP and UDP connections.
- `streamSession.service.type`: Service type used to expose TCP and UDP functionality, default is `NodePort`.
- `streamSession.portRange.start`: Start port for the TCP and UDP Session feature.
- `streamSession.portRange.end`: End port for the TCP and UDP Session feature.

The full list of supported configuration is available with the command:

```bash
helm show readme oci://docker.io/clearml/clearml-enterprise-app-gateway
```

### Expose App Gateway via NodePort [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/\#expose-app-gateway-via-nodeport "Direct link to Expose App Gateway via NodePort")

If you prefer to expose the App Gateway without using an ingress controller (for example, to support non-HTTP(S) workloads),
you can configure it to use a `NodePort` service type.

Add the following configuration overrides to your `clearml-app-gateway-values.override.yaml` file:

```yaml
ingress:

  enabled: false

service:

  type: NodePort

router:

  extraEnvs:

    - name: ROUTER__HTTP__AUTHORIZATION__COOKIE__SECURE

      value: "false"

externalURL: "http://<NODE_IP>:<NODE_PORT>"
```

- `ingress.enabled: false`: Disables ingress creation for the App Gateway.
- `service.type: NodePort`: Exposes the gateway through a Kubernetes NodePort instead of ingress.
- `ROUTER__HTTP__AUTHORIZATION__COOKIE__SECURE: false`: Allows the gateway to operate over HTTP rather than HTTPS.
- `externalURL`: Should point to the gateway's external address, using the node's IP and the assigned port.

### Install [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/\#install "Direct link to Install")

To install the App Gateway component via Helm use the following command:

```bash
helm upgrade -i <RELEASE_NAME> -n <WORKLOAD_NAMESPACE> oci://docker.io/clearml/clearml-enterprise-app-gateway -f clearml-app-gateway-values.override.yaml
```

Replace the placeholders with the following values:

- `<RELEASE_NAME>`: Unique name for the App Gateway within the K8s namespace. This is a required parameter in
Helm, which identifies a specific installation of the chart. The release name also defines the App Gateway's name and
appears in the UI within AI workload application URLs (e.g. Remote IDE URLs). This can be customized to support multiple installations within the same
namespace by assigning different release names.
- `<WORKLOAD_NAMESPACE>`: [Kubernetes Namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
where workloads will be executed. This namespace must be shared between a dedicated ClearML Agent and an App
Gateway. The agent is responsible for monitoring its assigned task queues and spawning workloads within this
namespace. The App Gateway monitors the same namespace for AI workloads (e.g. remote IDE applications). The App Gateway has a
namespace-limited scope, meaning it can only detect and manage tasks within its
assigned namespace.
- `<CHART_VERSION>`: Version recommended by the ClearML Support Team.

## Monitoring and Testing the Gateway [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/\#monitoring-and-testing-the-gateway "Direct link to Monitoring and Testing the Gateway")

Once your gateway is deployed, you can monitor its status, view routed tasks, and run connectivity tests in
ClearML WebApp, under **Settings > Application Gateway**.

![App Gateway Test](https://clear.ml/docs/latest/assets/images/settings_app_gateway_test-9ced7405a39b05c24ba8300140230d2c.png#light-mode-only)![App Gateway Test](https://clear.ml/docs/latest/assets/images/settings_app_gateway_test_dark-f2fc85a02fd99ba94c09e6c77f83ff70.png#dark-mode-only)

- [Requirements](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/#requirements)
- [Optional for HTTPS](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/#optional-for-https)
- [Helm](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/#helm)
  - [Log into the ClearML OCI Registry](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/#log-into-the-clearml-oci-registry)
  - [Prepare Values](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/#prepare-values)
  - [Expose App Gateway via NodePort](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/#expose-app-gateway-via-nodeport)
  - [Install](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/#install)
- [Monitoring and Testing the Gateway](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s/#monitoring-and-testing-the-gateway)