import requests
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font
import time
import os

# API endpoint and headers
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 50,
    'page': 1,
    'sparkline': False
}

# Fetch data from CoinGecko API
def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return []

# Analyze data
def analyze_data(data):
    top_5 = sorted(data, key=lambda x: x['market_cap'], reverse=True)[:5]
    avg_price = sum(item['current_price'] for item in data) / len(data)
    highest_change = max(data, key=lambda x: x['price_change_percentage_24h'])
    lowest_change = min(data, key=lambda x: x['price_change_percentage_24h'])
    
    return {
        "top_5": top_5,
        "avg_price": avg_price,
        "highest_change": highest_change,
        "lowest_change": lowest_change
    }

# Update Excel sheet
def update_excel(data, analysis):
    # Create workbook
    file_path = "crypto_data.xlsx"
    wb = Workbook()
    ws = wb.active
    ws.title = "Crypto Data"

    # Header
    headers = ["Name", "Symbol", "Current Price (USD)", "Market Cap", "24h Volume", "24h % Change"]
    ws.append(headers)
    for col in ws[1]:
        col.font = Font(bold=True)

    # Data rows
    for item in data:
        ws.append([
            item['name'],
            item['symbol'],
            item['current_price'],
            item['market_cap'],
            item['total_volume'],
            item['price_change_percentage_24h']
        ])

    # Analysis Section
    ws.append([])
    ws.append(["Top 5 by Market Cap"])
    for coin in analysis["top_5"]:
        ws.append([coin['name'], coin['symbol'], coin['market_cap']])

    ws.append([])
    ws.append(["Average Price", analysis["avg_price"]])
    ws.append(["Highest Change", analysis["highest_change"]['name'], analysis["highest_change"]['price_change_percentage_24h']])
    ws.append(["Lowest Change", analysis["lowest_change"]['name'], analysis["lowest_change"]['price_change_percentage_24h']])

    wb.save(file_path)
    print(f"Excel updated at {file_path}")

# Main function to automate fetching and updating
def main():
    while True:
        data = fetch_crypto_data()
        if data:
            analysis = analyze_data(data)
            update_excel(data, analysis)
        time.sleep(300)  # Wait 5 minutes before updating again

if __name__ == "__main__":
    main()
