import requests

def get_today_temperature(api_token,latitude, longitude):
    base_url = "https://api.weather.gov/"
    endpoint = f"points/{latitude},{longitude}"
    headers = {"User-Agent": "YourAppName", "token": api_token}
    #https://www.ncei.noaa.gov/cdo-web/api/v2/datatypes

    try:
        response = requests.get(base_url + endpoint, headers=headers)
        response.raise_for_status()  # Raise an error for bad requests

        #parse JSON repsonse
        data = response.json()

        #Extract the forecast endpoint from the properties
        forecast_endpoint = data["properties"]["forecast"]
        station_endpoint = data['properties']['observationStations']

        #make a new request to the forecast endpoint
        forecast_response = requests.get(forecast_endpoint, headers=headers)
        forecast_response.raise_for_status()

        station_repsonse = requests.get(station_endpoint, headers=headers)
        station_repsonse.raise_for_status()

        #parse the JSON response for the forecast
        forecast_data = forecast_response.json()
        station_data = station_repsonse.json()
        
        #extract todays temperature
        today_forecast = forecast_data["properties"]["periods"][0]
        tomorrow_forcast = forecast_data["properties"]["periods"][1]

        station_id = station_data["features"]["properties"]['']
        
        

        # Display todays temperature
        print(f"Todays temperature: {today_forecast['temperature']}{today_forecast['temperatureUnit']}")
        print(f"Tomorrows forecast: {tomorrow_forcast['temperature']}{tomorrow_forcast['temperatureUnit']}")
        print(f"Station: {station_id['stationIdentifier']}")
       
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")

# def get_observation_station(latitude, longitude):
#     points_url = f"https://api.weather.gov/points/{latitude},{longitude}"
#     response = requests.get(points_url)
#     data = response.json()

#     #Extract observationStations URL
#     observation_stations_url = data['properties']['observationStations']

#     #call observationStations endpoint
#     response = requests.get(observation_stations_url)
#     observation_stations_data = response.json()

#     #extract closest station
#     closest_station_id = observation_stations_data['features']['0']['id']
#     statioin_code = closest_station_id.split("/")[-1]

#     #append observation/latest endpoint to the station URL
#     observations_latest_url = f"{closest_station_id}/observations/latest"
#     response = requests.get(f"https://api.weather.gov/{observations_latest_url}")
#     observations_data = response.json()

#     return observations_data

    


api_token = 'yhAjVfuzPrrVWvoOtWHVkoMLCVjVarYf'
latitude = '29.424349'
longitude = '-98.491142'
get_today_temperature(api_token, latitude, longitude)
# observations = get_observation_station(latitude,longitude)
# print(observations)



    
