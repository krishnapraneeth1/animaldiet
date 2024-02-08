from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/weather")
async def get_weather(city: str):
    api_key = "380c6671b2f95f164d1d658f7cd14b54"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for HTTP status code errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": f"Error accessing the weather API: {str(e)}"}
    
    print(response.status_code)
    

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "City not found"}
