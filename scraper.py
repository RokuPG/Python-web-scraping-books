import requests as rq
import csv
from bs4 import BeautifulSoup as bf

def traer_datos():
    lista_libros = []
    page1 = "https://books.toscrape.com/"
    respuesta = rq.get(url=page1)
    respuesta.encoding = 'utf-8'
    contenido = respuesta.text
    soup = bf(contenido, 'html.parser')
    libros = soup.find_all('article', class_='product_pod')
    
    for libro in libros:
        titulo = libro.h3.a['title']
        precio = libro.find('p', class_='price_color').text
        lista_libros.append({"titulo": titulo, "precio": precio})
    
    return lista_libros

page1 = "https://books.toscrape.com/"
respuesta = rq.get(url=page1)
respuesta.encoding = 'utf-8'
contenido = respuesta.text
soup = bf(contenido, 'html.parser')
libros = soup.find_all('article', class_="product_pod")

with open('libros.csv', mode='w', encoding='utf-8', newline='') as f:

    writer = csv.writer(f)
    writer.writerow(['Título', 'Precio'])

    for libro in libros:
        titulo = libro.h3.a['title']
        precio = libro.find('p', class_='price_color').text
        writer.writerow([titulo, precio])
        print(f"Guardando: {titulo}")