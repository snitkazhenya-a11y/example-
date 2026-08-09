from typing import Dict, Any
db: Dict[str, Dict[int, Any]] = {
    "categories": {
        1: {"id": 1, "name": "Десерти", "description": "Солодкі страви"},
        2: {"id": 2, "name": "Перші страви", "description": "Супи, борщі, бульйони"}
    },
    "recipes": {
        1: {"id": 1,
            "title": "Борщ український",
            "ingredients": ["Буряк", "Капуста", "Картопля", "М'ясо"],
            "cooking_time_minutes": 120,
            "difficulty": "hard",
            "category_id": 2
            }
    }
}

id_counters = {
    "categories": 2,
    "recipes": 1
}