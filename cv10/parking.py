import json
from json.decoder import JSONDecodeError

class Zona():
    def __init__(self, data):
        self.objectid = data["properties"]["OBJECTID"]
        self.category = data["properties"]["CATEGORY"]
        self.tariftext = data["properties"]["TARIFTEXT"]
        self.code = data["properties"]["CODE"]

    @classmethod
    def from_geojsonZ(cls, filename):
        try:
            zona_dict = {}
            zona_list = []
            with open(filename, encoding="utf-8") as soubor:
                z_json = json.load(soubor)
            for feature in z_json["features"]:
                #cls je tady totožné jako Zona - tohle je lepší, kdyby se to někdo potom rozhodl přejmenovat; proto pak funguje init
                z = cls(feature)

                #ukládám ke klíči (code) ten celý objekt (jednu celou feature)
                zona_dict[feature["properties"]["CODE"]] = z
                zona_list.append(z)
            return zona_dict

        except FileNotFoundError:
            print("Vstupní soubor se nepodařilo načíst. Ujistěte se, že daný soubor existuje, případně zda je k němu zadána korektní cesta.")
            quit()
        except PermissionError:
            print("Program nemá přístup k zápisu výstupních souborů.")
            quit()
        except JSONDecodeError:
            print("Načtený vstupní soubor není platný JSON.")
            quit()

class Usek():
    def __init__(self, data, zona_dictionary):
        self.objectid = data["properties"]["OBJECTID"]
        self.zps_id = data["properties"]["ZPS_ID"]
        self.typ_zony = data["properties"]["TYPZONY"]
        self.ps_zps = data["properties"]["PS_ZPS"]

        #chci mu říct, ať sem uloží hodnotu, která odpovídá tarif kódu ze slovníku
        self.zona : Zona = zona_dictionary.get(data["properties"]["TARIFTAB"])

    @classmethod
    def from_geojsonU(cls, filename, zona_dictionary):
        try:
            usek_list = []
            with open(filename, encoding="utf-8") as soubor:
                u_json = json.load(soubor)
            for feature in u_json["features"]:
                u = cls(feature, zona_dictionary)
                usek_list.append(u)
            return usek_list

        except FileNotFoundError:
            print("Vstupní soubor se nepodařilo načíst. Ujistěte se, že daný soubor existuje, případně zda je k němu zadána korektní cesta.")
            quit()
        except PermissionError:
            print("Program nemá přístup k zápisu výstupních souborů.")
            quit()
        except JSONDecodeError:
            print("Načtený vstupní soubor není platný JSON.")
            quit()

zony = "DOP_ZPS_ZonyStani_p.json"
Zona.from_geojsonZ(zony)
zona_dict =Zona.from_geojsonZ(zony)

useky = "DOP_ZPS_USEKY_p.json"
Usek.from_geojsonU(useky, zona_dict)