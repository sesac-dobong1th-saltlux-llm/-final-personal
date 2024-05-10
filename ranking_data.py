import requests

import csv

def get_ranking_data(offset, limit, api_key):
    url = f"https://api.neople.co.kr/cy/ranking/ratingpoint"
    params = {
        "offset": offset,
        "limit": limit,
        "apikey": api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for any HTTP errors
        
        # If the request was successful, return JSON data
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None



offset = 0

limit = 10

api_key = "BXVbXvZz67zzWlrt9PX0RvYdZZUQAEAh"

ranking_data = get_ranking_data(offset, limit, api_key)
if ranking_data:
    print(ranking_data)  # Do something with the data
else:
    print("Failed to retrieve data.")




def save_to_csv(data, filename):
    # CSV 파일로 데이터 저장
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data['rows'][0].keys())
        writer.writeheader()
        for row in data['rows']:
            writer.writerow(row)

filename = 'ranking_data.csv'

data = ranking_data

save_to_csv(data, filename)