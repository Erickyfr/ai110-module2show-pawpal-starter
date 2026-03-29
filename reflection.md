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

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

### b. Tradeoffs

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

### a. How you used AI

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

### b. Judgment and verification

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

### a. What you tested

- What behaviors did you test?
- Why were these tests important?

### b. Confidence

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

### a. What went well

- What part of this project are you most satisfied with?

### b. What you would improve

- If you had another iteration, what would you improve or redesign?

### c. Key takeaway

- What is one important thing you learned about designing systems or working with AI on this project?
