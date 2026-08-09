from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class DifficultyLevel(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Назва категорії")
    description: Optional[str] = Field(None, max_length=200, description="Опис категорії")

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    description: Optional[str] = Field(None, max_length=200)

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True

class RecipeBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, description="Назва рецепту")
    ingredients: List[str] = Field(..., min_items=1, description="Список інгредієнтів")
    cooking_time_minutes: int = Field(..., gt=0, description="Час приготування у хвилинах")
    difficulty: DifficultyLevel = Field(default=DifficultyLevel.medium, description="Рівень складності")
    category_id: int = Field(..., gt=0, description="ID категорії")

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(RecipeBase):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    ingredients: Optional[List[str]] = Field(None, min_items=1)
    cooking_time_minutes: Optional[int] = Field(None, gt=0)
    difficulty: Optional[DifficultyLevel] = None
    category_id: Optional[int] = Field(None, gt=0)

class RecipeResponse(RecipeBase):
    id: int

    class Config:
        from_attributes = True