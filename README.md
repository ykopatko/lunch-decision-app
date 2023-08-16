# Lunch-decision-app #

This service provides an efficient way for a company's employees to vote on their preferred restaurant menus for lunch. Restaurants can easily update their daily menus via the API, allowing employees to view and select their preferred choices through a mobile app. The backend is tailored to support both the latest and previous versions of the app, seamlessly addressing the needs of users who haven't yet updated.

## Setup and Installation ##

To run the Lunch Decision App, follow the instructions below:

## Prerequisites ##

- Docker and Docker Compose need to be installed on your machine.

## Clone the repository to your local machine: ##

   ```
   git clone https://github.com/ykopatko/lunch-decision-app.git
   ```

## Navigate to the project's root directory: ##

   ```
   cd lunch-decision-app
   ```

## Rename a `.env.sample` file to `.env` in the project's root directory and provide the following environment variables: ##

   ```
   POSTGRES_HOST=db
   POSTGRES_DB=your_database_name
   POSTGRES_USER=your_database_user
   POSTGRES_PASSWORD=your_database_password
   DJANGO_SECRET_KEY=your_django_secret_key
   ```

   Replace the values with your own database and Django secret key configurations.


## Build and run the Docker containers 🐳: ##

   ```shell
   docker-compose build
   docker-compose up
   ```

##  Create a superuser account: ##

   ```shell
   docker exec -it ********* python manage.py createsuperuser {********* - id your container}
   ```

## The Lunch App should now be running on `http://localhost:8000`. ##

Domain:
*  localhost:8000
*  create new user - api/users/register/
*  get JWT Token - api/users/token/

## Documentation
Try the app and check the available endpoints via SWAGGER documentation
- `/api/doc/swagger/`

Additional info via the next url
- `/api/doc/redoc/`

## API Endpoints

The Lunch App provides the following API endpoints:

# Restaurants

- `GET /api/lunch_app/restaurants/` - Retrieve a list of all restaurants.
- `POST /api/lunch_app/restaurants/` - Create a new restaurant.
- `GET /api/lunch_app/restaurants/{id}/` - Retrieve details of a specific restaurant.
- `PUT /api/lunch_app/restaurants/{id}/` - Update a specific restaurant.
- `PATCH /api/lunch_app/restaurants/{id}/` - Partial update  of the specific restaurant.
- `DELETE /api/lunch_app/restaurants/{id}/` - Delete a specific restaurant.

# Menus

- `GET /api/lunch_app/menus/` - Retrieve a list of all menus.
- `POST /api/lunch_app/menus/` - Create a new menu.
- `GET /api/lunch_app/menus/{id}/` - Retrieve details of a specific menu.
- `PUT /api/lunch_app/menus/{id}/` - Update a specific menu.
- `PATCH /api/lunch_app/menus/{id}/` - Partial update of the specific menu.
- `DELETE /api/lunch_app/menus/{id}/` - Delete a specific menu.
- `GET /api/lunch_app/menus/results/` - Retrieve the voting results for top chosen menus.
- `GET /api/lunch_app/menus/today/` - Retrieve today's menu based on the highest number of votes.
- `POST /api/lunch_app/votes/` - Vote for a specific menu.

# User

- `POST /api/users/register/` - Register a new user.
- `POST /api/users/token/` - Obtain a JWT token.
- `POST /api/users/token/refresh/` - Refresh a JWT token.
- `POST /api/users/token/verify/` - Verify a JWT token.
- `GET /api/users/me/` - Retrieve the authenticated user's details.
- `PUT /api/users/me/` - Update the authenticated user's details.
- `PATCH /api/users/me/` - Partial update the authenticated user's details.

# Authentication

The Lunch App uses JSON Web Tokens (JWT) for authentication. To access protected endpoints, include the JWT token in the `Authorization` header of the request using the format: `Bearer <token>`. Tokens can be obtained by authenticating with valid user credentials.