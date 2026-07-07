---
url: "https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/"
title: "Application Gateway | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The AI Application Gateway is available under the ClearML Enterprise plan.

The ClearML [AI Application Gateway](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw) facilitates setting up secure,
authenticated access to jobs running on your compute nodes from external networks (see application gateway installation
for [Kubernetes](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s), Docker-Compose for [Self-Hosted Deployment](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_compose)
or Docker-Compose for [Hosted Deployment](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_compose_hosted)).

**Application Gateway** Settings include:

- **Routers** – Monitor gateway routers and verify routing functionality
- **Static Routes** – Define and monitor fixed, externally accessible endpoints that route to specific tasks or services.
- **Access Tokens** – Manage tokens for secure access to gateway endpoints

## Routers [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/\#routers "Direct link to Routers")

The **Routers** table lets you monitor all active application gateway routers, as well as verify gateway functionality. The table shows each router’s:

- Name
- Externally accessible URL
- Test Status: The result of the most recent connectivity test
- Last Tested: The time the router was last tested

![Application Gateway table](https://clear.ml/docs/latest/assets/images/settings_app_gateway-9a714e4bbc5734d41bb298892c32663f.png#light-mode-only)![Application Gateway table](https://clear.ml/docs/latest/assets/images/settings_app_gateway_dark-78f9371243c6d0d155ed29c7c7dae098.png#dark-mode-only)

Click on a router to open its details panel, which includes:

- **Info**: General router information


  - Router details
    - Uptime
    - Last update time
    - Router version
  - Routed Tasks table: ClearML tasks currently available for access through the router
    - Task name: Click to navigate to the task page
    - Endpoint: Exposed application URL
    - Owner: User who initiated the task

![Application Gateway info](https://clear.ml/docs/latest/assets/images/settings_app_gateway_info-afacdb6b9e93e419d69e6eb92e7b21f3.png#light-mode-only)![Application Gateway info](https://clear.ml/docs/latest/assets/images/settings_app_gateway_info_dark-ec52d9f52cf0e3d861c86c5eb8acc527.png#dark-mode-only)

- **Test Details**: Administrators can run a test to verify that a gateway is functioning correctly: Identifying routed
tasks and creating accessible network endpoints for them. The test launches a small task in the target network
(specified through the desired ClearML queue), and checks that the router successfully creates a route to that task,
and routes the network traffic to it.

To run a test:


1. Hover over the **Test Details** panel **>** Click **Test**
2. Input a queue that is serviced by agents in the network environment the router should provide access to
3. Click **Test**

note

Testing is only supported when both the ClearML WebApp and the gateway endpoint are served over secure (HTTPS) protocols.

The **Test Details** tab displays:

  - Status - Result of the most recent test
  - Status message
  - Status reason
  - Started time
  - Completed time
  - Run time
  - Queue - Queue where test task was enqueued for execution
  - Worker - ClearML Agent that executed the test task
  - Test Task name
  - Task ID
  - Browser endpoint
  - Endpoint

![Application Gateway test](https://clear.ml/docs/latest/assets/images/settings_app_gateway_test-9ced7405a39b05c24ba8300140230d2c.png#light-mode-only)![Application Gateway test](https://clear.ml/docs/latest/assets/images/settings_app_gateway_test_dark-f2fc85a02fd99ba94c09e6c77f83ff70.png#dark-mode-only)

- **Test log**: Console output of the most recent router test.


## Static Routes [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/\#static-routes "Direct link to Static Routes")

**Static Routes** allow administrators to define external endpoints which users can attach to their ClearML application
instances or services. Static routes decouple user network access from the specific deployed service instance (whose
details make up the on-demand, router generated endpoints).

Static routes can operate in two modes:

- **Single Endpoint**: One internal endpoint per route
- **Load Balancing**: Multiple internal endpoints behind the single fixed endpoint. Load balancing endpoints maintain
session context to keep sessions routing to the same internal endpoint.

Both URL-path and subdomain static routes can be defined.

Administrators can also enable **authentication** for route access using group-based permissions.

The **Static Routes** table lets you monitor all defined routes. The table shows each route's:

- Enabled: Toggle to enable / disable the static route
- Name: Route label
- Route:
  - When active, displays the endpoint URL (e.g.` <router_url>/path` or `subdomain.<router_domain>`). Click to access the endpoint in a new tab
  - When inactive, displays the projected route template depending on the route configuration (e.g. `<router url>/path` , `subdomain.<router domain>`)
- Type: URL or Subdomain route
- Load Balancing: Whether the route is single-endpoint or load balancing.
- Status: Router status
  - `Not In Use` \- Route is configured but not being used by any router.
  - `Pending` \- Route is being set up for use by a router
  - `Routing` \- Route configured and attached to at least one internal endpoint.
- Targets: Internal endpoints (Pod/IP:Port) connected to the route. These are existing endpoints provided by app instances
or services (e.g. Model Deployment app instance) that are exposed through the static route. If the
route is configured for load balancing, it can include multiple targets, with traffic distributed across them.
- Tasks: Linked tasks or app instances running the internal endpoints using the route
- Access: User groups with access to the route, or Public if no authentication is configured
- Created: Creation time
- Last Updated: Last modification time
- Updated By: User who last updated the route

### Creating a Static Route [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/\#creating-a-static-route "Direct link to Creating a Static Route")

To create a static route:

1. Click **\+ Add Route**
2. In the **Add New Route** modal, input the following information

   - Name – Route label
   - Input a Route URL path or Subdomain name. Note that a path must begin with a slash (`/`)
   - Load Balanced - Whether the route can serve multiple internal endpoints (load balancing) or just one.
   - Authenticated Route -Whether the route is accessible to specific users (default) or is publicly accessible.
     - Endpoint Access - When authentication is required, add the ClearML groups whose members can access this endpoint.

### Editing Routes [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/\#editing-routes "Direct link to Editing Routes")

A static route can be modified only when it is disabled. To edit route details, hover and click **Edit**![Edit Pencil](https://clear.ml/docs/latest/icons/ico-edit.svg)
in the **Static Routes** table.

An enabled route is view-only. To view its details, hover and click **View route configuration**![Info](https://clear.ml/docs/latest/icons/ico-info.svg)
in the **Static Routes** table.

### Deleting Routes [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/\#deleting-routes "Direct link to Deleting Routes")

To delete a static route details, hover and click **Delete**![Trash](https://clear.ml/docs/latest/icons/ico-trash.svg)
in the **Static Routes** table. Disabling or Deleting a route removes the external endpoint and stops routing any active
connections.

## Access Tokens [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/\#access-tokens "Direct link to Access Tokens")

Tokens provide access to AI Application Gateway endpoints.

Two token types are available:

- User tokens - Grant access according to ClearML user (or service account) identity privileges
- Endpoint tokens - Grant access to designated endpoints regardless of user identity

The **Access Tokens** table lists all manually created tokens in the system. The table shows each token's:

- Label
- Type - User or Endpoint
- Creation Time
- Expiration Time
- Scope - The token access privileges: user identity for user tokens or endpoint list for endpoint tokens
- Metadata - Additional key-value metadata attached to the token (for endpoint tokens)
- Created by - User who generated the token

![Application Gateway token table](https://clear.ml/docs/latest/assets/images/settings_app_gateway_tokens-71e2aa14069f4392f028a73b2477fcd4.png#light-mode-only)![Application Gateway token table](https://clear.ml/docs/latest/assets/images/settings_app_gateway_tokens_dark-ac7b96931877afe247c48707839f22a9.png#dark-mode-only)

You can search ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg)
the tokens list by label or username.

### Generating an Access Token [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/\#generating-an-access-token "Direct link to Generating an Access Token")

To generate an access token:

1. Click **Generate a Token**
2. Select the token type and enter token details:
   - User token
     - `Label` \- A descriptive name for the token
     - `User` \- The ClearML user identity whose privileges will be used for authorizing endpoint access
     - `Expiration` \- The number of days the token should remain valid
   - Endpoint token
     - `Label` \- A descriptive name for the token
     - `Endpoints` \- Select the endpoints the token will authorize access to (out of the non-public endpoints available under Static Routes).
     - `Additional Token Metadata` \- Optional custom key-value metadata attached to the token.
     - `Expiration` \- The number of days the token should remain valid
3. Click `Generate`, which creates a token and copies it to your clipboard

### Revoking an Access Token [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/\#revoking-an-access-token "Direct link to Revoking an Access Token")

To revoke a token, hover over the token's row and click ![Trash](https://clear.ml/docs/latest/icons/ico-trash.svg).

- [Routers](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/#routers)
- [Static Routes](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/#static-routes)
  - [Creating a Static Route](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/#creating-a-static-route)
  - [Editing Routes](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/#editing-routes)
  - [Deleting Routes](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/#deleting-routes)
- [Access Tokens](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/#access-tokens)
  - [Generating an Access Token](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/#generating-an-access-token)
  - [Revoking an Access Token](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_app_gw/#revoking-an-access-token)