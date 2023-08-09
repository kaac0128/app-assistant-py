import platform
import os
import psutil
import time
import requests
import geocoder
import os

OPENWEATHER_APIKEY = os.getenv("OPENWEATHER_APIKEY")

def info_system():
    memoria = psutil.virtual_memory()
    almacenamiento = psutil.disk_usage('/')
    conexion = psutil.net_connections()
    data = {
        "so": "Sistema operativo:" + platform.system(),
        "versionSo": "Versión del sistema operativo:" + platform.release(),
        "arquitecturaSo": "Arquitectura del sistema:" + platform.machine(),
        "procesador": "Información del procesador:" + os.popen("cat /proc/cpuinfo | grep 'model name' | uniq").read().strip(),
        "nucleos": "Número de núcleos:" + str(os.cpu_count()),
        "ramTotal": "Memoria RAM total:" + str(memoria.total),
        "ramDisponible": "Memoria RAM disponible:" + str(memoria.available),
        "ramUtilizada":"Memoria RAM utilizada:" + str(memoria.used),
        "pid":"PID:"+ str(conexion[0].pid),
        "laddr":"LADDR:"+str(conexion[0].laddr),
        "raddr":"RADDR:"+ str(conexion[0].raddr),
        "estado":"Estado:"+ conexion[0].status,
        "almacenamientoTotal":"Almacenamiento total:"+ str(almacenamiento.total),
        "almacenamientoUtilizado":"Almacenamiento utilizado:"+ str(almacenamiento.used),
        "almacenamientoLibre":"Almacenamiento libre:"+ str(almacenamiento.free)
    }
    return data

def get_hour():
    hora_actual = time.localtime()
    hora_legible = time.strftime("%I:%M %p", hora_actual)
    return "La hora actual es " + hora_legible

def get_wheater():
    g = geocoder.ip('me')
    ciudad = g.city
    pais = g.country
    url_base = 'http://api.openweathermap.org/data/2.5/weather?'
    url = f'{url_base}q={ciudad},{pais}&appid={OPENWEATHER_APIKEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        datos_clima = response.json()
        temperatura_actual = datos_clima['main']['temp']
        descripcion_clima = datos_clima['weather'][0]['description']
        humedad_actual = datos_clima['main']['humidity']
        return f'El pronóstico del clima en {ciudad}, {pais} es {descripcion_clima} su temperatura es de {temperatura_actual} °C y la humedad es de {humedad_actual}'
    else:
        return 'Error al obtener el pronóstico del clima.'