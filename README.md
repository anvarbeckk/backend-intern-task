# Chess Tournament Management System

## Overview
A Backend system to manage a chess tournament, built using Django and PostgreSQL.

## Features
- User Authentication and Authorization
- Player Management
- Tournament Management
- Match Management
- Leaderboard
- API Documentation with Swagger

## Installation

- You should have POSTGRESQL and Python3.6+

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd chess_tournament
   ```
2. Create and activate a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows 
   ```
3. Install required packages
    ```bash
    pip install -r requirements.txt
    ```
4. Configure PostgreSQL
5. Apply migrations
    ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```
6. Create superuser
   ```bash
      python manage.py createsuperuser 
   ```
7. Finally, run the server
   ```bash
      python manage.py runserver 
   ```

## API Documentation

The backend system for managing the chess tournament includes various endpoints for user management, player management, tournament management, match management, and leaderboard retrieval.

### Documentation

- **Swagger**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Redoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

### Endpoints

#### User

- `POST /api/register/`: Register a new user
- `POST /api/login/`: Login and get JWT token

#### Player

- `GET /api/players/`: List all players
- `POST /api/players/`: Create a new player
- `GET /api/players/<id>/`: Retrieve a player
- `PUT /api/players/<id>/`: Update a player
- `DELETE /api/players/<id>/`: Delete a player

#### Tournament

- `GET /api/tournaments/`: List all tournaments
- `POST /api/tournaments/`: Create a new tournament
- `GET /api/tournaments/<id>/`: Retrieve a tournament
- `PUT /api/tournaments/<id>/`: Update a tournament
- `DELETE /api/tournaments/<id>/`: Delete a tournament

#### Match

- `GET /api/matches/`: List all matches
- `POST /api/matches/`: Create a new match
- `GET /api/matches/<id>/`: Retrieve a match
- `PUT /api/matches/<id>/`: Update a match
- `DELETE /api/matches/<id>/`: Delete a match

#### Leaderboard

- `GET /api/tournaments/<tournament_id>/leaderboard/`: Get leaderboard for a tournament

![this_is_ine](https://media3.giphy.com/media/QMHoU66sBXqqLqYvGO/giphy.gif)