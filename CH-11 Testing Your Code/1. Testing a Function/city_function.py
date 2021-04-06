# city_functions.py

# def get_location_info(city, country):
#     """Return a single string like City, Country."""
#     return f'{city.title()}, {country.title()}' 


# city_function.py (updated)

# def get_location_info(city, country, population):
#     """Return a single string like City, Country - population xxxx."""
#     return f'{city.title()}, {country.title()} - population {population}'



# city_function.py (updated)
# Make population parameter optional

def get_location_info(city, country, population = ''):
    """Return a single string like City, Country - population xxxx."""
    if population:
        return f'{city.title()}, {country.title()} - population {population}'
    else:
        return f'{city.title()}, {country.title()}'