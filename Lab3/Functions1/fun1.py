def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces


grams_required = 200
result = grams_to_ounces(grams_required)
print(f"{grams_required} grams is equal to {result:.2f} ounces.")
