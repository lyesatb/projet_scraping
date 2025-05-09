import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://www.autoscout24.fr/lst?page={}"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

NUM_PAGES = 50  # Ajuste ce nombre selon le nombre réel de pages disponibles

def scrape_page(page_number):
    url = BASE_URL.format(page_number)
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article', {'data-testid': 'list-item'})
    data = []

    for art in articles:
        marque = art.get('data-make', '').capitalize()
        modele = art.get('data-model', '')
        annee = art.get('data-first-registration', '')
        km = art.get('data-mileage', '')
        energie = art.get('data-fuel-type', '')
        code_postal = art.get('data-listing-zip-code', '')
        departement = code_postal[:2] if len(code_postal) >= 2 else ''
        prix = art.get('data-price', '')  # Ajout du prix

        boite = ''
        details = art.find_all('span', {'class': 'VehicleDetailTable_item__4n35N'})
        for d in details:
            if 'boîte' in d.get('aria-label', '').lower():
                boite = d.text.strip()
        
        data.append([marque, modele, annee, boite, km, energie, code_postal, departement, prix])
    
    return data

# Écriture dans le fichier CSV
with open('voitures.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Marque', 'Modèle', 'Année', 'Boîte', 'KM', 'Énergie', 'Code Postal', 'Département', 'Prix'])

    for page in range(1, NUM_PAGES + 1):
        print(f"Scraping page {page}...")
        try:
            records = scrape_page(page)
            writer.writerows(records)
            time.sleep(2)
        except Exception as e:
            print(f"Erreur à la page {page} : {e}")
