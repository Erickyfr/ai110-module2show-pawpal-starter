# PawPal+ Project Reflection

## 1. System Design

### a. Initial design

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler.

The Owner class stores basic information about the user, such as their name and available time for the day. This is important because the daily plan depends on how much time the owner has.

The Pet class represents the pet and stores information such as name, species, and a list of care tasks. Each pet has its own set of tasks that need to be completed.

The Task class represents individual care activities such as feeding, walking, medication, grooming, or enrichment. Each task includes attributes like duration and priority, which are essential for scheduling.

The Scheduler class is responsible for generating the daily plan. It sorts tasks, selects which tasks fit within the available time, and determines which tasks should be prioritized.

I designed the system this way to separate data (Owner, Pet, Task) from logic (Scheduler), which makes the code easier to understand and test.

### b. Design changes

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

I kept the design simple by using four main classes: Owner, Pet, Task, and Scheduler. One design decision I made was to separate the scheduling logic into the Scheduler class instead of placing it inside the Pet or Task classes. This helps keep responsibilities clear and makes the system easier to test and maintain.

I also ensured that Task includes important attributes like duration and priority, since these are required for generating a daily plan.

During implementation, I refined how tasks are associated with pets by adding a pet_name attribute to the Task class. This made it easier to display which pet each task belongs to when generating the schedule.

I also adjusted the Scheduler to sort tasks by time and return them in a way that makes them easier to display in both the CLI and future UI.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers time as the primary constraint by sorting tasks based on their scheduled time. Tasks are organized in chronological order to create a clear daily plan.

It also considers task completion status, allowing filtering of completed and pending tasks. Additionally, the system handles recurring tasks (daily and weekly) by automatically generating the next occurrence, and includes basic conflict detection to identify tasks scheduled at the same time.

### b. Tradeoffs

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff is that the scheduler does not prioritize tasks beyond time ordering. This means more important tasks are not treated differently from less important ones. This is reasonable for now because the goal is to create a simple and readable daily schedule before adding more complex logic.

One tradeoff my scheduler makes is that conflict detection only checks for exact matching times instead of overlapping durations. I chose this because it keeps the algorithm simple and easy to understand while still providing useful warnings for obvious scheduling issues.

---

## 3. AI Collaboration

### a. How you used AI

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI tools throughout the project to assist with design, implementation, and debugging. During the early stages, I used AI to brainstorm class structures and generate a UML diagram based on the project requirements.

In the implementation phase, I used AI to help generate class skeletons, implement methods such as sorting and filtering, and refine my Scheduler logic. AI was especially helpful when adding more advanced features like recurring task handling and conflict detection.

The most helpful prompts were specific ones, such as asking how to structure methods for sorting tasks by time, how to implement filtering logic, and how to handle recurring tasks using Python’s datetime module.

### b. Judgment and verification

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One moment where I did not accept an AI suggestion as-is was during conflict detection. The initial implementation flagged conflicts even when tasks were effectively the same or duplicated, which resulted in unnecessary warnings.

I reviewed the logic and modified it to ensure that conflicts were only reported when tasks were meaningfully different, such as different descriptions or different pets. I verified the correctness by running my main.py script with test cases that included overlapping and non-overlapping tasks to confirm that only valid conflicts were detected.

---

## 4. Testing and Verification

### a. What you tested

- What behaviors did you test?
- Why were these tests important?

I tested core behaviors of the system, including task completion, task addition, and scheduling logic. Specifically, I verified that calling mark_complete() correctly updates a task’s completion status, and that adding a task to a pet increases the number of tasks stored for that pet.

I also tested that the scheduler correctly sorts tasks by time and that filtering functions return the correct subsets of tasks. These tests were important because they confirm that the core logic of the system behaves as expected and that the scheduling output is reliable.

### b. Confidence

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am confident that my scheduler works correctly for the main use cases, including sorting tasks, filtering tasks, handling recurring tasks, and detecting basic conflicts.

If I had more time, I would test additional edge cases such as tasks with identical descriptions and times, handling invalid time formats, multiple overlapping recurring tasks, and scenarios with no tasks or pets. These tests would further improve the robustness of the system.

---

## 5. Reflection

### a. What went well

- What part of this project are you most satisfied with?

What went well in this project was the separation of system design and implementation. Starting with a UML design helped me clearly define responsibilities for each class, which made the coding process smoother.

I am also satisfied with the Scheduler class, especially the implementation of sorting, filtering, recurring task generation, and conflict detection. These features made the system more functional and closer to a real-world application.

### b. What you would improve

- If you had another iteration, what would you improve or redesign?

If I had another iteration, I would improve the scheduling logic by incorporating task priorities and time constraints more deeply, such as limiting the total time available in a day.

I would also improve the user interface to support managing multiple pets more clearly and allow editing or deleting tasks directly from the UI. Additionally, I would refine conflict detection to handle overlapping time ranges instead of only exact matches.

### c. Key takeaway

- What is one important thing you learned about designing systems or working with AI on this project?

One important thing I learned is the importance of being the “lead architect” when working with AI. While AI can generate code and ideas quickly, it is important to review, simplify, and adapt those suggestions to fit the project requirements.

I also learned that breaking the project into phases (design, implementation, testing, and UI integration) makes complex systems easier to build and understand.
