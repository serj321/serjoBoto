import requests
from bs4 import BeautifulSoup

def searchCiv(civilization):
    page_result = requests.get(f"https://civilization.fandom.com/wiki/{civilization}_(Civ6)")
    print("in searchCiv")
    print(page_result.status_code)
    soup = BeautifulSoup(page_result.content, "lxml")
    ability_descrpition = soup.find(attrs={"data-source":"ability-description"}).getText()
    print(ability_descrpition)