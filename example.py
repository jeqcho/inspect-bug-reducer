from inspect_ai import Task, task
from inspect_ai._eval.task.epochs import Epochs
from inspect_ai.dataset import example_dataset

from inspect_ai.scorer import match, score_reducer
from inspect_ai.scorer._metric import Score
from inspect_ai.scorer._reducer.types import ScoreReducer
from inspect_ai.solver import generate


@task
def task_using_custom_reducer():
    return Task(
        dataset=example_dataset("theory_of_mind"),
        solver=[generate()],
        scorer=match(),
        epochs=Epochs(10, ["a_custom_score_reducer"]),
    )


@score_reducer
def a_custom_score_reducer() -> ScoreReducer:
    def reduce(scores: list[Score]) -> Score:
        return Score(value=0)

    return reduce