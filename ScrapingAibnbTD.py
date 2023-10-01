# pip  install python-dotenv
from time import sleep
from selenium import webdriver # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager


from mongodb import MongoConnection

db_client = MongoConnection().client
db = db_client.get_database('airbnb')
col = db.get_collection('lugares')

print(col)
opt = Options()
opt.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opt
)

driver.get('https://www.airbnb.com/')

sleep(3)

titulos_anuncios = driver.find_elements(By.XPATH, '//div[@data-testid="listing-card-title"]')
for titulo in titulos_anuncios:
    document = {
        "titulo": titulo.text
    }
    col.insert_one(document=document)

    print(titulo.text)