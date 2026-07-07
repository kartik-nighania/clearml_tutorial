---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/"
title: "UniformIntegerParameterRange | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ automation.UniformIntegerParameterRange(name, min\_value, max\_value, step\_size=1, include\_max\_value=True) [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/\#class-automationuniformintegerparameterrangename-min_value-max_value-step_size1-include_max_valuetrue "Direct link to class-automationuniformintegerparameterrangename-min_value-max_value-step_size1-include_max_valuetrue")

Uniform randomly sampled integer Hyperparameter object.

Create a parameter to be sampled by the SearchStrategy.

- **Parameters**
  - **name** ( _str_ ) – The parameter name. Match the task hyperparameter name.

  - **min\_value** ( _int_ ) – The minimum sample to use for uniform random sampling.

  - **max\_value** ( _int_ ) – The maximum sample to use for uniform random sampling.

  - **step\_size** ( _int_ ) – The default step size is `1`.

  - **include\_max\_value** ( _bool_ ) – Range includes the `max_value`.

    The values are:
    - `True` \- Includes the `max_value` (Default)

    - `False` \- Does not include.

* * *

### UniformIntegerParameterRange.from\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/\#uniformintegerparameterrangefrom_dict "Direct link to UniformIntegerParameterRange.from_dict")

**_classmethod_ from\_dict(a\_dict)**

Construct Parameter object from a dict representation (deserialize from dict).

- **Return type**

`Parameter`

- **Returns**

The Parameter object.

- **Parameters**

**a\_dict** ( _Mapping_ _\[_ _str_ \\*, \\* _str_ _\]_ ) –


* * *

### get\_random\_seed [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/\#get_random_seed "Direct link to get_random_seed")

**static get\_random\_seed()**

Get the global seed for all hyperparameter strategy random number sampling.

- **Return type**

`int`

- **Returns**

The random seed.


* * *

### get\_value [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/\#get_value "Direct link to get_value")

**get\_value()**

Return uniformly sampled value based on object sampling definitions.

- **Return type**

`Mapping`\[`str`, `Any`\]

- **Returns**

`{self.name: random value [self.min_value, self.max_value)}`\
\
\
* * *\
\
### set\_random\_seed [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/\#set_random_seed "Direct link to set_random_seed")\
\
**static set\_random\_seed(seed=1337)**\
\
Set global seed for all hyperparameter strategy random number sampling.\
\
- **Parameters**\
\
**seed** ( _int_ ) – The random seed.\
\
- **Return type**\
\
`None`\
\
\
* * *\
\
### to\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/\#to_dict "Direct link to to_dict")\
\
**to\_dict()**\
\
Return a dict representation of the Parameter object. Used for serialization of the Parameter object.\
\
- **Return type**\
\
`Mapping`\[`str`, `Union`\[`str`, `Parameter`\]\]\
\
- **Returns**\
\
dict representation of the object (serialization).\
\
\
* * *\
\
### to\_list [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/\#to_list "Direct link to to_list")\
\
**to\_list()**\
\
Return a list of all the valid values of the Parameter. If `self.step_size` is not defined, return 100 points\
between minmax values.\
\
- **Return type**\
\
`Sequence`\[`Mapping`\[`str`, `int`\]\]\
\
- **Returns**\
\
list of dicts `{name: int}`\
\
\
- [_class_ automation.UniformIntegerParameterRange(name, min\_value, max\_value, step\_size=1, include\_max\_value=True)](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/#class-automationuniformintegerparameterrangename-min_value-max_value-step_size1-include_max_valuetrue)\
  - [UniformIntegerParameterRange.from\_dict](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/#uniformintegerparameterrangefrom_dict)\
  - [get\_random\_seed](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/#get_random_seed)\
  - [get\_value](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/#get_value)\
  - [set\_random\_seed](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/#set_random_seed)\
  - [to\_dict](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/#to_dict)\
  - [to\_list](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_uniformintegerparameterrange/#to_list)