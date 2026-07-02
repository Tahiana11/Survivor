from alchemy.grimoire import light_spellbook


if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record light spell:", end=" ")
    res = light_spellbook.light_spell_record("Fantasy", "Earth, wind and fire")
    print(f"{res}")
