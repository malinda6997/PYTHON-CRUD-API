from fastapi import FastAPI, APIRouter, HTTPException
from configuretions import collection
from database.model import Todo
from database.schemes import all_data  # Updated import statement
from bson import ObjectId
from datetime import datetime

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_todos():
    data = collection.find({"is_deleted": False})
    return all_data(data)  # Use all_data instead of all_tasks

@router.post("/")
async def create_task(new_task: Todo):
    try:
        resp = collection.insert_one(dict(new_task))
        return {"status_code": 200, "id": str(resp.inserted_id)}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
    
@router.put("/{task_id}")
async def update_task(task_id: str, updated_task: Todo):
    try:
        id = ObjectId(task_id)
        exesting_doc = collection.find_one({"_id":id ,"is_deleted":False})
        if not exesting_doc:
             return HTTPException(status_code=404, detail=f"Internal Server Error: {e}")
        updated_task.updated_at = datetime.timestamp(datetime.now())
        resp = collection.update_one({"_id": id}, {"$set": dict(updated_task)})
        return {"status_code": 200, "message": "Task updated successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
    
@router.delete("/{task_id}")
async def delete_task(task_id: str):
    try:
        id = ObjectId(task_id)
        exesting_doc = collection.find_one({"_id":id ,"is_deleted":False})
        if not exesting_doc:
             return HTTPException(status_code=404, detail=f"Internal Server Error: {e}")
        resp = collection.update_one({"_id": id}, {"$set": {"is_deleted": True}})
        return {"status_code": 200, "message": "Task deleted successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
        
        

app.include_router(router)
