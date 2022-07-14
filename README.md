# una-coding-task
Una Health Backend Tech Challenge

1. Install `poetry` with pip - `pip install poetry`
2. Run `poetry install` from root folder
3. Run `poetry run python manage.py migrate`
4. Run `poetry run python manage.py runserver`
5. Visit `http://127.0.0.1:8000/api/v1/levels/` to see the `list` endpoint.
6. It's possible to filter by user_id, start and stop dates in the format used by the recording devices (mm-dd-yyyy hh:mm).
