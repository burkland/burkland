# Standard library imports
import re
import string

# Third party imports
from bs4 import BeautifulSoup
import requests

# Base URL for tgsc
tgsc_url = "http://www.thegoodscentscompany.com/"

# Iterate through each letter to get fragrance ingredients
for letter in string.ascii_lowercase:
    # Logic for handling one-off letter combos
    if letter in ["j", "w"]:
        continue
    elif letter in ["k", "x"]:
        letter = chr(ord(letter) - 1) + letter

    # Build URL
    url = tgsc_url + f"fragonly-{letter}.html"

    # Fetch the URL
    response = requests.request("GET", url)

    # Create the soup object
    materials_soup = BeautifulSoup(response.text, "html.parser")

    # For each of the materials we find the name, link, and use
    for material in materials_soup.find_all("tr"):

        # Get text as array (should just be two sets)
        material_descriptions = material.text.split("\n")

        # Check wether it is a link to a material
        valid_material = material.find("a") is not None

        # Skip the rest of the logic if no link
        if not valid_material:
            continue

        # Use regex to find the URL (contained within single quotes of onclick attribute)
        material_link = re.findall(r"'([^']+)'", material.find("a").get("onclick"))[0]

        # Fetch the individual material link
        response = requests.request("GET", material_link)

        # Create the soup object
        material_soup = BeautifulSoup(response.text, "html.parser")

        # Get the formulas link if it is exists
        formulas_link = material_soup.find('a', text="Fragrance Demo Formulas")

        # Get the link if not none
        if formulas_link is not None:
            formulas_link = formulas_link.get("href")

        print(
            f"""
            Descriptors: {material_descriptions}
            Material Link: {material_link}
            Formulas Link: {formulas_link}
            ============================
            """
        )