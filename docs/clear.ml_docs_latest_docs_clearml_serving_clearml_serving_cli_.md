---
url: "https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/"
title: "ClearML Serving CLI | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The `clearml-serving` utility is a CLI tool for model deployment and orchestration.

The following page provides a reference for `clearml-serving`'s CLI commands:

- [list](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#list) \- List running Serving Services
- [create](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#create) \- Create a new Serving Service
- [metrics](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#metrics) \- Configure inference metrics Service
- [config](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#config) \- Configure a new Serving Service
- [model](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#model) \- Configure model endpoints for a running Service

## Global Parameters [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#global-parameters "Direct link to Global Parameters")

```bash
clearml-serving [-h] [--debug] [--yes] [--id ID] {list,create,metrics,config,model}
```

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | Serving Service (Control plane) Task ID to configure (if not provided, automatically detect the running control plane Task) | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--debug` | Print debug messages | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--yes` | Always answer YES on interactive inputs | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

Service ID

The Serving Service's ID (`--id`) is required to execute the `metrics`, `config`, and `model` commands.

## list [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#list "Direct link to list")

List running Serving Services.

```bash
clearml-serving list [-h]
```

## create [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#create "Direct link to create")

Create a new Serving Service.

```bash
clearml-serving create [-h] [--name NAME] [--tags TAGS [TAGS ...]] [--project PROJECT]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--name` | Serving service's name. Default: `Serving-Service` | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--project` | Serving service's project. Default: `DevOps` | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--tags` | Serving service's user tags. The serving service can be labeled, which can be useful for organizing | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## metrics [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#metrics "Direct link to metrics")

Configure inference metrics Service.

```bash
clearml-serving metrics [-h] {add,remove,list}
```

### add [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#add "Direct link to add")

Add/modify metric for a specific endpoint.

```bash
clearml-serving metrics add [-h] --endpoint ENDPOINT [--log-freq LOG_FREQ]

                            [--variable-scalar VARIABLE_SCALAR [VARIABLE_SCALAR ...]]

                            [--variable-enum VARIABLE_ENUM [VARIABLE_ENUM ...]]

                            [--variable-value VARIABLE_VALUE [VARIABLE_VALUE ...]]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--endpoint` | Metric endpoint name including version (e.g. `"model/1"` or a prefix `"model/*"`). Notice: it will override any previous endpoint logged metrics | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--log-freq` | Logging request frequency, between 0.0 to 1.0. Example: 1.0 means all requests are logged, 0.5 means half of the requests are logged if not specified. To use global logging frequency, see [`config --metric-log-freq`](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#config) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--variable-scalar` | Add float (scalar) argument to the metric logger, `<name>=<histogram>`. Example: with specific buckets: `"x1=0,0.2,0.4,0.6,0.8,1"` or with min/max/num\_buckets `"x1=0.0/1.0/5"`. Notice: In cases where 1000s of requests per second reach the serving, it makes no sense to display every datapoint. So scalars can be divided in buckets, and for each minute for example. Then it's possible to calculate what % of the total traffic fell in bucket 1, bucket 2, bucket 3 etc. The Y axis represents the buckets, color is the value in % of traffic in that bucket, and X is time. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--variable-enum` | Add enum (string) argument to the metric logger, `<name>=<optional_values>`. Example: `"detect=cat,dog,sheep"` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--variable-value` | Add non-samples scalar argument to the metric logger, `<name>`. Example: `"latency"` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

### remove [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#remove "Direct link to remove")

Remove metric from a specific endpoint.

```bash
clearml-serving metrics remove [-h] [--endpoint ENDPOINT]

                               [--variable VARIABLE [VARIABLE ...]]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--endpoint` | Metric endpoint name including version (e.g. `"model/1"` or a prefix `"model/*"`) | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--variable` | Remove (scalar/enum) argument from the metric logger, `<name>` example: `"x1"` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

### list [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#list-1 "Direct link to list")

List metrics logged on all endpoints.

```bash
clearml-serving metrics list [-h]
```

## config [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#config "Direct link to config")

Configure a new Serving Service.

```bash
clearml-serving config [-h] [--base-serving-url BASE_SERVING_URL]

                       [--triton-grpc-server TRITON_GRPC_SERVER]

                       [--kafka-metric-server KAFKA_METRIC_SERVER]

                       [--metric-log-freq METRIC_LOG_FREQ]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--base-serving-url` | External base serving service url. Example: `http://127.0.0.1:8080/serve` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--triton-grpc-server` | External ClearML-Triton serving container gRPC address. Example: `127.0.0.1:9001` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--kafka-metric-server` | External Kafka service url. Example: `127.0.0.1:9092` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--metric-log-freq` | Set default metric logging frequency between 0.0 to 1.0. 1.0 means that 100% of all requests are logged | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## model [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#model "Direct link to model")

Configure model endpoints for an already running Service.

```bash
clearml-serving model [-h] {list,remove,upload,canary,auto-update,add}
```

### list [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#list-2 "Direct link to list")

List current models.

```bash
clearml-serving model list [-h]
```

### remove [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#remove-1 "Direct link to remove")

Remove model by its endpoint name.

```bash
clearml-serving model remove [-h] [--endpoint ENDPOINT]
```

**Parameter**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--endpoint` | Model endpoint name | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |

### upload [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#upload "Direct link to upload")

Upload and register model files/folder.

```bash
clearml-serving model upload [-h] --name NAME [--tags TAGS [TAGS ...]] --project PROJECT

                             [--framework {tensorflow,tensorflowjs,tensorflowlite,pytorch,torchscript,caffe,caffe2,onnx,keras,mknet,cntk,torch,darknet,paddlepaddle,scikitlearn,xgboost,lightgbm,parquet,megengine,catboost,tensorrt,openvino,custom}]

                             [--publish] [--path PATH] [--url URL]

                             [--destination DESTINATION]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--name` | Specifying the model name to be registered in | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--tags` | Add tags to the newly created model | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--project` | Specify the project for the model to be registered in | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--framework` | Specify the model framework. Options are: 'tensorflow', 'tensorflowjs', 'tensorflowlite', 'pytorch', 'torchscript', 'caffe', 'caffe2', 'onnx', 'keras', 'mknet', 'cntk', 'torch', 'darknet', 'paddlepaddle', 'scikitlearn', 'xgboost', 'lightgbm', 'parquet', 'megengine', 'catboost', 'tensorrt', 'openvino', 'custom' | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--publish` | Publish the newly created model (change model state to "published" (i.e. locked and ready to deploy) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--path` | Specify a model file/folder to be uploaded and registered | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--url` | Specify an already uploaded model url (e.g. `s3://bucket/model.bin`, `gs://bucket/model.bin`) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--destination` | Specify the target destination for the model to be uploaded. For example: <br>- S3: `s3://bucket/folder`<br>- Non-AWS S3-like services (such as MinIO): `s3://host_addr:port/bucket`. **Note that port specification is required**.<br>- Google Cloud Storage: `gs://bucket-name/folder`<br>- Azure Storage: `azure://<account name>.blob.core.windows.net/path/to/file` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

### canary [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#canary "Direct link to canary")

Add model Canary/A/B endpoint.

```bash
clearml-serving model canary [-h] [--endpoint ENDPOINT] [--weights WEIGHTS [WEIGHTS ...]]

                             [--input-endpoints INPUT_ENDPOINTS [INPUT_ENDPOINTS ...]]

                             [--input-endpoint-prefix INPUT_ENDPOINT_PREFIX]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--endpoint` | Model canary serving endpoint name (e.g. `my_model/latest`) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--weights` | Model canary weights (order matching model ep), (e.g. 0.2 0.8) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--input-endpoints` | Model endpoint prefixes, can also include version (e.g. `my_model`, `my_model/v1`) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--input-endpoint-prefix` | Model endpoint prefix, lexicographic order or by version `<int>` (e.g. `my_model/1`, `my_model/v1`), where the first weight matches the last version. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

### auto-update [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#auto-update "Direct link to auto-update")

Add/Modify model auto-update service.

```bash
clearml-serving model auto-update [-h] [--endpoint ENDPOINT] --engine ENGINE

                                  [--max-versions MAX_VERSIONS] [--name NAME]

                                  [--tags TAGS [TAGS ...]] [--project PROJECT]

                                  [--published] [--preprocess PREPROCESS]

                                  [--input-size INPUT_SIZE [INPUT_SIZE ...]]

                                  [--input-type INPUT_TYPE] [--input-name INPUT_NAME]

                                  [--output-size OUTPUT_SIZE [OUTPUT_SIZE ...]]

                                  [--output_type OUTPUT_TYPE] [--output-name OUTPUT_NAME]

                                  [--aux-config AUX_CONFIG [AUX_CONFIG ...]]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--endpoint` | Base model endpoint (must be unique) | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--engine` | Model endpoint serving engine (triton, sklearn, xgboost, lightgbm) | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--max-versions` | Max versions to store (and create endpoints) for the model. Highest number is the latest version | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--name` | Specify model name to be selected and auto-updated (notice regexp selection use `"$name^"` for exact match) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--tags` | Specify tags to be selected and auto-updated | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--project` | Specify model project to be selected and auto-updated | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--published` | Only select published model for auto-update | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--preprocess` | Specify Pre/Post processing code to be used with the model (point to local file / folder) - this should hold for all the models | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--input-size` | Specify the model matrix input size \[Rows x Columns X Channels etc ...\] | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--input-type` | Specify the model matrix input type. Examples: uint8, float32, int16, float16 etc. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--input-name` | Specify the model layer pushing input into. Example: layer\_0 | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--output-size` | Specify the model matrix output size \[Rows x Columns X Channels etc ...\] | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--output_type` | Specify the model matrix output type. Examples: uint8, float32, int16, float16 etc. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--output-name` | Specify the model layer pulling results from. Examples: layer\_99 | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--aux-config` | Specify additional engine specific auxiliary configuration in the form of key=value. Example: `platform=onnxruntime_onnx response_cache.enable=true max_batch_size=8`. Notice: you can also pass a full configuration file (e.g. Triton "config.pbtxt") | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

### add [​](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/\#add-1 "Direct link to add")

Add/Update model.

```bash
clearml-serving model add [-h] --engine ENGINE --endpoint ENDPOINT [--version VERSION]

                          [--model-id MODEL_ID] [--preprocess PREPROCESS]

                          [--input-size INPUT_SIZE [INPUT_SIZE ...]]

                          [--input-type INPUT_TYPE] [--input-name INPUT_NAME]

                          [--output-size OUTPUT_SIZE [OUTPUT_SIZE ...]]

                          [--output-type OUTPUT_TYPE] [--output-name OUTPUT_NAME]

                          [--aux-config AUX_CONFIG [AUX_CONFIG ...]] [--name NAME]

                          [--tags TAGS [TAGS ...]] [--project PROJECT] [--published]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--engine` | Model endpoint serving engine (triton, sklearn, xgboost, lightgbm) | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--endpoint` | Base model endpoint (must be unique) | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--version` | Model endpoint version (default: None) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--model-id` | Specify a model ID to be served | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--preprocess` | Specify Pre/Post processing code to be used with the model (point to local file / folder) - this should hold for all the models | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--input-size` | Specify the model matrix input size \[Rows x Columns X Channels etc ...\] | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--input-type` | Specify the model matrix input type. Examples: uint8, float32, int16, float16 etc. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--input-name` | Specify the model layer pushing input into. Example: layer\_0 | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--output-size` | Specify the model matrix output size \[Rows x Columns X Channels etc ...\] | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--output_type` | Specify the model matrix output type. Examples: uint8, float32, int16, float16 etc. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--output-name` | Specify the model layer pulling results from. Examples: layer\_99 | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--aux-config` | Specify additional engine specific auxiliary configuration in the form of key=value. Example: `platform=onnxruntime_onnx response_cache.enable=true max_batch_size=8`. Notice: you can also pass a full configuration file (e.g. Triton "config.pbtxt") | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--name` | Instead of specifying `--model-id` select based on model name | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--tags` | Specify tags to be selected and auto-updated | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--project` | Instead of specifying `--model-id` select based on model project | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--published` | Instead of specifying `--model-id` select based on model published | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

- [Global Parameters](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#global-parameters)
- [list](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#list)
- [create](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#create)
- [metrics](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#metrics)
  - [add](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#add)
  - [remove](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#remove)
  - [list](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#list-1)
- [config](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#config)
- [model](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#model)
  - [list](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#list-2)
  - [remove](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#remove-1)
  - [upload](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#upload)
  - [canary](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#canary)
  - [auto-update](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#auto-update)
  - [add](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_cli/#add-1)