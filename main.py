import requests
import datetime

def main():
token = "g6bBlqpabgHFrqll48wq0ZcREq7zoq6x"
url = "https://calendarific.com/api/v2/holidays"
params = {
    "api_key": token, 
    "country": "RU",
    "year": 2025
}

response = requests.get(url, params=params)
response.raise_for_status()
holidays = response.json()["response"]["holidays"]


for holiday in holidays:
    date = holiday["date"]["iso"]
    slit_date = date.split("-")
    date_only = date.split("T")[0]
    true_date = datetime.datetime.strptime(date_only, "%Y-%m-%d")
    formatted_date = true_date.strftime("%d %B")
    print(f"""название праздника: {holiday["name"]}
    дата: {formatted_date}
    описание: {holiday["description"]}\n""")
if __name__ == "__main__":
    main()
   









