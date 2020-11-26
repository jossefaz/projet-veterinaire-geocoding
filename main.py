import os
import csv
from utils.regex.regex import is_ordinal, is_fax, is_tel, remove_non_digit
from utils.Geo.geocoding import get_lat_lon

RESOURCE_DIR = "resources"
OUTPUT_DIR = "output"
OUTPUT_CSV_NAME = "global.csv"


def generate_adress_list() -> list:
    address_global = []
    for filename in os.listdir(RESOURCE_DIR):
        if filename.endswith(".txt"):
            fichier = os.path.join(RESOURCE_DIR, filename)
            with open(fichier, 'r', encoding='utf-8') as address_txt_file:
                address_list_local = []
                for line in address_txt_file:
                    if line == "\n":
                        try:
                            name = ' '.join(address_list_local[1:-2])
                            telephone = address_list_local[0]
                            address = address_list_local[-2]
                            town = address_list_local[-1]
                            address_list_local = [name, telephone, address, town]
                            address_global.append(address_list_local)
                            address_list_local = []
                        except:
                            continue
                    if not is_tel(line) and not is_fax(line) and not is_ordinal(line):
                        line = line.strip("\n").strip("\\")
                        address_list_local.append(line)
                    elif is_tel(line):
                        line = remove_non_digit(line)
                        address_list_local.insert(0, line)
    return address_global


def generate_csv(address_list: list):
    out_csv_path = os.path.join(OUTPUT_DIR, OUTPUT_CSV_NAME)
    with open(out_csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nom", "Telephone", "Adresse", "ville", "lat", "lon"])
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
