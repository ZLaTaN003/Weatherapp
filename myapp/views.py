from django.shortcuts import render
import requests
import datetime
# Create your views here.




def index(request):
    cw2 = None

    api_key = ""
    current_weather = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    

    if request.method == "POST":
        city1 = request.POST["city1"]
        city2 = request.POST.get("city2",None)
    
        cw1 = findweather(city1,api_key,current_weather)
    
    
        if city2:
           
         
           cw2 = findweather(city2,api_key,current_weather)
        
            
    
        else:
           cw2,fw2 = None,None
        return render(request,"myapp/index.html",{
          "weatherdata1" :cw1,
        
          "weatherdata2" : cw2,
    
     })
    


    else:

     return render(request,"myapp/index.html")
    

#function
import requests

def findweather(city, apikey, current_weather):
    try:
        response = requests.get(current_weather.format(city, apikey))
        response.raise_for_status()
        weather_data = response.json()

        
        if weather_data.get("cod") == "404":
        
            error_message = f"City '{city}' not found."
            return {"error": error_message}

        temp = round(weather_data["main"]["temp"] - 273.15, 2)
        desc = weather_data["weather"][0]["description"]
        icon = weather_data["weather"][0]["icon"]

        weatherdata = {
            "city": city,
            "temp": temp,
            "desc": desc,
            "icon": icon,
        }

        return weatherdata

    except requests.exceptions.RequestException as e:
    
        print(f"Error during request: {e}")
        return None
    except KeyError as e:
        
        print(f"KeyError: {e}")
        return None

