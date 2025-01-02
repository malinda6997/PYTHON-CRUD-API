# FastAPI Todo CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application built using **FastAPI** and **MongoDB**. The application provides APIs to manage a Todo list.

## Features

- **Create** a new task
- **Read** all tasks
- **Update** an existing task
- **Delete** a task (soft delete)

## Prerequisites

- Python 3.10+
- MongoDB database
- FastAPI
- Pydantic
- pymongo
- bson
- python-dotenv

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install the required dependencies:

   ```bash
   pip install fastapi pymongo uvicorn pydantic python-dotenv
   ```

3. Configure your MongoDB URI in the `.env` file:

   ```bash
   echo "MONGO_URI=mongodb+srv://<username>:<password>@crud-api.jqorm.mongodb.net/?retryWrites=true&w=majority&appName=CRUD-API" > .env
   ```

   Replace `<username>` and `<password>` with your MongoDB credentials.

4. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### 1. Get All Todos

- **URL**: `/`
- **Method**: GET
- **Description**: Retrieves all non-deleted tasks.

### 2. Create a New Todo

- **URL**: `/`
- **Method**: POST
- **Body**:
  ```json
  {
      "title": "Task title",
      "description": "Task description",
      "is_done": false
  }
  ```

### 3. Update a Todo

- **URL**: `/{task_id}`
- **Method**: PUT
- **Body**:
  ```json
  {
      "title": "Updated title",
      "description": "Updated description",
      "is_done": true
  }
  ```

### 4. Delete a Todo

- **URL**: `/{task_id}`
- **Method**: DELETE
- **Description**: Soft deletes a task by setting `is_deleted` to `true`.

## Postman Collection

To test the API endpoints, import the `postman_collection.json` file into Postman. This collection includes pre-configured requests for all available endpoints.

## Notes

- The MongoDB connection is configured using the `MongoClient` in `configuretions.py`.
- The `schemes.py` file handles the serialization of MongoDB documents into API responses.

## License

This project is licensed under the MIT License.
