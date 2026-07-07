---
url: "https://clear.ml/docs/latest/docs/references/sdk/http_router/"
title: "HttpRouter | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/http_router/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ router.router.HttpRouter(task) [​](https://clear.ml/docs/latest/docs/references/sdk/http_router/\#class-routerrouterhttproutertask "Direct link to class-routerrouterhttproutertask")

A router class to manage HTTP routing for an application.
Allows the creation, deployment, and management of local and external endpoints,
as well as the configuration of a local proxy for traffic routing.

Example usage:

```py
def request_callback(request, persistent_state):

    persistent_state["last_request_time"] = time.time()

def response_callback(response, request, persistent_state):

    print("Latency:", time.time() - persistent_state["last_request_time"])

    if urllib.parse.urlparse(str(request.url).rstrip("/")).path == "/modify":

        new_content = response.body.replace(b"modify", b"modified")

        headers = copy.deepcopy(response.headers)

        headers["Content-Length"] = str(len(new_content))

        return Response(status_code=response.status_code, headers=headers, content=new_content)

router = Task.current_task().get_http_router()

router.set_local_proxy_parameters(incoming_port=9000)

router.create_local_route(

    source="/",

    target="http://localhost:8000",

    request_callback=request_callback,

    response_callback=response_callback,

    endpoint_telemetry={"model": "MyModel"}

)

router.deploy(wait=True)
```

Do not use directly. Use Task.get\_router instead

- **Parameters**

**task** ( _Any_ ) –


* * *

### create\_local\_route [​](https://clear.ml/docs/latest/docs/references/sdk/http_router/\#create_local_route "Direct link to create_local_route")

**create\_local\_route(source, target, request\_callback=None, response\_callback=None, endpoint\_telemetry=True, error\_callback=None)**

Create a local route from a source to a target through a proxy. If no proxy instance
exists, one is automatically created.
This function enables routing traffic between the source and target endpoints, optionally
allowing custom callbacks to handle requests and responses or to gather telemetry data
at the endpoint.
To customize proxy parameters, use the Router.set\_local\_proxy\_parameters method.
By default, the proxy binds to port 9000 for incoming requests.

- **Parameters**


  - **source** (`str`) – The source path for routing the traffic. For example, / will intercept
    all the traffic sent to the proxy, while /example will only intercept the calls
    that have /example as the path prefix.

  - **target** (`str`) – The target URL where the intercepted traffic is routed.

  - **request\_callback** (`Optional`\[`Callable`\[\[`Request`\], `Dict`\]\]) – A function used to process each request before it is forwarded to the target.
    The callback must have the following parameters:
    - request - The intercepted FastAPI request

    - persistent\_state - A dictionary meant to be used as a caching utility object.

Shared with response\_callback and error\_callback.
The callback can return a FastAPI Request, in which case this request will be forwarded to the target

  - **response\_callback** (`Optional`\[`Callable`\[\[`Response`, `Request`\], `Dict`\]\]) – A function used to process each response before it is returned by the proxy.
    The callback must have the following parameters:
    - response - The FastAPI response

    - request - The FastAPI request (after being preprocessed by the proxy)

    - persistent\_state - A dictionary meant to be used as a caching utility object.

Shared with request\_callback and error\_callback
The callback can return a FastAPI Response, in which case this response will be forwarded

  - **endpoint\_telemetry** (`Union`\[`bool`, `Dict`\]) – If True, enable endpoint telemetry. If False, disable it.
    If a dictionary is passed, enable endpoint telemetry with custom parameters.
    The parameters are:
    - endpoint\_url - URL to the endpoint, mandatory if no external URL has been requested

    - endpoint\_name - name of the endpoint

    - model\_name - name of the model served by the endpoint

    - model - referenced model

    - model\_url - URL to the model

    - model\_source - Source of the model

    - model\_version - Model version

    - app\_id - App ID, if used inside a ClearML app

    - app\_instance - The ID of the instance the ClearML app is running

    - tags - ClearML tags

    - system\_tags - ClearML system tags

    - container\_id - Container ID, should be unique

    - input\_size - input size of the model

    - input\_type - input type expected by the model/endpoint

    - report\_statistics - whether to report statistics
  - **error\_callback** (`Optional`\[`Callable`\[\[`Request`, `Exception`\], `Dict`\]\]) – Callback to be called on request error.
    The callback must have the following parameters:
    - request - the FastAPI request which caused the error

    - error - an exception which indicates which error occurred

    - persistent\_state - A dictionary meant to be used as a caching utility object.

Shared with request\_callback and response\_callback

- **Return type**

`None`


* * *

### deploy [​](https://clear.ml/docs/latest/docs/references/sdk/http_router/\#deploy "Direct link to deploy")

**deploy(wait=False, wait\_interval\_seconds=3.0, wait\_timeout\_seconds=90.0, static\_route=None)**

Start the local HTTP proxy and request an external endpoint for an application

- **Parameters**
  - **port** – Port the application is listening to. If no port is supplied, a local proxy
    will be created. To control the proxy parameters, use Router.set\_local\_proxy\_parameters.
    To control create local routes through the proxy, use Router.create\_local\_route.
    By default, the incoming port bound by the proxy is 9000

  - **protocol** – As of now, only http is supported

  - **wait** (`bool`) – If True, wait for the endpoint to be assigned

  - **wait\_interval\_seconds** (`float`) – The poll frequency when waiting for the endpoint

  - **wait\_timeout\_seconds** (`float`) – If this timeout is exceeded while waiting for the endpoint,
    the method will no longer wait and None will be returned

  - **static\_route** (`Optional`\[`str`\]) – The static route name (not the route path).
    When set, the external endpoint requested will use this route
    instead of generating it based on the task ID. Useful for creating
    persistent, load balanced routes.
- **Return type**

`Optional`\[`Dict`\]

- **Returns**

If wait is False, this method will return None. If no endpoint could be found while waiting, this method returns None. Otherwise, it returns a dictionary containing the following values:
  - `endpoint` \- raw endpoint. One might need to authenticate in order to use this endpoint

  - `browser_endpoint` \- endpoint to be used in browser. Authentication will be handled via the browser

  - `port` \- the port exposed by the application

  - `protocol` \- the protocol used by the endpoint

* * *

### list\_external\_endpoints [​](https://clear.ml/docs/latest/docs/references/sdk/http_router/\#list_external_endpoints "Direct link to list_external_endpoints")

**list\_external\_endpoints()**

List all external endpoints assigned

- **Return type**

`List`\[`Dict`\]

- **Returns**

A list of dictionaries. Each dictionary contains the following values:
  - `endpoint` \- raw endpoint. One might need to authenticate in order to use this endpoint

  - `browser_endpoint` \- endpoint to be used in browser. Authentication will be handled via the browser

  - `port` \- the port exposed by the application

  - `protocol` \- the protocol used by the endpoint

* * *

### remove\_local\_route [​](https://clear.ml/docs/latest/docs/references/sdk/http_router/\#remove_local_route "Direct link to remove_local_route")

**remove\_local\_route(source)**

Remove a local route. If endpoint telemetry is enabled for that route, disable it

- **Parameters**

**source** (`str`) – Remove route based on the source path used to route the traffic

- **Return type**

`None`


* * *

### set\_local\_proxy\_parameters [​](https://clear.ml/docs/latest/docs/references/sdk/http_router/\#set_local_proxy_parameters "Direct link to set_local_proxy_parameters")

**set\_local\_proxy\_parameters(incoming\_port=None, default\_target=None, log\_level=None, access\_log=True, enable\_streaming=True)**

Set the parameters with which the local proxy is initialized

- **Parameters**
  - **incoming\_port** (`Optional`\[`int`\]) – The incoming port of the proxy

  - **default\_target** (`Optional`\[`str`\]) – If None, no default target is set. Otherwise, route all traffic
    that doesn’t match a local route created via create\_local\_route to this target

  - **log\_level** (`Optional`\[`str`\]) – Python log level for the proxy, one of:
    ‘critical’, ‘error’, ‘warning’, ‘info’, ‘debug’, ‘trace’

  - **access\_log** (`bool`) – Enable/Disable access log

  - **enable\_streaming** (`bool`) – If True, enable streaming of responses with the transfer-encoding header set.
    If False, no response will be streamed
- **Return type**

`None`


* * *

### start\_local\_proxy [​](https://clear.ml/docs/latest/docs/references/sdk/http_router/\#start_local_proxy "Direct link to start_local_proxy")

**start\_local\_proxy()**

Start the local proxy without deploying the router, i.e. requesting an external endpoint

- **Return type**

`None`


* * *

### wait\_for\_external\_endpoint [​](https://clear.ml/docs/latest/docs/references/sdk/http_router/\#wait_for_external_endpoint "Direct link to wait_for_external_endpoint")

**wait\_for\_external\_endpoint(wait\_interval\_seconds=3.0, wait\_timeout\_seconds=90.0)**

Wait for an external endpoint to be assigned

- **Parameters**
  - **wait\_interval\_seconds** (`float`) – The poll frequency when waiting for the endpoint

  - **wait\_timeout\_seconds** (`float`) – If this timeout is exceeded while waiting for the endpoint,
    the method will no longer wait
- **Return type**

`Optional`\[`Dict`\]

- **Returns**

If no endpoint could be found while waiting, this method returns None. Otherwise, it returns a dictionary containing the following values:
  - `endpoint` \- raw endpoint. One might need to authenticate in order to use this endpoint

  - `browser_endpoint` \- endpoint to be used in browser. Authentication will be handled via the browser

  - `port` \- the port exposed by the application

  - `protocol` \- the protocol used by the endpoint

- [_class_ router.router.HttpRouter(task)](https://clear.ml/docs/latest/docs/references/sdk/http_router/#class-routerrouterhttproutertask)
  - [create\_local\_route](https://clear.ml/docs/latest/docs/references/sdk/http_router/#create_local_route)
  - [deploy](https://clear.ml/docs/latest/docs/references/sdk/http_router/#deploy)
  - [list\_external\_endpoints](https://clear.ml/docs/latest/docs/references/sdk/http_router/#list_external_endpoints)
  - [remove\_local\_route](https://clear.ml/docs/latest/docs/references/sdk/http_router/#remove_local_route)
  - [set\_local\_proxy\_parameters](https://clear.ml/docs/latest/docs/references/sdk/http_router/#set_local_proxy_parameters)
  - [start\_local\_proxy](https://clear.ml/docs/latest/docs/references/sdk/http_router/#start_local_proxy)
  - [wait\_for\_external\_endpoint](https://clear.ml/docs/latest/docs/references/sdk/http_router/#wait_for_external_endpoint)