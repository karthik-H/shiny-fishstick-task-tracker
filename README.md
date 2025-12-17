
# Task API

This is a simple task management API built with FastAPI and SQLAlchemy.

## Setup

1.  Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

2.  Run the application:

    ```
    uvicorn task_api.main:app --reload
    ```

## API Endpoints

The API will be available at `http://127.0.0.1:8000`.

*   `POST /tasks/`: Create a new task.
*   `GET /tasks/`: Get a list of tasks.
*   `GET /tasks/{task_id}`: Get a specific task.
*   `PUT /tasks/{task_id}`: Update a task.
*   `DELETE /tasks/{task_id}`: Delete a task. 
    Delete should check if the user exist if not return error.

