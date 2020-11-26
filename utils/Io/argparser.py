import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--apikey', '-ak', help="insert the API Key for Google Geocoding API", type=str)
args = parser.parse_args()