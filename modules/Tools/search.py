import requests
import wikipediaapi
import pywhatkit as kit
from googlesearch import search

def search_wikipedia(query):
    wiki_wiki = wikipediaapi.Wikipedia('es')  
    page = wiki_wiki.page(query)
    if not page.exists():
        return "No se encontró la página en Wikipedia."
    return page.summary

def search_google(consulta):
    resultados = []
    for resultado in search(consulta, stop=10):
        resultados.append(resultado)
    return resultados

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return "El numero de ip es " + ip_address["ip"]

def play_youtube(consulta):
    kit.playonyt(consulta)
    return f"Reproduciendo {consulta}"
