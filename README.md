
1. Setup

```
python -m venv .venv
source .venv/bin/activate
pip install inspect-ai
```

2. Run eval.

```
inspect eval example.py --model mockllm/model
```

The output will look something like

```
match                                                                                                                                                           
red             0.000                                                                                                                                           
green           0.000                                                                                                                                           
all (accuracy)  0.000                                                                                                                                           
red2            0.000                                                                                                                                           
green2          0.000                                                                                                                                           
all (stderr)    0.000 
```

Ideally we instead want something like

```
match
red (accuracy)     0.000
green (accuracy)   0.000
all (accuracy)     0.000
red (stderr)       0.000
green2 (stderr)    0.000
all (stderr)       0.000
```