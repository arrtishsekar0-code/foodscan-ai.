from fastapi import FastAPI
from routers import meals

app = FastAPI(title="FoodScan AI Backend")

app.include_router(meals.router)

@app.get("/")
async def root():
    return {"message": "Welcome to FoodScan AI Backend"}