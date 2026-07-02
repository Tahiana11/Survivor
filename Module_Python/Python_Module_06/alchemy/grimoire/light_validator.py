def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    is_valid = any(item.lower() in ingredients_lower for item in allowed)

    keyword = "VALID" if is_valid else "INVALID"
    return f"{keyword}"
