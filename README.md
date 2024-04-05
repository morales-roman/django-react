# Full Stack Notes Application with JWT Authentication

This is a full stack application for creating and managing notes. The frontend is built with React and the backend is built with Django.

## Project Structure

The project is divided into two main directories:

- `frontend/`: Contains the React application.
- `backend/`: Contains the Django application.

### Frontend

The frontend is built with React and uses Vite for a build tool. It uses Axios for making HTTP requests to the backend.

The main files and directories are:

- `src/`: Contains the source code for the React application.
- `package.json`: Contains the list of npm dependencies and scripts for the frontend.

### Backend

The backend is built with Django REST Framework and uses SQLite for a database.

The main files and directories are:

- `backend/`: Contains the main Django project files.
- `api/`: Contains the Django app for the API.
- `requirements.txt`: Contains the list of pip dependencies for the backend.

#### Authentication

This application uses JSON Web Tokens (JWT) for authentication. The JWTs are generated in the backend and sent to the frontend, where they are stored and sent with each request to authenticate the user.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository.
2. Install the dependencies for the frontend and backend.
3. Start the servers for the frontend and backend.

### Frontend

To install the dependencies and start the server for the frontend, run the following commands in the `frontend/` directory:

```sh
npm install
npm run dev
```

### Backend

To install the dependencies and start the server for the backend, first create a virtual environment and activate it. Then, run the following commands in the `backend/` directory:

```sh
pip install -r requirements.txt
python manage.py runserver
```

## Testing

This project includes unit tests to ensure the functionality of the backend application. The tests are located in the `tests.py` file inside of the `backend/api/` directory.

To run the tests, use the following command in the `backend/` directory:

```sh
python manage.py test api
```