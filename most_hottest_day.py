import pprint
import requests
from datetime import datetime, timedelta

current_date = datetime.now()
week_beginning = current_date + timedelta(days=(7 - (current_date.weekday() + 1)))
week_end = week_beginning + timedelta(days=6)

request_url = 'https://api.open-meteo.com/v1/forecast?' \
              'latitude=13.754&' \
              'longitude=100.5014&' \
              'daily=apparent_temperature_max&' \
              'timezone=Asia%2FBangkok&' \
              f"start_date={week_beginning.strftime('%Y-%m-%d')}&" \
              f"end_date={week_end.strftime('%Y-%m-%d')}"

response = requests.get(request_url).json()
response_daily = response['daily']

temperatures = response_daily['apparent_temperature_max']
max_temperature = temperatures[0]
max_index = 0
for i in range(len(temperatures)):
    temperature = temperatures[i]
    if temperature > max_temperature:
        max_temperature = temperature
        max_index = i

hottest_day = datetime.fromisoformat(response_daily['time'][max_index])
print("Hottest day on next week:", hottest_day.strftime('%A'))
print("Temperature:", max_temperature)

