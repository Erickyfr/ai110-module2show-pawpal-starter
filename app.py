import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.caption("A simple pet care schedule planner.")

# --- Owner & Pet Setup ---
st.subheader("Owner & Pet Info")
col1, col2, col3 = st.columns(3)
with col1:
    owner_name = st.text_input("Owner name", value="Jordan")
with col2:
    pet_name = st.text_input("Pet name", value="Mochi")
with col3:
    species = st.selectbox("Species", ["Dog", "Cat", "Other"])

st.divider()

# --- Add Tasks ---
st.subheader("Add Tasks")
col1, col2, col3 = st.columns(3)
with col1:
    task_desc = st.text_input("Task description", value="Morning walk")
with col2:
    task_time = st.text_input("Time (HH:MM)", value="08:00")
with col3:
    task_freq = st.selectbox("Frequency", ["daily", "weekly", "as needed"])

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if st.button("Add Task"):
    st.session_state.tasks.append(
        {"description": task_desc, "time": task_time, "frequency": task_freq}
    )
    st.success(f"Added: {task_desc} at {task_time}")

if st.session_state.tasks:
    st.write("Tasks added so far:")
    st.table(st.session_state.tasks)

    if st.button("Clear all tasks"):
        st.session_state.tasks = []
        st.rerun()
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# --- Generate Schedule ---
st.subheader("Today's Schedule")

if st.button("Generate Schedule"):
    if not st.session_state.tasks:
        st.warning("Add at least one task before generating a schedule.")
    else:
        # Build objects from session state
        pet = Pet(name=pet_name, species=species)
        for t in st.session_state.tasks:
            pet.add_task(Task(description=t["description"], time=t["time"], frequency=t["frequency"]))

        owner = Owner(name=owner_name)
        owner.add_pet(pet)

        schedule = Scheduler().get_schedule(owner)

        st.success(f"Schedule for {owner_name} — {pet_name} the {species}")
        for task in schedule:
            status = "✅" if task.completed else "🔲"
            st.markdown(f"{status} **{task.time}** — {task.description} *({task.frequency})*")
