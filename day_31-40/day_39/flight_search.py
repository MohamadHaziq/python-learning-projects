import requests
from flight_data import FlightData
import json

with open("./day_31-40/day_39/creds.json") as f:
    creds = json.load(f)

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = creds['api_key']

class FlightSearch:
    def get_destination_code(self,city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        headers = {
            "apikey" : TEQUILA_API_KEY
        }

        query = {
            "term" : city_name,
            "location_types" : 'city',
        }

        response = requests.get(url = location_endpoint, headers = headers, params = query)
        results = response.json()['locations']
        city_code = results[0]['code']

        return city_code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apikey" : TEQUILA_API_KEY
            }

        query = {
            "fly_from" : origin_city_code,
            "fly_to" : destination_city_code,
            "date_from" : from_time.strftime("%d/%m/%Y"),
            "date_to" : to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from" : 7,
            "nights_in_dst_to" : 28,
            "flight_type" : "round",
            "one_for_city" : 1,
            "max_stopovers" : 0,
            "curr" : "GBP"
        }

        response = requests.get(
            url = f"{TEQUILA_ENDPOINT}/v2/search",
            headers = headers,
            params = query
        )

        data = response.json()["data"][0]
        print(data)

        flight_data = FlightData(
            price = data['price'],
            origin_city = data['route'][0]['cityFrom'],
            origin_airport = data['route'][0]['flyFrom'],
            destination_city = data['route'][0]['cityTo'],
            destination_airport = data['route'][0]['flyTo'],
            out_date = data['route'][0]['local_departure'].split("T")[0],
            return_date = data['route'][1]['local_departure'].split("T")[0],
        )

        with open('./day_31-40/day_39/dump.json', 'w') as f:
            json.dump(response.json(), f)

        return flight_data