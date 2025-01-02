from fastapi import FastAPI, APIRouter, HTTPException
from configuretions import collection
from database.model import Todo
from database.schemes import all_data  # Updated import statement

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_todos():
    data = collection.find()
    return all_data(data)  # Use all_data instead of all_tasks

@router.post("/")
async def create_task(new_task: Todo):
    try:
        resp = collection.insert_one(dict(new_task))
        return {"status_code": 200, "id": str(resp.inserted_id)}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

app.include_router(router)
