---
url: "https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-app-gateway/3.2/"
title: "Version 3.2 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-app-gateway/3.2/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### clearml-enterprise-app-gateway 3.2.0 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-app-gateway/3.2/\#clearml-enterprise-app-gateway-320 "Direct link to clearml-enterprise-app-gateway 3.2.0")

**New Features and Improvements**

- Update router image to v2.16.0 (Docker Hardened Image)
- Update proxy image to v1.9.0 (Docker Hardened Image)
- Update `OpenResty` Lua mount path to `/opt/openresty/nginx/lua` to match Docker Hardened Image layout
- Render `ROUTER__WEBSERVER__AUTO_RELOAD_CONFIG` environment variable only when `proxy.autoReloadConfig` is set

- [clearml-enterprise-app-gateway 3.2.0](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-app-gateway/3.2/#clearml-enterprise-app-gateway-320)