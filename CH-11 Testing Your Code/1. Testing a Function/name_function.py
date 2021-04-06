# get formatted name using first and last name as required arguments

# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {last}"
#     return full_name.title()


# A new version of get_formatted_name() that requires a middle name argument

# def get_formatted_name(first, middle, last):
#     """Generate a neatly formatted full name."""
#     full_name = f"{first} {middle} {last}"
#     return full_name.title()


# A new version of get_formatted_name() that has an optional middle name argument

def get_formatted_name(first, last, middle = ''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()