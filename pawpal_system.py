from dataclasses import dataclass, field
from typing import List


@dataclass
class Owner:
    name: str
    available_time: int
    preferences: str = ""


@dataclass
class Task:
    title: str
    category: str
    duration: int
    priority: int
    completed: bool = False

    def mark_complete(self) -> None:
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task_title: str) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass


class Scheduler:
    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        pass

    def generate_daily_plan(self, tasks: List[Task], available_time: int) -> List[Task]:
        pass

    def explain_plan(self, selected_tasks: List[Task], skipped_tasks: List[Task]) -> str:
        pass