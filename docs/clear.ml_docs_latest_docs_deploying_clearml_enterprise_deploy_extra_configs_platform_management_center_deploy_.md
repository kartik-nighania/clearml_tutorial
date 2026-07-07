---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/"
title: "Platform Management Center | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

important

The Platform Management Center is available under the ClearML Enterprise plan.

This guide describes how to deploy the [Platform Management Center](https://clear.ml/docs/latest/docs/webapp/platform_management_center) on
Kubernetes.

This procedure assumes you have already set up the [ClearML control plane](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/k8s).

## Step 1: Add Dedicated Control Plane Access Credentials [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/\#step-1-add-dedicated-control-plane-access-credentials "Direct link to Step 1: Add Dedicated Control Plane Access Credentials")

Configure the ClearML Server with credentials that the platform management center will use for secure access.
If `openssl` is available, you can use the following command to generate suitable key and secret:

```text
openssl rand -hex 16
```

Add the following environment variables to your ClearML Enterprise server overrides file (`clearml-values.override.yaml`):

```yaml
apiserver:

  extraEnvs:

    - name: CLEARML__secure__credentials__platform_management__user_key

      value: "<PLATFORM_MANAGEMENT_USER_KEY>"

    - name: CLEARML__secure__credentials__platform_management__user_secret

      value: "<PLATFORM_MANAGEMENT_USER_SECRET>"
```

Then apply the new configuration:

```text
helm upgrade -n clearml clearml-enterprise \

  oci://docker.io/clearml/clearml-enterprise \

  -f clearml-values.override.yaml
```

## Step 2: Platform Management Center Setup Configuration [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/\#step-2-platform-management-center-setup-configuration "Direct link to Step 2: Platform Management Center Setup Configuration")

The Platform Management Center needs to:

1. Connect to the ClearML API server
2. Authenticate administrators using it ( [SSO or fixed users](https://clear.ml/docs/latest/docs/user_management/identity_providers))

Create an overrides file, for example:

```text
clearml-enterprise-platform-management.override.yaml.
```

### Configure Container Repository Access [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/\#configure-container-repository-access "Direct link to Configure Container Repository Access")

Add the following configuration to the overrides file:

```text
global:

  imageCredentials:

    password: "<CLEARML_DOCKERHUB_TOKEN>"
```

Where `<CLEARML_DOCKERHUB_TOKEN>` is the token provided by ClearML for its container repository.

### Configure ClearML Control Plane Connection Parameters [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/\#configure-clearml-control-plane-connection-parameters "Direct link to Configure ClearML Control Plane Connection Parameters")

Add the following configuration to the overrides file:

```text
clearml:

  apiServerUrlReference: "<CLEARML_APISERVER_URL>"

  apiKey: "<PLATFORM_MANAGEMENT_USER_KEY>"

  apiSecret: "<PLATFORM_MANAGEMENT_USER_SECRET>"
```

Where

- `<CLEARML_APISERVER_URL>` is the URL for the ClearML control plane API server
- `<PLATFORM_MANAGEMENT_USER_KEY>` and `<PLATFORM_MANAGEMENT_USER_SECRET>` are the values created in Step 1

### Configure Admin Authentication [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/\#configure-admin-authentication "Direct link to Configure Admin Authentication")

To configure how administrators log in to the Platform Management Center, fill in the appropriate identity provider
information in the overrides file.

For complete information on identity provider options, see the [SSO Setup Guide](https://clear.ml/docs/latest/docs/user_management/identity_providers).

#### Example: OAuth [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/\#example-oauth "Direct link to Example: OAuth")

```text
platformManagement:

  extraEnvs:

    - name: CLEARML__secure__login__sso__oauth_client__auth0__client_id

      value: "<AUTH0_AUTH_CLIENT_ID>"

    - name: CLEARML__secure__login__sso__oauth_client__auth0__client_secret

      value: "<AUTH0_AUTH_CLIENT_SECRET>"

    - name: CLEARML__services__login__sso__oauth_client__auth0__base_url

      value: "<AUTH0_TENANT_BASE_URL>"

    - name: CLEARML__services__login__sso__oauth_client__auth0__authorize_url

      value: "<AUTH0_TENANT_AUTHORIZE_URL>"

    - name: CLEARML__services__login__sso__oauth_client__auth0__access_token_url

      value: "<AUTH0_TENANT_ACCESS_TOKEN_URL>"

    - name: CLEARML__services__login__sso__oauth_client__auth0__audience

      value: "<AUTH0_TENANT_AUDIENCE_URL>"

    # Optional: restrict access by email or domain

    - name: CLEARML__services__login__email_filters__allowed

      value: ["example.com", "my-domain.ai"]
```

#### Example: Fixed Users [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/\#example-fixed-users "Direct link to Example: Fixed Users")

You can enable fixed users instead of an external identity provider:

```text
platformManagement:

  extraEnvs:

    - name: CLEARML__platform_management__auth__fixed_users__enabled

      value: "true"

    - name: CLEARML__platform_management__auth__fixed_users__users

      value: "[{\"username\":\"<USERNAME_PLACEHOLDER>\",\"password\":\"<PASSWORD_PLACEHOLDER>\",\"name\":\"<USER_NAME_PLACEHOLDER>\"}]"
```

## Step 3: Install the Platform Management Center [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/\#step-3-install-the-platform-management-center "Direct link to Step 3: Install the Platform Management Center")

Install the `clearml-enterprise-platform-management` Helm chart in the same namespace as the ClearML control plane:

```text
helm upgrade -i clearml-enterprise-platform-management oci://docker.io/clearml/clearml-enterprise-platform-management -n clearml -f clearml-enterprise-platform-management.override.yaml
```

note

This installs the Platform Management Center service and webserver, but does not expose it externally.

## Step 4: Accessing the Platform Management Center UI [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/\#step-4-accessing-the-platform-management-center-ui "Direct link to Step 4: Accessing the Platform Management Center UI")

By default, the UI is only accessible from inside the cluster using `kubectl port-forward`.

If external access is required, you can expose the webserver using an Ingress resource in your overrides file. For example:

```text
platformManagementWebserver:

  ingress:

    enabled: true

    ingressClassName: ""

    annotations: {}

    hostName: "<HOSTNAME_PLACEHOLDER>"

    tlsSecretName: "<TLS_SECRETNAME>"
```

- [Step 1: Add Dedicated Control Plane Access Credentials](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/#step-1-add-dedicated-control-plane-access-credentials)
- [Step 2: Platform Management Center Setup Configuration](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/#step-2-platform-management-center-setup-configuration)
  - [Configure Container Repository Access](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/#configure-container-repository-access)
  - [Configure ClearML Control Plane Connection Parameters](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/#configure-clearml-control-plane-connection-parameters)
  - [Configure Admin Authentication](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/#configure-admin-authentication)
- [Step 3: Install the Platform Management Center](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/#step-3-install-the-platform-management-center)
- [Step 4: Accessing the Platform Management Center UI](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/platform_management_center_deploy/#step-4-accessing-the-platform-management-center-ui)