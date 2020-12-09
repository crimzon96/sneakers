import os
import json
import csv
import re
import string
import random

def tsb_to_csv(profile_json_file, account_json_file):
    """Transfer The Shit bot profiles to a csv file"""
    with open(profile_json_file) as p_json_file:
        profile_json = json.load(p_json_file)
    with open(account_json_file) as a_json_file:
        account_json = json.load(a_json_file)
    with open('profiles.csv', 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Header
        header = [
            "PROFILENAME",
            "FIRSTNAME",
            "LASTNAME",
            "EMAIL",
            "STREET",
            "HOUSENUMBER",
            "ADRESS2",
            "POSTALCODE",
            "CITY",
            "STATE",
            "COUNTRY",
            "PHONE",
            "CARDTYPE",
            "CREDITCARD_NUMBER",
            "CREDITCARD_EXPMONTH",
            "CREDITCARD_EXPYEAR",
            "CREDITCARD_CVV",
            "43einhalbCountryID",
            "allikeStateID",
            "awLabStateID",
            "bstnCountryID",
            "consortiumStateID",
            "consortiumStateName",
            "footshopCountryID",
            "grosbasketStateID",
            "overkillStateID",
            "prodirectCountryID",
            "prodirectStateID",
            "shinzoCountryID",
            "slamJamState",
            "slamJamStateID",
            "sneakAvenueCountryID",
            "titoloStateID"
        ]
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        for profile, account in zip(profile_json, account_json):
            character_list =  list(string.ascii_lowercase)
            random_char_1 = random.choice(character_list)
            random_char_2 = random.choice(character_list)
            random_char_3 = random.choice(character_list)
            try:
                cc_expire = profile.get("cc").get('ccExpiry')
                writer.writerow(
                    {
                        'PROFILENAME' : profile.get("cc").get('profileName'),
                        'FIRSTNAME': profile.get("cc").get('profileName'),
                        "LASTNAME": profile.get("cc").get('lastName'),
                        "EMAIL": account.get("account").get("username"),
                        "STREET":"herman heijermanshove",
                        "HOUSENUMBER": "50",
                        "ADRESS2": random_char_1 + random_char_2 + random_char_3,
                        "POSTALCODE": "3438HD",
                        "CITY": "Nieuwegein",
                        "STATE": "",
                        "COUNTRY": "NL",
                        "PHONE": account.get("user").get("contact").get("sms").get("verifiedNumber"),
                        "CARDTYPE": "Visa",
                        "CREDITCARD_NUMBER": profile.get("cc").get('ccNumber'),
                        "CREDITCARD_EXPMONTH": re.match("^\d{2}", cc_expire).group(),
                        "CREDITCARD_EXPYEAR": re.compile(r'(\d+)$').search(cc_expire).group(),
                        "CREDITCARD_CVV": profile.get("cc").get('ccCvc'),
                        "43einhalbCountryID": "",
                        "allikeStateID": "",
                        "awLabStateID": "",
                        "bstnCountryID": "",
                        "consortiumStateID": "",
                        "consortiumStateName": "",
                        "footshopCountryID": "",
                        "grosbasketStateID": "",
                        "overkillStateID": "",
                        "prodirectCountryID": "",
                        "prodirectStateID": "",
                        "shinzoCountryID": "",
                        "slamJamState": "",
                        "slamJamStateID": "",
                        "sneakAvenueCountryID": "",
                        "titoloStateID": ""
                    }
                )
            except Exception as e:
                print(e)
                print(profile)
                # for debugging
                import pdb; pdb.set_trace()
                pass
tsb_to_csv("tsb-profiles-dec.json", "tsb-accounts-dec.json")
