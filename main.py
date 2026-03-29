from pawpal_system import Task, Pet, Owner, Scheduler

# Create owner
owner = Owner(name="Alex")

# Create pets
dog = Pet(name="Buddy", species="Dog")
cat = Pet(name="Luna", species="Cat")

# Add tasks to Buddy
dog.add_task(Task(description="Morning walk", time="07:00", frequency="daily"))
dog.add_task(Task(description="Evening walk", time="18:00", frequency="daily"))

# Add tasks to Luna
cat.add_task(Task(description="Feed breakfast", time="08:00", frequency="daily"))
cat.add_task(Task(description="Clean litter box", time="12:00", frequency="daily"))
cat.add_task(Task(description="Feed dinner", time="17:00", frequency="daily"))

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Generate and print schedule
scheduler = Scheduler()
schedule = scheduler.get_schedule(owner)

print("=== Today's Pet Care Schedule ===")
for task in schedule:
    status = "Done" if task.completed else "Pending"
    print(f"[{task.time}] {task.pet_name}: {task.description} ({task.frequency}) - {status}")
