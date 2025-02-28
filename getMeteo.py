from cat.mad_hatter.decorators import tool
import requests

@tool(examples=['Che tempo fa a Roma,it?', 'Meteo a Roma,it?', 'Meteo di New Tourk,us?'])
def getWeather(location, cat)-> dict:
    """
    Retrieve real time weather information about the requested city from the user.
    The input is always the location of the city and is formatted as a string.
    An input example to pass to the function a parameter is: "Roma,it" or "New York,us".
    """
    
    url="https://api.openweathermap.org/data/2.5/weather"
    payload = {
        "q": location,
        "units": "metric",
        "lang": "it",
        "appid": "8ca86f8c2555dd834acea58d05ca01c3"
    }
    r = requests.get(url, params=payload)
    output = r.json()
    info = {
        "Meteo": output['weather'][0]['description'],
        "Temperatura percepita": f"{output['main']['feels_like']} °C",
        "Umidità": f"{output['main']['humidity']}%",
        "Vento": f"{output['wind']['speed']} nodi"
    }

    exact_response = f"Il tempo a {payload['q']} è {info['Meteo']}. La temperatura percepita è di {info['Temperatura percepita']} con il {info['Umidità']} di umidità"

    return exact_response