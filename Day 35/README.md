python - cheatsheat
DAY 35 - API KEYs, Authentication, Environmental variable and send SMS
What is API Authentication and Why Do We Need to Authenticate Ourselves
API authentication is the process of verifying the identity of a user or application attempting to access an API, typically through the use of credentials (such as API keys, tokens, or username/password combinations) to ensure secure and authorized access to the API's functionality and data.

An API key is a unique alphanumeric code or token issued by an API provider to authenticate and authorize access to their services and resources.

Using API Keys to Authenticate and Get the Weather from OpenWeatherMap
        
            import requests

            API_key= "7481580853971b6038e3450027157893",
            parameters = {
            "lat":8.980603,
            "lon":38.757759,
            "cnt":7,
            "appid":API_key,
            "exclude":"current,minutly,daily"
            
            }
            
            
            response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameters)
            response.raise_for_status()
            
            weather_data = response.json()["hourly"][:12]
            
            will_rain = False
            for hourly_data in weather_data:
                condition_code = hourly_data["weather"][0]["id"]
            
                if int(condition_code) > 700:
                    will_rain = True
            
            
            if will_rain:
                print("will, rain")
                
Challenge - Check if it Will Rain in the Next 12 Hours
