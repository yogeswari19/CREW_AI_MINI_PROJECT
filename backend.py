from fastapi import FastAPI, BackgroundTasks
from crew_blog import generate_blog
from fastapi.middleware.cors import CORSMiddleware
import uuid
from fastapi.responses import FileResponse
import re


app = FastAPI(title="AI Blog Writer API")
tasks_storage={}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    # return {"message":"Welcome to AI Blog Writer API"}
    return FileResponse("frontend.html")

@app.post("/create-blog")
def create_blog(topic:str,background_tasks:BackgroundTasks):
    task_id=str(uuid.uuid4())
    tasks_storage[task_id]={"status":"processing","content":None,"error":None}
    background_tasks.add_task(run_crew,task_id,topic)

    return {
        "task_id":task_id,
        "status":"processing",
        "message":f"Blog generation started"
    }

@app.get("/blog-status/{task_id}")
def get_status(task_id: str):
    if task_id not in tasks_storage:
        return {"error":"Task not found"}
    return tasks_storage[task_id]

def run_crew(task_id:str,topic:str):
    try:
        result=generate_blog(topic)
        content=str(result)

        content=re.sub(r'^```(?:html)?\s*\n','',content,flags=re.MULTILINE)
        content=re.sub(r'\n```\s*$','',content,flags=re.MULTILINE)
        content=content.lstrip()
        content=content.rstrip()

        tasks_storage[task_id]["status"]="completed"
        tasks_storage[task_id]["content"]=content
    except Exception as e:
        tasks_storage[task_id]["status"]="failed"
        tasks_storage[task_id]["error"]=str(e)
