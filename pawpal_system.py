from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date, timedelta

@dataclass
class Task:
    """Represents a single pet care task."""

    description: str
    time: str
    frequency: str
    due_date: date = field(default_factory=date.today)
    completed: bool = False
    pet_name: str = ""

    def mark_complete(self) -> None:
        """Marks the task as completed."""
        self.completed = True

    def create_next_recurring_task(self) -> Optional["Task"]:
        """Creates the next recurring task if the task repeats daily or weekly."""
        if self.frequency.lower() == "daily":
            next_date = self.due_date + timedelta(days=1)
        elif self.frequency.lower() == "weekly":
            next_date = self.due_date + timedelta(days=7)
        else:
            return None

        return Task(
            description=self.description,
            time=self.time,
            frequency=self.frequency,
            due_date=next_date,
            completed=False,
            pet_name=self.pet_name
        )


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

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Returns tasks sorted by time."""
        return sorted(tasks, key=lambda task: task.time)

    def filter_by_status(self, tasks: List[Task], completed: bool) -> List[Task]:
        """Returns tasks filtered by completion status."""
        return [task for task in tasks if task.completed == completed]

    def filter_by_pet(self, owner: Owner, pet_name: str) -> List[Task]:
        """Returns tasks for a specific pet."""
        filtered_tasks = []
        for pet in owner.pets:
            if pet.name.lower() == pet_name.lower():
                filtered_tasks.extend(pet.get_tasks())
        return filtered_tasks

    def get_schedule(self, owner: Owner) -> List[Task]:
        """Returns all tasks sorted by time."""
        all_tasks = owner.get_all_tasks()
        return self.sort_by_time(all_tasks)

    def mark_task_complete(self, owner: Owner, task_to_complete: Task) -> Optional[Task]:
        """Marks a task complete and creates the next recurring task if needed."""
        task_to_complete.mark_complete()
        next_task = task_to_complete.create_next_recurring_task()

        if next_task:
            for pet in owner.pets:
                if pet.name == task_to_complete.pet_name:
                    pet.add_task(next_task)
                    return next_task

        return None

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Returns warning messages for tasks scheduled at the same time."""
        conflicts = []
        seen_times: dict[str, List[Task]] = {}

        for task in tasks:
            if task.time not in seen_times:
                seen_times[task.time] = [task]
            else:
                for existing_task in seen_times[task.time]:
                    if (
                        task.description != existing_task.description
                        or task.pet_name != existing_task.pet_name
                    ):
                        conflicts.append(
                            f"Conflict at {task.time}: '{existing_task.description}' ({existing_task.pet_name})"
                            f" and '{task.description}' ({task.pet_name})"
                        )
                seen_times[task.time].append(task)

        return conflicts