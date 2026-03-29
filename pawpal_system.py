from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    """Represents a single pet care task."""

    description: str
    time: str
    frequency: str
    completed: bool = False
    pet_name: str = ""

    def mark_complete(self) -> None:
        """Marks the task as completed."""
        self.completed = True


@dataclass
class Pet:
    """Represents a pet and its care tasks."""

    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a task to the pet and records which pet it belongs to."""
        task.pet_name = self.name
        self.tasks.append(task)

    def remove_task(self, task_description: str) -> None:
        """Removes a task from the pet by description."""
        self.tasks = [task for task in self.tasks if task.description != task_description]

    def get_tasks(self) -> List[Task]:
        """Returns all tasks for the pet."""
        return self.tasks


@dataclass
class Owner:
    """Represents a pet owner who can manage multiple pets."""

    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Adds a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Returns all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """Retrieves and organizes tasks across an owner's pets."""

    def get_schedule(self, owner: Owner) -> List[Task]:
        """Returns all tasks sorted by time."""
        all_tasks = owner.get_all_tasks()
        return sorted(all_tasks, key=lambda task: task.time)