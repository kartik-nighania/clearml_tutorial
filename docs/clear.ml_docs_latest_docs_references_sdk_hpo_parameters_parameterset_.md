---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/"
title: "ParameterSet | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ automation.ParameterSet(parameter\_combinations=()) [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/\#class-automationparametersetparameter_combinations "Direct link to class-automationparametersetparameter_combinations")

Discrete randomly sampled Hyper-Parameter object.

Uniformly sample values form a list of discrete options (combinations) of parameters.

- **Parameters**

**parameter\_combinations** ( _list_ ) – The list/tuple of valid parameter combinations.

For example, two combinations with three specific parameters per combination:





```javascript
[\
\
    {"opt1": 10, "arg2": 20, "arg2": 30},\
\
    {"opt2": 11, "arg2": 22, "arg2": 33}\
\
]
```









Two complex combination each one sampled from a different range:





```javascript
[\
\
    {"opt1": UniformParameterRange('arg1',0,1) , "arg2": 20},\
\
    {"opt2": UniformParameterRange('arg1',11,12), "arg2": 22},\
\
]
```


* * *

### ParameterSet.from\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/\#parametersetfrom_dict "Direct link to ParameterSet.from_dict")

**_classmethod_ from\_dict(a\_dict)**

Construct Parameter object from a dict representation (deserialize from dict).

- **Return type**

`Parameter`

- **Returns**

The Parameter object.

- **Parameters**

**a\_dict** ( _Mapping_ _\[_ _str_ \\*, \\* _str_ _\]_ ) –


* * *

### get\_random\_seed [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/\#get_random_seed "Direct link to get_random_seed")

**static get\_random\_seed()**

Get the global seed for all hyperparameter strategy random number sampling.

- **Return type**

`int`

- **Returns**

The random seed.


* * *

### get\_value [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/\#get_value "Direct link to get_value")

**get\_value()**

Return uniformly sampled value from the valid list of values.

- **Return type**

`Mapping`\[`str`, `Any`\]

- **Returns**

`{self.name: random entry from self.value}`


* * *

### set\_random\_seed [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/\#set_random_seed "Direct link to set_random_seed")

**static set\_random\_seed(seed=1337)**

Set global seed for all hyperparameter strategy random number sampling.

- **Parameters**

**seed** ( _int_ ) – The random seed.

- **Return type**

`None`


* * *

### to\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/\#to_dict "Direct link to to_dict")

**to\_dict()**

Return a dict representation of the Parameter object. Used for serialization of the Parameter object.

- **Return type**

`Mapping`\[`str`, `Union`\[`str`, `Parameter`\]\]

- **Returns**

dict representation of the object (serialization).


* * *

### to\_list [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/\#to_list "Direct link to to_list")

**to\_list()**

Return a list of all the valid values of the Parameter.

- **Return type**

`Sequence`\[`Mapping`\[`str`, `Any`\]\]

- **Returns**

list of dicts `{name: value}`


- [_class_ automation.ParameterSet(parameter\_combinations=())](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/#class-automationparametersetparameter_combinations)
  - [ParameterSet.from\_dict](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/#parametersetfrom_dict)
  - [get\_random\_seed](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/#get_random_seed)
  - [get\_value](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/#get_value)
  - [set\_random\_seed](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/#set_random_seed)
  - [to\_dict](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/#to_dict)
  - [to\_list](https://clear.ml/docs/latest/docs/references/sdk/hpo_parameters_parameterset/#to_list)