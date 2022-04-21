import requests
from bs4 import BeautifulSoup

def searchCiv(civilization):
    civ_name = civilization[0].upper() + civilization[1:]
    res = civ_name
    page_result = requests.get(f"https://civilization.fandom.com/wiki/{civilization}_(Civ6)")
    print(page_result.status_code)
    soup = BeautifulSoup(page_result.content, "lxml")
    ability_descrpition = soup.find(attrs={"data-source":"ability-description"}).getText()
    res = civ_name + ability_descrpition
    return res