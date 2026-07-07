---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/"
title: "DiscreteParameterRange | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ automation.DiscreteParameterRange(name, values=()) [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/\#class-automationdiscreteparameterrangename-values "Direct link to class-automationdiscreteparameterrangename-values")

Discrete randomly sampled hyperparameter object.

Uniformly sample values form a list of discrete options.

- **Parameters**
  - **name** ( _str_ ) – The parameter name. Match the task hyperparameter name.

  - **values** ( _list_ ) – The list/tuple of valid parameter values to sample from.

* * *

### DiscreteParameterRange.from\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/\#discreteparameterrangefrom_dict "Direct link to DiscreteParameterRange.from_dict")

**_classmethod_ from\_dict(a\_dict)**

Construct Parameter object from a dict representation (deserialize from dict).

- **Return type**

`Parameter`

- **Returns**

The Parameter object.

- **Parameters**

**a\_dict** ( _Mapping_ _\[_ _str_ \\*, \\* _str_ _\]_ ) –


* * *

### get\_random\_seed [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/\#get_random_seed "Direct link to get_random_seed")

**static get\_random\_seed()**

Get the global seed for all hyperparameter strategy random number sampling.

- **Return type**

`int`

- **Returns**

The random seed.


* * *

### get\_value [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/\#get_value "Direct link to get_value")

**get\_value()**

Return uniformly sampled value from the valid list of values.

- **Return type**

`Mapping`\[`str`, `Any`\]

- **Returns**

`{self.name: random entry from self.value}`


* * *

### set\_random\_seed [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/\#set_random_seed "Direct link to set_random_seed")

**static set\_random\_seed(seed=1337)**

Set global seed for all hyperparameter strategy random number sampling.

- **Parameters**

**seed** ( _int_ ) – The random seed.

- **Return type**

`None`


* * *

### to\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/\#to_dict "Direct link to to_dict")

**to\_dict()**

Return a dict representation of the Parameter object. Used for serialization of the Parameter object.

- **Return type**

`Mapping`\[`str`, `Union`\[`str`, `Parameter`\]\]

- **Returns**

dict representation of the object (serialization).


* * *

### to\_list [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/\#to_list "Direct link to to_list")

**to\_list()**

Return a list of all the valid values of the Parameter.

- **Return type**

`Sequence`\[`Mapping`\[`str`, `Any`\]\]

- **Returns**

list of dicts `{name: value}`


- [_class_ automation.DiscreteParameterRange(name, values=())](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/#class-automationdiscreteparameterrangename-values)
  - [DiscreteParameterRange.from\_dict](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/#discreteparameterrangefrom_dict)
  - [get\_random\_seed](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/#get_random_seed)
  - [get\_value](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/#get_value)
  - [set\_random\_seed](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/#set_random_seed)
  - [to\_dict](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/#to_dict)
  - [to\_list](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_discreteparameterrange/#to_list)