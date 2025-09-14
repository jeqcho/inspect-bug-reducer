
1. Setup

```
python -m venv .venv
source .venv/bin/activate
pip install inspect-ai
```

2. Open the file `example.py`. `custom_scorer1` receives the following linter error.

```
Argument of type "list[Metric]" cannot be assigned to parameter "metrics" of type "list[Metric | dict[str, list[Metric]]] | dict[str, list[Metric]]" in function "scorer"
  Type "list[Metric]" is not assignable to type "list[Metric | dict[str, list[Metric]]] | dict[str, list[Metric]]"
    "list[Metric]" is not assignable to "list[Metric | dict[str, list[Metric]]]"
      Type parameter "_T@list" is invariant, but "Metric" is not the same as "Metric | dict[str, list[Metric]]"
      Consider switching from "list" to "Sequence" which is covariant
    "list[Metric]" is not assignable to "dict[str, list[Metric]]"basedpyright[reportArgumentType](https://docs.basedpyright.com/v1.31.3/configuration/config-files/#reportArgumentType)
```

3. The errors will go away if `inspect_ai.scorer._scorer.scorer` changes its argument type from `list` to `Sequence`, i.e.
```python
metrics: list[Metric | dict[str, list[Metric]]] | dict[str, list[Metric]]
```
to
```python
metrics: Sequence[Metric | dict[str, Sequence[Metric]]] | dict[str, Sequence[Metric]]
```

4. `custom_scorer2` now has linter errors. To maintain compatibility with existing code, further change the argument type from `dict` to `Mapping`.

```python
metrics: Sequence[Metric | Mapping[str, Sequence[Metric]]] | Mapping[str, Sequence[Metric]]
```