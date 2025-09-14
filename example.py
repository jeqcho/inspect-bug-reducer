from inspect_ai import Task, task
from inspect_ai.dataset import example_dataset

from inspect_ai.scorer import Metric, accuracy, match, scorer, stderr
from inspect_ai.solver import generate

# ideally we want this to work
def get_metrics1() -> list[Metric]:
    return [accuracy(), stderr()]

@scorer(metrics=get_metrics1()) # linter throws at get_metrics1
def custom_scorer1():
    return match()

# this is the current approach but messy
def get_metrics2() -> list[Metric | dict[str, list[Metric]]] | dict[str, list[Metric]]:
    return [accuracy(), stderr()]

@scorer(metrics=get_metrics2())
def custom_scorer2():
    return match()
