import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pawpal_system import Task, Pet, Owner, Scheduler


def test_mark_complete():
    """A task should be marked as completed after calling mark_complete."""
    task = Task(description="Feed breakfast", time="08:00", frequency="daily")
    task.mark_complete()
    assert task.completed is True


def test_schedule_sorted_by_time():
    """Scheduler should return tasks in time order."""
    owner = Owner(name="Alex")
    pet = Pet(name="Buddy", species="Dog")
    pet.add_task(Task(description="Evening walk", time="18:00", frequency="daily"))
    pet.add_task(Task(description="Morning walk", time="07:00", frequency="daily"))
    owner.add_pet(pet)

    schedule = Scheduler().get_schedule(owner)
    assert schedule[0].time == "07:00"
    assert schedule[1].time == "18:00"
