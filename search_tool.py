import requests
import os

def search_Agent(query) -> str:
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    
    response = requests.get(url)
    data = response.json()
    
    return data["AbstractText"] if data["AbstractText"] else "No result found."