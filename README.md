# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## UML Diagram

```mermaid
classDiagram
    class Owner {
        +name: str
        +available_time: int
        +preferences: str
    }

    class Pet {
        +name: str
        +species: str
        +tasks: List[Task]
        +add_task(task)
        +remove_task(task_title)
        +get_tasks()
    }

    class Task {
        +title: str
        +category: str
        +duration: int
        +priority: int
        +completed: bool
        +mark_complete()
    }

    class Scheduler {
        +sort_tasks(tasks)
        +generate_daily_plan(tasks, available_time)
        +explain_plan(selected_tasks, skipped_tasks)
    }

    Owner --> Pet
    Pet --> Task
    Scheduler --> Task

## Testing PawPal+

Run the test suite with:

```bash
python -m pytest
