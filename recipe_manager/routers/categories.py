from typing import List, Optional
from fastapi import APIRouter, HTTPException, status, Path, Query, Header
from schemas import CategoryCreate, CategoryUpdate, CategoryResponse
from database import db, id_counters

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=List[CategoryResponse], status_code=status.HTTP_200_OK)
def get_categories(
        limit: int = Query(10, ge=1, le=100, description="Пагінація: кількість елементів"),
        offset: int = Query(0, ge=0, description="Пагінація: зсув"),
        x_api_key: Optional[str] = Header(None, alias="X-API-Key", description="Кастомний заголовок")
):
    categories = list(db["categories"].values())
    return categories[offset: offset + limit]


@router.get("/{category_id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def get_category_by_id(category_id: int = Path(..., gt=0, description="ID категорії")):
    if category_id not in db["categories"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Категорію не знайдено")
    return db["categories"][category_id]


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate):
    id_counters["categories"] += 1
    new_id = id_counters["categories"]

    category_data = category.model_dump()
    category_data["id"] = new_id

    db["categories"][new_id] = category_data
    return category_data


@router.put("/{category_id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def update_category_full(
        category: CategoryCreate,
        category_id: int = Path(..., gt=0)
):
    if category_id not in db["categories"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Категорію не знайдено")

    updated_data = category.model_dump()
    updated_data["id"] = category_id
    db["categories"][category_id] = updated_data
    return updated_data


@router.patch("/{category_id}", response_model=CategoryResponse, status_code=status.HTTP_200_OK)
def update_category_partial(
        category: CategoryUpdate,
        category_id: int = Path(..., gt=0)
):
    if category_id not in db["categories"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Категорію не знайдено")

    stored_data = db["categories"][category_id]
    update_data = category.model_dump(exclude_unset=True)

    stored_data.update(update_data)
    db["categories"][category_id] = stored_data
    return stored_data


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int = Path(..., gt=0)):
    if category_id not in db["categories"]:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Категорію не знайдено")

    del db["categories"][category_id]
    return None