import requests
import os
from PIL import Image

# Dicionário dos países
paises = {
    'Itália': 'Italy',
    'Reino Unido': 'United Kingdom',
    'França': 'France',
    'Bélgica': 'Belgium',
    'Argentina': 'Argentina',
    'Irlanda': 'Ireland',
    'Tailândia': 'Thailand',
    'Suíça': 'Switzerland',
    'Mônaco': 'Monaco',
    'Estados Unidos': 'United States of America',
    'Alemanha': 'Germany',
    'Brasil': 'Brazil',
    'Espanha': 'Spain',
    'Austrália': 'Australia',
    'Uruguai': 'Uruguay',
    'Países Baixos': 'Netherlands',
    'Suécia': 'Sweden',
    'Nova Zelândia': 'New Zealand',
    'Portugal': 'Portugal',
    'Venezuela': 'Venezuela',
    'África do Sul': 'South Africa',
    'México': 'Mexico',
    'Canadá': 'Canada',
    'Áustria': 'Austria',
    'Liechtenstein': 'Liechtenstein',
    'Dinamarca': 'Denmark',
    'Finlândia': 'Finland',
    'Japão': 'Japan',
    'Chile': 'Chile',
    'Colômbia': 'Colombia',
    'República Tcheca': 'Czech Republic',
    'Malásia': 'Malaysia',
    'Hungria': 'Hungary',
    'Índia': 'India',
    'Polônia': 'Poland',
    'Rússia': 'Russia',
    'Indonésia': 'Indonesia'
}

# Países em português
lista_paises_pt = list(paises.keys())

# Países em inglês
lista_paises_eng = list(paises.values())
for i, pais in enumerate(lista_paises_eng):
    lista_paises_eng[i] = pais.lower().replace(" ", "-")

# Pasta em que serão salvas as imagens
pasta = "assets"
if not os.path.exists(pasta):
    os.mkdir(pasta)
 
# Baixando as imagens
for i, pais in enumerate(lista_paises_eng):
    url = f"https://cdn.countryflags.com/thumbs/{pais}/flag-square-500.png"
    img = requests.get(url)
    with open(os.path.join(pasta, lista_paises_pt[i] + ".png"), "wb") as f:
        f.write(img.content)

# Ajuste do tamanho das imagens
for img in os.listdir(pasta):
    f = os.path.join(pasta, img)
    load_img = Image.open(f)
    resized_img = load_img.resize((128, 128))
    resized_img.save(f)
