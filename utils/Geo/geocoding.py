from utils.Io.argparser import args
import requests

GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/"
RESPONSE_FORMAT = "json"

def generate_params(adress : str, town : str, api_key : str) -> dict:
    adress = '+'.join(adress)
    town = '+'.join(town)
    return {
        "adress" : adress,
        "town" : town,
        "key" : api_key
    }

def get_lat_lon(adress : str, town : str) -> list:
    lat_lon = []
    try:
        api_key = args.apikey
    except :
        print("You did not provid an API key for Google geocoding API, this script will stop !")
        exit(1)
    params = generate_params(adress, town, api_key)
    url = GEOCODE_URL + RESPONSE_FORMAT
    response = requests.get(url, params=params)
    coord = response.json()
    try:
        lat_lon.append(coord['results'][0]['geometry']['location']['lat'])
        lat_lon.append(coord['results'][0]['geometry']['location']['lng'])
    except:
        lat_lon.append(0)
        lat_lon.append(0)
        print('No Coordinates')
    return lat_lon




