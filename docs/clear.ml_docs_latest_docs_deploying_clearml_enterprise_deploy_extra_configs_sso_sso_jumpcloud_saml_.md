---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_jumpcloud_saml/"
title: "JumpCloud SAML | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_jumpcloud_saml/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This guide explains how to configure JumpCloud as a SAML identity provider for ClearML Single Sign-On (SSO):

1. Register and Configure the ClearML application in JumpCloud
2. Identity service configuration in the ClearML Server
3. Optionally, configure automatic user creation by assigning a default company.

## Configure JumpCloud [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_jumpcloud_saml/\#configure-jumpcloud "Direct link to Configure JumpCloud")

1. Go to the JumpCloud Admin console and define ClearML app as a **Generic SAML Service Provider** with the following parameters:

   - Entity ID - `clearml`
   - Callback URL - `<the_url_of_clearml_webapp_in_your_deployment>/callback_jumpcloudsaml`
2. Configure the SAML response attributes:
   - `emailaddress` \- User email
   - `objectidentifier` \- User ID in the IdP
   - `displayname` \- Username for the display
3. Generate the IdP metadata file and save the file and entity ID, which you will use when configuring ClearML Server

## Configure ClearML Server [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_jumpcloud_saml/\#configure-clearml-server "Direct link to Configure ClearML Server")

1. Prepare the deployment with the user IdP metadata file mapped into the `apiserver`.

2. Set the following environment variables:
   - `CLEARML__SECURE__LOGIN__SSO__SAML_CLIENT__JUMPCLOUDSAML__ENTITY_ID=clearml`
   - `CLEARML__SECURE__LOGIN__SSO__SAML_CLIENT__JUMPCLOUDSAML__IDP_METADATA_FILE=<path to the metadata file>`
   - `CLEARML__SECURE__LOGIN__SSO__SAML_CLIENT__JUMPCLOUDSAML__DEFAULT_COMPANY=<company_id>`

- [Configure JumpCloud](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_jumpcloud_saml/#configure-jumpcloud)
- [Configure ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_jumpcloud_saml/#configure-clearml-server)