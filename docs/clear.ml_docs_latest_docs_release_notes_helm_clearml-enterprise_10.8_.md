---
url: "https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/"
title: "Version 10.8 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### clearml-enterprise 10.8.18 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-10818 "Direct link to clearml-enterprise 10.8.18")

**New Features and Improvements**

- Increase default Apps Agent `maxPods` value

### clearml-enterprise 10.8.17 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-10817 "Direct link to clearml-enterprise 10.8.17")

**Bug Fixes**

- Fix Apps Agent override image credentials not being propagated correctly

### clearml-enterprise 10.8.16 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-10816 "Direct link to clearml-enterprise 10.8.16")

**New Features and Improvements**

- Enable RBAC by default

### clearml-enterprise 10.8.15 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-10815 "Direct link to clearml-enterprise 10.8.15")

**New Features and Improvements**

- Support configuring custom API and file server URLs with `WEBSERVER__displayedServerUrls`

### clearml-enterprise 10.8.14 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-10814 "Direct link to clearml-enterprise 10.8.14")

**New Features and Improvements**

- Update image tags

### clearml-enterprise 10.8.13 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-10813 "Direct link to clearml-enterprise 10.8.13")

**New Features and Improvements**

- Add `customCertificates` support for `clearmlApplications`

**Bug Fixes**

- Fix `clearmlCheckCertificate` not being correctly propagated

### clearml-enterprise 10.8.12 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-10812 "Direct link to clearml-enterprise 10.8.12")

**New Features and Improvements**

- Add `dnsPolicy`, `dnsConfig` and `hostAliases` options to `apiserver`, `webserver`, `fileserver` and apps deployments.
- Update image tags

**Bug Fixes**

- Fix Task Cleaner unable to authenticate to MongoDB when credentials are provided in the connection string

### clearml-enterprise 10.8.11 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-10811 "Direct link to clearml-enterprise 10.8.11")

**New Features and Improvements**

- Update image tags

**Bug Fixes**

- Fix Task Cleaner unable to authenticate to MongoDB when credentials are provided in the connection string

### clearml-enterprise 10.8.10 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-10810 "Direct link to clearml-enterprise 10.8.10")

**New Features and Improvements**

- Add support for extra environment variables in Task Cleaner

### clearml-enterprise 10.8.9 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-1089 "Direct link to clearml-enterprise 10.8.9")

**New Features and Improvements**

- Update image tags

### clearml-enterprise 10.8.8 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-1088 "Direct link to clearml-enterprise 10.8.8")

**New Features and Improvements**

- Update image tags

### clearml-enterprise 10.8.7 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-1087 "Direct link to clearml-enterprise 10.8.7")

**New Features and Improvements**

- Update default `hiddenWorkersPatterns`

**Bug Fixes**

- Fix incorrect `appVersion` value in Helm chart

### clearml-enterprise 10.8.6 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-1086 "Direct link to clearml-enterprise 10.8.6")

**New Features and Improvements**

- Improve `ingressCatchAll` behavior

### clearml-enterprise 10.8.5 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-1085 "Direct link to clearml-enterprise 10.8.5")

**Bug Fixes**

- Fix MongoDB image typo

### clearml-enterprise 10.8.4 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-1084 "Direct link to clearml-enterprise 10.8.4")

**New Features and Improvements**

- Update image tags

### clearml-enterprise 10.8.3 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-1083 "Direct link to clearml-enterprise 10.8.3")

**Bug Fixes**

- Fix Bitnami dependency issue

### clearml-enterprise 10.8.2 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-1082 "Direct link to clearml-enterprise 10.8.2")

**New Features and Improvements**

- Set `CLEARML__apiserver__mongo__ensure_db_version_on_startup=false` automatically when using an external MongoDB

### clearml-enterprise 10.8.1 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-1081 "Direct link to clearml-enterprise 10.8.1")

**New Features and Improvements**

- Update image tags

### clearml-enterprise 10.8.0 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/\#clearml-enterprise-1080 "Direct link to clearml-enterprise 10.8.0")

**New Features and Improvements**

- Update MongoDB to v7
- Update ClearML Enterprise Server to [v3.26](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_26#enterprise-server-3260)

- [clearml-enterprise 10.8.18](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-10818)
- [clearml-enterprise 10.8.17](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-10817)
- [clearml-enterprise 10.8.16](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-10816)
- [clearml-enterprise 10.8.15](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-10815)
- [clearml-enterprise 10.8.14](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-10814)
- [clearml-enterprise 10.8.13](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-10813)
- [clearml-enterprise 10.8.12](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-10812)
- [clearml-enterprise 10.8.11](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-10811)
- [clearml-enterprise 10.8.10](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-10810)
- [clearml-enterprise 10.8.9](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-1089)
- [clearml-enterprise 10.8.8](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-1088)
- [clearml-enterprise 10.8.7](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-1087)
- [clearml-enterprise 10.8.6](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-1086)
- [clearml-enterprise 10.8.5](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-1085)
- [clearml-enterprise 10.8.4](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-1084)
- [clearml-enterprise 10.8.3](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-1083)
- [clearml-enterprise 10.8.2](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-1082)
- [clearml-enterprise 10.8.1](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-1081)
- [clearml-enterprise 10.8.0](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise/10.8/#clearml-enterprise-1080)