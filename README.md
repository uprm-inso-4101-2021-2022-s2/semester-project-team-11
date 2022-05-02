# HomeService App by team-11 #

## Project Structure ##
- Backend: 
    - Django Rest Framework (/DRF/)
- Frontend:
    - React.js (/REACT/)
- Important:
    - Start Django server before React
### Django: (Open terminal in /DRF/) ###
- First Set Up:
    - py -m venv venv
    - Set-ExecutionPolicy Unrestricted -Scope Process
    - venv\Scripts\activate
    - pip install django
    - pip install djangorestframework
    - pip install djangorestframework-simplejwt
    - pip install django-cors-headers
    - pip install coverage                                
    - py manage.py makemigrations                         
    - py manage.py migrate
    - py manage.py createsuperuser                        
    - py manage.py runserver                       

- Testing:
    - coverage run --omit='\*/venv/*' manage.py test
    - coverage html
    - Postman app as a tool to see the api

- Shutting Down:
    - CTRL + C         
    - deactivate                                       

- Starting Up After Shut Down
    - Set-ExecutionPolicy Unrestricted -Scope Process
    - venv\Scripts\activate
    - py manage.py runserver

- After making model changes or large modifications
    - py manage.py makemigrations    
    - py manage.py migrate

### React: (Open terminal in /REACT/) ###
- First Set Up:
    - Download and Install Node.js
    - cd homeserviceapi
    - npm install
    - npm start

- Shutting Down:
    - CTRL + C
    - Y

- Starting Up After Shut Down:
    - npm start