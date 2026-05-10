from fastapi import FastAPI
from fastapi import Response

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Making an api connection...Hello World!"}

@app.get("/csv")
def csv():
    csv_content = "app_name,description,type\nBusiness Card Swap,An app to swap career specific business cards between devices,application"
    return Response(content=csv_content, media_type="text/plain")