"""
  Exemplo de multiprocessamento com base na live:
  https://www.youtube.com/watch?v=9HNlmjcOj6s

  Primeira etapa do problema.

  Fazer o download dos 100 primeiros pokemons da pokeapi

  Sincrono levou 2m e 40s
"""
from contextlib import contextmanager
from datetime import datetime
from os import makedirs
from os.path import exists
from pprint import pprint
from shutil import rmtree, copyfileobj
from urllib.parse import urljoin
from requests import get

path = 'downloads'
base_url = 'http://pokeapi.co/api/v2/'

start_time = datetime.now()

if exists(path):
    rmtree(path)
makedirs(path)


def get_sprite_url(url, sprite='front_default'):
    return get(url).json()['sprites'][sprite]

def download_file(name, url, *, path=path, type_='png'):
    """ Faz o download de um arquivo """
    response = get(url, stream=True)
    fname = f'{path}/{name}.{type_}'
    with open(fname, 'wb') as f:
        copyfileobj(response.raw, f)
    return fname

pokemons = get(urljoin(base_url, 'pokemon/?limit=100')).json()['results']

images_url = {j['name']: get_sprite_url(j['url']) for j in pokemons}

files = [download_file(name, url) for name, url in images_url.items()]

time_elapsed = datetime.now() - start_time

print(f'Tempo Total (hh:mm:ss.ms): {time_elapsed}')

pprint(files)
