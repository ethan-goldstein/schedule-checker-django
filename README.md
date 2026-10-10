# Schedule Checker (Django)

My research milestone app for CSCE 490 (team MLRT). You add the classes you plan to take, and the app saves them, checks every pair for time conflicts, totals your credits, and warns you if you go over 18.

## Built with

- Django 5.2
- SQLite (Django's default database)
- uv for package management

## Run it

```
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Then open http://127.0.0.1:8000

## How it works

- `planner/models.py`: the Course model stores the code, title, days, start and end time, credits, and location (building and room). `conflicts_with` returns true when two classes share a day and their times overlap.