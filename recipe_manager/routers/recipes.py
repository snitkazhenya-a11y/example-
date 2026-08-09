from typing import List, Optional
from fastapi import APIRouter, HTTPException, status, Path, Query
from schemas import RecipeCreate, RecipeUpdate, RecipeResponse, DifficultyLevel
from database import db, id_counters

router = APIRouter(prefix="/recipes", tags=["Recipes"])


@router.get("/", response_model=List[RecipeResponse], status_code=status.HTTP_200_OK)
def get_recipes(
        limit: int = Query(10, ge=1, le=100),
        offset: int = Query(0, ge=0),
        search: Optional[str] = Query(None, description="Пошук за назвою"),
        difficulty: Optional[DifficultyLevel] = Query(None, description="Фільтрація за складністю")
):
    recipes = list(db["recipes"].values())

    if search:
        recipes = [r for r in recipes if search.lower() in r["title"].lower()]

    if difficulty:
        recipes = [r for r in recipes if r["difficulty"] == difficulty]

    return recipes[offset: offset + limit]


@router.get("/{recipe_id}", response_model=RecipeResponse, status_code=status.HTTP_200_OK)
def get_recipe_by_id(recipe_id: int = Path(..., gt=0)):
    if recipe_id not in db["recipes"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Рецепт не знайдено")
    return db["recipes"][recipe_id]


@router.post("/", response_model=RecipeResponse, status_code=status.HTTP_201_CREATED)
def create_recipe(recipe: RecipeCreate):
    if recipe.category_id not in db["categories"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Вказаної категорії не існує")

    id_counters["recipes"] += 1
    new_id = id_counters["recipes"]

    recipe_data = recipe.model_dump()
    recipe_data["id"] = new_id

    db["recipes"][new_id] = recipe_data
    return recipe_data


@router.put("/{recipe_id}", response_model=RecipeResponse, status_code=status.HTTP_200_OK)
def update_recipe_full(recipe: RecipeCreate, recipe_id: int = Path(..., gt=0)):
    if recipe_id not in db["recipes"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Рецепт не знайдено")
    if recipe.category_id not in db["categories"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Вказаної категорії не існує")

    updated_data = recipe.model_dump()
    updated_data["id"] = recipe_id
    db["recipes"][recipe_id] = updated_data
    return updated_data


@router.patch("/{recipe_id}", response_model=RecipeResponse, status_code=status.HTTP_200_OK)
def update_recipe_partial(recipe: RecipeUpdate, recipe_id: int = Path(..., gt=0)):
    if recipe_id not in db["recipes"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Рецепт не знайдено")

    stored_data = db["recipes"][recipe_id]
    update_data = recipe.model_dump(exclude_unset=True)

    if "category_id" in update_data and update_data["category_id"] not in db["categories"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Вказаної категорії не існує")

    stored_data.update(update_data)
    db["recipes"][recipe_id] = stored_data
    return stored_data


@router.delete("/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipe(recipe_id: int = Path(..., gt=0)):
    if recipe_id not in db["recipes"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Рецепт не знайдено")

    del db["recipes"][recipe_id]
    return None