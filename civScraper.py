import requests
from bs4 import BeautifulSoup

def searchCiv(civilization):
    civ_name = civilization[0].upper() + civilization[1:]
    page_result = requests.get(f"https://civilization.fandom.com/wiki/{civilization}_(Civ6)")

    print(page_result.status_code)

    if page_result.status_code == 404:
        return "Invalid civilization name."

    soup = BeautifulSoup(page_result.content, "lxml")
    ability_description = soup.find(attrs={"data-source":"ability-description"}).getText()
    unique_units = soup.find_all(attrs={"data-source":"unit"})
    unique_buidlings = soup.find_all(attrs={"data-source":"building"})

    units = ""
    buildings = ""
    print(unique_units)
    print(len(unique_units))
    for unique_unit in unique_units:
        units += unique_unit.getText()
    
    for unique_building in unique_buidlings:
        buildings += unique_building.getText()

    res = f"{civ_name} \n{units} \n{buildings}\nCiv ability: \n{ability_description}"

    res = f"```\n{res}``` \n more info: https://civilization.fandom.com/wiki/{civilization}_(Civ6)"
    return res