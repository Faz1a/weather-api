import requests
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def current_weather(request):
    location = request.GET.get('location')
    logger.info(f'Request received for current weather. Location: {location}')

    api_key = '93f3ce70575c93f5ec939b281cb3ad23'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        response_data = {
            'location': location,
            'temperature': temperature,
            'description': description,
        }

        logger.info('Weather data successfully retrieved.')
        return JsonResponse(response_data)
    elif response.status_code == 404:
        error_message = 'Location not found.'
        logger.error(f'Error retrieving weather data: {error_message}')
        return JsonResponse({'error': error_message}, status=404)
    else:
        error_message = 'Error retrieving weather data.'
        logger.error(f'Error retrieving weather data: {error_message}')
        return JsonResponse({'error': error_message}, status=response.status_code)
    
