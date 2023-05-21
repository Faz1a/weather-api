# Weather App

Weather App is a Django-based web application that provides current weather information for a given location.

## Features

- Retrieve current weather information for a specific location.
- Display temperature and weather description for the requested location.
- Error handling for invalid location inputs and server errors.
- Logging of request and response information.

## Installation

1. Clone the repository to your local machine:

   `shell
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
 
#API Endpoints

GET /current-weather

Retrieve the current weather information for a specific location.

Parameters:

location (required): The name of the location.
