---
url: "https://clear.ml/docs/latest/docs/integrations/splunk/"
title: "Splunk | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/splunk/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Splunk integration is available under the ClearML Enterprise plan.

Integrating ClearML with Splunk allows you to centralize and analyze API logs for improved monitoring.

## Create a Splunk Index [​](https://clear.ml/docs/latest/docs/integrations/splunk/\#create-a-splunk-index "Direct link to Create a Splunk Index")

1. Log in to your Splunk web application

2. In the **Settings** menu, click **Indexes**

![Splunk Settings menu](https://clear.ml/docs/latest/assets/images/server_splunk_1-89dd8b4fe02e2c6ea28837e3891fcb68.png)

3. In the Indexes page, click **New Index**

4. In the index creation modal, enter Index name (`<SPLUNK_INDEX>`). If you don't need special
settings, keep the default settings for the rest of the fields

5. Click **Save**


## Set Up a Splunk HTTP Event Collector [​](https://clear.ml/docs/latest/docs/integrations/splunk/\#set-up-a-splunk-http-event-collector "Direct link to Set Up a Splunk HTTP Event Collector")

1. In the **Settings** menu, click **Data Inputs**

![Splunk Settings menu](https://clear.ml/docs/latest/assets/images/server_splunk_2-90fbacc84d12ef3c14ccb9f28f89c92a.png)

2. On the **HTTP Event Collector** row, click **\+ Add new**

![Splunk](https://clear.ml/docs/latest/assets/images/server_splunk_3-87bea35f66c2461cdb7be404024e4541.png)

3. On the next page, input a name for your collector and click **Next**

4. On the next page, select your newly created index from the list and add it to the selected items list
on the right

5. Click **Review**

6. Click **Submit**

7. Copy the displayed collector token (`<SPLUNK_TOKEN>`). It will be used in the next steps


## Configure ClearML [​](https://clear.ml/docs/latest/docs/integrations/splunk/\#configure-clearml "Direct link to Configure ClearML")

Configure the ClearML server to send API logs to Splunk using [Docker Compose](https://clear.ml/docs/latest/docs/integrations/splunk/#docker-compose) or [Kubernetes Helm](https://clear.ml/docs/latest/docs/integrations/splunk/#kubernetes-helm):

### Docker Compose [​](https://clear.ml/docs/latest/docs/integrations/splunk/\#docker-compose "Direct link to Docker Compose")

1. Add the following configuration to your `apiserver.conf` file. Make sure to replace `<SPLUNK_URL>`, `<SPLUNK_PORT>`,
`<SPLUNK_TOKEN>`, and `<SPLUNK_INDEX>`.





```text
apilog: {

        adapter: ["logging"],

        adapters: {

          logging: {

            logger_prefix: "",

            formatter: {

              cls: "logstash_formatter.LogstashFormatterV1",

              -kwargs: {}

            },

            handler: {

              cls: "splunk_handler.SplunkHandler",

              -custom_kwargs: {},

              -kwargs: {

                host: "<SPLUNK_URL>",

                port: <SPLUNK_PORT>,

                token: "<SPLUNK_TOKEN>",

                index: "<SPLUNK_INDEX>",

                protocol: https,

                verify: false

              },

            }

          }

        }

      }
```

2. Set the following environment variables:





```text
CLEARML__apiserver__endpoints__debug__ping__log_call=false

CLEARML__apiserver__endpoints___default__log_call=true

CLEARML__apiserver__log_calls=true
```

3. Apply configuration with `docker-compose`:





```text
docker-compose -f docker-compose.yml down

docker-compose -f /opt/clearml/docker-compose.yml --env-file constants.env up -d
```


### Kubernetes Helm [​](https://clear.ml/docs/latest/docs/integrations/splunk/\#kubernetes-helm "Direct link to Kubernetes Helm")

1. Add the following `values.override.yaml` to your ClearML installation specification. Make sure to replace `<SPLUNK_TOKEN>`
and `<SPLUNK_INDEX>` with the values from the previous steps.





```text
apiserver:

     logCalls: true # Sets CLEARML__APISERVER__LOG_CALLS to true

     extraEnvs:

    - name: CLEARML__apiserver__endpoints___default__log_call

      value: "true"

    - name: CLEARML__apiserver__endpoints__debug__ping__log_call

      value: "false"

additionalConfigs:

    apiserver.conf: |

      apilog: {

        adapter: ["logging"],

        adapters: {

          logging: {

            logger_prefix: "",

            formatter: {

              cls: "logstash_formatter.LogstashFormatterV1",

              -kwargs: {}

            },

            handler: {

              cls: "splunk_handler.SplunkHandler",

              -custom_kwargs: {},

              -kwargs: {

                host: "splunk-splunk-standalone-service.splunk.svc.cluster.local",

                port: 8088,

                token: "<SPLUNK_TOKEN>",

                index: "<SPLUNK_INDEX>",

                protocol: https,

                verify: false

              },

            }

          }

        }

      }
```

2. Upgrade the Helm release:





```text
helm upgrade -i clearml-enterprise oci://docker.io/clearml/clearml-enterprise -f values-override.yaml
```


### Exclude API Calls from Logs [​](https://clear.ml/docs/latest/docs/integrations/splunk/\#exclude-api-calls-from-logs "Direct link to Exclude API Calls from Logs")

To exclude specific API calls from the Splunk logs, add an environment variable with the following
format: `CLEARML__apiserver__endpoints__<SERVICE>__<METHOD>__log_call` and set it to `false`.

For example, the configuration below for servers on K8s Helm exclude the [`POST /debug.ping`](https://clear.ml/docs/latest/docs/references/api/debug#post-debugping)
call from the Splunk logs:

```text
apiserver:

extraEnvs:

    - name: CLEARML__apiserver__endpoints__debug__ping__log_call

      value: "false"
```

- [Create a Splunk Index](https://clear.ml/docs/latest/docs/integrations/splunk/#create-a-splunk-index)
- [Set Up a Splunk HTTP Event Collector](https://clear.ml/docs/latest/docs/integrations/splunk/#set-up-a-splunk-http-event-collector)
- [Configure ClearML](https://clear.ml/docs/latest/docs/integrations/splunk/#configure-clearml)
  - [Docker Compose](https://clear.ml/docs/latest/docs/integrations/splunk/#docker-compose)
  - [Kubernetes Helm](https://clear.ml/docs/latest/docs/integrations/splunk/#kubernetes-helm)
  - [Exclude API Calls from Logs](https://clear.ml/docs/latest/docs/integrations/splunk/#exclude-api-calls-from-logs)