import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8d4637c4dec4a8abda8bcdc8a0be4bc0'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '47180'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'
    
    
@pytest.mark.parametrize('key, velue', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '1308988')])
def test_parametrize(key, velue):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == velue