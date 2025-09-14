import random
from inspect_ai import Task, task
from inspect_ai.dataset import Dataset, example_dataset

from inspect_ai.scorer import accuracy, grouped, match, stderr
from inspect_ai.solver import generate


@task
def some_task():
    return Task(
        dataset=load_dataset(),
        solver=[generate()],
        scorer=match(),
        metrics=[
            grouped(accuracy(), group_key="category", all_label="all (accuracy)"),
            grouped(stderr(), group_key="category", all_label="all (stderr)"),
        ],
    )


def load_dataset() -> Dataset:
    dataset = example_dataset("theory_of_mind")
    for sample in dataset:
        if sample.metadata is None:
            sample.metadata = {}
        sample.metadata["category"] = random.choice(["red", "green"])
    return dataset
