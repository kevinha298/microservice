# microservice
A microservice API with  JSON Web Tokens (jwt) authentication using docker with django and postgresql containers.

1) Open git bash from local repository directory

2) Clone project from remote git to local repositorydirectory:
git clone https://github.com/kevinha298/microservice.git

3) Open project in vs code:
code .

4) Open first terminal session in vs code to build container image:
docker-compose up

5) Once the image is built from the session above, open second terminal session in vs code to migrate Django models to Postgresql database:
docker-compose run app python manage.py makemigrations
docker-compose run app python manage.py migrate

6) On the second terminal session in vs code, stop the containers and rebuild image containers:
docker-compose down
docker-compose build

7) On the first terminal session in vs code, start the containers:
docker-compose up

8) Test django default site:
http://127.0.0.1:8000/admin/

9) On the second terminal session for the following instructions (get into the app service of the django_app container to create a super user).
docker-compose exec app sh

10) Once inside the app service of the django_app container, create a super user and enter username, email address, and password.
python manage.py createsuperuser
username: admin
password: app123


11) Use Postman to test different endpoints.

    api endpoints:
    GET: http://127.0.0.1:8000/api/member/
    POST: http://127.0.0.1:8000/api/member/
    PUT: http://127.0.0.1:8000/api/member/3/
    DELETE: http://127.0.0.1:8000/api/member/3/

    {
    "mrn": 228,
    "name": "John Doe",
    "dob": "1968-01-28"
    }

    tokens endpoints:
    http://127.0.0.1:8000/api/token/
    http://127.0.0.1:8000/api/token/refresh/


12) Use the Client.py app within the project to test different api calls with different endpoints.


