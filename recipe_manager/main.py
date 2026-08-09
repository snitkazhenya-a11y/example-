from fastapi import FastAPI
from middleware import TimingAndHeaderMiddleware
from routers import categories, recipes

app = FastAPI(
    title="Recipes Manager API",
    description="REST API для управління рецептами та категоріями",
    version="1.0.0"
)

app.add_middleware(TimingAndHeaderMiddleware)

app.include_router(categories.router)
app.include_router(recipes.router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "Вітаємо в Recipes Manager API! Перейдіть на /docs для документації."}