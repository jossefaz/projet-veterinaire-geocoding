import os
import csv
from utils.regex.regex import is_ordinal, is_fax, is_tel, remove_non_digit
from utils.Geo.geocoding import get_lat_lon

RESOURCE_DIR = "resources"
OUTPUT_DIR = "output"
OUTPUT_CSV_NAME = "global.csv"

def generate_name(name_string:str)-> list:
    name = name_string.split(" ")
    if len(name) == 1:
        name.append('')
    return name

def generate_town(town_string:str)->list:
    town = town_string.split(" ")
    if len(town) == 1:
        town.append('')
    return town

def generate_adress_list() -> list:
    address_global = []
    for filename in os.listdir(RESOURCE_DIR):
        if filename.endswith(".txt"):
            fichier = os.path.join(RESOURCE_DIR, filename)
            with open(fichier, 'r', encoding='utf-8') as address_txt_file:
                address_list_local = []
                phones = [None,None]
                for line in address_txt_file:
                    if line == "\n":
                        try:
                            nom, prenom = generate_name(address_list_local[0])
                            clinique = ' '.join(address_list_local[1:-2])
                            telephone = address_list_local[0]
                            address = address_list_local[-2]
                            zipcode, town_name = generate_town(address_list_local[-1])
                            address_list_local = [nom,prenom,clinique, *phones, address, town_name, zipcode]
                            address_global.append(address_list_local)
                            address_list_local = []
                        except:
                            continue
                    if not is_tel(line) and not is_fax(line) and not is_ordinal(line):
                        line = line.strip("\n").strip("\\")
                        address_list_local.append(line)
                    elif is_tel(line):
                        line = remove_non_digit(line)
                        if(phones[0] is None):
                            phones[0] = line
                        elif(phones[1] is None) :
                            phones[1] = line

    return address_global


def generate_csv(address_list: list):
    out_csv_path = os.path.join(OUTPUT_DIR, OUTPUT_CSV_NAME)
    with open(out_csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nom", "Prenom", "nom_clinique", "Telephone_1", "Telephone_1", "Adresse", "ville", "code_postal","lat", "lon"])
        count = 0
        total = len(address_list)
        for line in address_list:
            lat, lon = get_lat_lon(line[2], line[3])
            line.append(lat)
            line.append(lon)
            writer.writerow(line)
            count +=1
            print("{} / {} adresses".format(count, total))


def main():
    address_list = generate_adress_list()
    generate_csv(address_list)


if __name__ == '__main__':
    main()
