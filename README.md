# Weather App

Weather App is a Django-based web application that provides current weather information for a given location.

## Features

- Retrieve current weather information for a specific location.
- Display temperature and weather description for the requested location.
- Error handling for invalid location inputs and server errors.
- Logging of request and response information.

## Installation

1. Clone the repository to your local machine:

   
         git clone https://github.com/your-username/weatherapp.git
   
2. Navigate to the project directory:
  
         cd weatherapp
    
 3.Create a virtual environment:
 
         python -m venv env
      
 4.Activate the virtual environment:
 
    
         env\Scripts\activate
  
 5.Install the required dependencies:
 
    
         pip install -r requirements.txt
      
 6.Run database migrations:
 
   
         python manage.py migrate
      
 7. Start the development server:
    
    
         python manage.py runserver
 
   # Error Handling
The API handles the following error cases:

   400 Bad Request: If the required location parameter is missing or invalid.<br>
      404 Not Found: If the requested location is not found.<br>
         500 Internal Server Error: If there is an error retrieving the weather data from the provider.<br>
            The API returns appropriate HTTP status codes and error messages in the response to indicate the error to the client.

   # Logging
The application logs important details about each request and response, including the request method, endpoint, request parameters, response status, and any relevant error messages.<br> The logs are stored in the log file specified in the settings.py configuration file.

