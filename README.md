# covid-19-vaccination

# Project Description
A python/Django COVID-19 vaccination registry project to efficiently manage people vaccinated againts covid-19. The system was developed using python3 and django 3.17.  
All CRUD operations i.e - Create a person, Read all vaccinated persons, Update a vaccinated person's details, Delete a vaccinated person and Search for a vaccinated person using multiple parameters has been implemented.

## Installation $ setup 
- Run: git clone https://github.com/abdimoha-dev/covid-19-vaccination.git
- (Igore if using local development) -> To set up production server, create .env file in the project root directory for setting up database credentals and copy .envExample to provide guidance. Uncomment DB setting if you are using POSTGRESQL.  
- Run: cd covid-19-vaccination
- Run: pip3 install -r requirements.txt  # To install all project dependencies  
- Run: python3 manage.py makemigrations 
- Run: python3 manage.py migrate  

#### create superuser
Run: python3 manage.py createsuperuser  

#### Run Unittesting 
- python3 manage.py test vaccination_registry/

Run: python3 manage.py runserver  
## Accessing the system
- open http://127.0.0.1:8000/vaccination/login on your browser  
NB: As we are simulating a real life scenario, users cannot create their own account. They can contact their system admin for their account.  
- For testing purposes, login using the credentials displayed on the login page .ie Username: test  password: test123  
- Congratulation!! you have successfully deployed the system and you are ready.

## Test server
- The system prototype is available at: http://104.131.23.233/vaccination/login

## Accessing the APIs
Swagger API domentation provides a great way for interacting with the APIs
### visit http://127.0.0.1:8000/api/

### POSTMAN COLLECTION - A postman collection is available at the root folder as Covid19 vaccination_postman_collection.json
