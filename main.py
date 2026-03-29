from pawpal_system import Task, Pet, Owner, Scheduler

# Create owner
owner = Owner(name="Alex")

# Create pets
dog = Pet(name="Buddy", species="Dog")
cat = Pet(name="Luna", species="Cat")

# Add tasks out of order on purpose
dog.add_task(Task(description="Evening walk", time="18:00", frequency="daily"))
dog.add_task(Task(description="Morning walk", time="07:00", frequency="daily"))
cat.add_task(Task(description="Feed dinner", time="17:00", frequency="daily"))
cat.add_task(Task(description="Feed breakfast", time="08:00", frequency="daily"))
dog.add_task(Task(description="Breakfast", time="08:00", frequency="daily"))
cat.add_task(Task(description="Clean litter box", time="12:00", frequency="daily"))

# Mark one task complete
cat.tasks[0].mark_complete()

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create scheduler
scheduler = Scheduler()

# Print sorted schedule
print("=== Today's Pet Care Schedule ===")
schedule = scheduler.get_schedule(owner)
for task in schedule:
    status = "Done" if task.completed else "Pending"
    print(f"[{task.time}] {task.pet_name}: {task.description} ({task.frequency}) - {status}")

print("\n=== Pending Tasks Only ===")
pending_tasks = scheduler.filter_by_status(schedule, completed=False)
for task in pending_tasks:
    print(f"[{task.time}] {task.pet_name}: {task.description}")

print("\n=== Luna's Tasks ===")
luna_tasks = scheduler.filter_by_pet(owner, "Luna")
luna_tasks = scheduler.sort_by_time(luna_tasks)
for task in luna_tasks:
    print(f"[{task.time}] {task.pet_name}: {task.description}")
    
print("\n=== Marking Morning Walk Complete ===")
task_to_complete = dog.tasks[1]  # Morning walk
new_task = scheduler.mark_task_complete(owner, task_to_complete)

print(f"Completed: {task_to_complete.description} on {task_to_complete.due_date}")

if new_task:
    print(
        f"New recurring task created: {new_task.description} on {new_task.due_date} at {new_task.time}"
    )
else:
    print("No recurring task created.")

print("\n=== Buddy's Updated Tasks ===")
buddy_tasks = scheduler.filter_by_pet(owner, "Buddy")
buddy_tasks = scheduler.sort_by_time(buddy_tasks)
for task in buddy_tasks:
    status = "Done" if task.completed else "Pending"
    print(f"[{task.time}] {task.pet_name}: {task.description} - {status} ({task.due_date})")
    
print("\n=== Conflict Warnings ===")
updated_schedule = scheduler.get_schedule(owner)
conflicts = scheduler.detect_conflicts(updated_schedule)

if conflicts:
    for warning in conflicts:
        print(warning)
else:
    print("No conflicts detected.")