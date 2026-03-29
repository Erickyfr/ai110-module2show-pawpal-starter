import sys
import os
from datetime import date, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pawpal_system import Task, Pet, Owner, Scheduler


def test_mark_complete():
    """A task should be marked as completed after calling mark_complete."""
    task = Task(description="Feed breakfast", time="08:00", frequency="daily")
    task.mark_complete()
    assert task.completed is True


def test_schedule_sorted_by_time():
    """Scheduler should return tasks in chronological order."""
    owner = Owner(name="Alex")
    pet = Pet(name="Buddy", species="Dog")
    pet.add_task(Task(description="Evening walk", time="18:00", frequency="daily"))
    pet.add_task(Task(description="Morning walk", time="07:00", frequency="daily"))
    owner.add_pet(pet)

    schedule = Scheduler().get_schedule(owner)

    assert schedule[0].time == "07:00"
    assert schedule[1].time == "18:00"


def test_recurring_task_creates_next_day_task():
    """Completing a daily task should create a new task for the next day."""
    owner = Owner(name="Alex")
    pet = Pet(name="Buddy", species="Dog")
    task = Task(
        description="Morning walk",
        time="07:00",
        frequency="daily",
        due_date=date.today(),
    )

    pet.add_task(task)
    owner.add_pet(pet)

    scheduler = Scheduler()
    new_task = scheduler.mark_task_complete(owner, task)

    assert task.completed is True
    assert new_task is not None
    assert new_task.description == "Morning walk"
    assert new_task.due_date == date.today() + timedelta(days=1)
    assert new_task.completed is False


def test_conflict_detection_flags_same_time_tasks():
    """Scheduler should detect conflicts when two tasks share the same time."""
    owner = Owner(name="Alex")
    dog = Pet(name="Buddy", species="Dog")
    cat = Pet(name="Luna", species="Cat")

    dog.add_task(Task(description="Breakfast", time="08:00", frequency="daily"))
    cat.add_task(Task(description="Feed breakfast", time="08:00", frequency="daily"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler()
    schedule = scheduler.get_schedule(owner)
    conflicts = scheduler.detect_conflicts(schedule)

    assert len(conflicts) == 1
    assert "08:00" in conflicts[0]


def test_filter_by_status_returns_only_pending_tasks():
    """Scheduler should return only tasks matching the requested completion status."""
    owner = Owner(name="Alex")
    pet = Pet(name="Buddy", species="Dog")

    task1 = Task(description="Morning walk", time="07:00", frequency="daily")
    task2 = Task(description="Evening walk", time="18:00", frequency="daily")
    task2.mark_complete()

    pet.add_task(task1)
    pet.add_task(task2)
    owner.add_pet(pet)

    scheduler = Scheduler()
    schedule = scheduler.get_schedule(owner)
    pending_tasks = scheduler.filter_by_status(schedule, completed=False)

    assert len(pending_tasks) == 1
    assert pending_tasks[0].description == "Morning walk"