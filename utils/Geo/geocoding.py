from utils.Io.argparser import args
import requests

GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/"
RESPONSE_FORMAT = "json"

def generate_params(address : str, town : str, zipcode, api_key : str) -> dict:
    address = '+'.join(address.split(' '))
    town = '+'.join(town.split(' '))
    return {
        "address" : '{},{},+{}'.format(address, town,zipcode),
        "key" : api_key
    }

def get_lat_lon(adress : str, town : str, zipcode) -> list:
    lat_lon = []
    api_key = args.apikey



    if api_key is None :
        print("You did not provid an API key for Google geocoding API, this script will stop !")
        exit(1)
    params = generate_params(adress, town, zipcode, api_key)
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




