# Class with `dict` features.

*The purpose is to have something like this :*
```py
{
    {"name": "dad"} : {"age": 44}
}
```
*which is not possible because the **key** of a `dict` must be a `hash`.*

# Usage
## Preambule
```py
dad = {"name": "dad"}
mom = {"name": "mom"}
boy = {"name": "son"}
girl = {"name": "daughter"}
president = {"name": "president"}
first_lady = {"name": "first_lady"}

dad_age = {"age": 44}
mom_age = {"age": 43}
boy_age = {"age": 12}
girl_age = {"age": 9}
president_age = {"age": "old"}
first_lady_age = {"age": "young"}
```

## init
Initialize with a kind of `OrderedDict`.
```py
family = NotHashableKeyDict(
    (dad, {"age": 44}),
    (mom, {"age": 43}),
)
```

## set
You can set a key :
```py
family[son] = son_age
```
or
```py
family.set(girl, girl_age)
```

## get
```py
family[son]  # returns {"age": 12}
family.get(girl)  # returns {"age": 9}
family.get(president)  # returns None
family.get(president, "not member...")  # returns "not member..."
```

## pop
```py
family.pop(dad)  # returns {"age": 44}
family.pop(president)  # returns None
family.pop(president, "not member...")  # returns "not member..."
```

## keys, values and items
```py
family.keys() == [
    {"name": "dad"},
    {"name": "mom"},
    {"name": "son"},
    {"name": "daughter"},
]
```

```py
family.values() == [
   {"age": 44},
   {"age": 43},
   {"age": 12},
   {"age": 9},
]
```

```py
family.items() == [
   ({"name": "dad"}, {"age": 44}),
   ({"name": "mom"}, {"age": 43}),
   ({"name": "son"}, {"age": 12}),
   ({"name": "daughter"}, {"age": 9}),
]
```