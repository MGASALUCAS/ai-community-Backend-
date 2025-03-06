
# Challenge App Documentation

## Overview

The Challenge app is a Django application that provides an API for managing challenges. It supports CRUD (Create, Read, Update, Delete) operations on challenge details. The app uses Django REST framework to expose the API endpoints.

### Challenge Model

The `Challenge` model contains the following fields:
- `name`: The name of the challenge.
- `host_phone`: The phone contact of the host.
- `email`: The email of the host.
- `linkedin_profile`: The LinkedIn profile URL of the host.
- `description`: A description of the challenge.
- `host_name`: The name of the host.
- `evaluation_details`: Details about the evaluation process.
- `challenge_type`: The type of challenge (paid or knowledge).
- `start_date`: The start date of the challenge.
- `close_date`: The close date of the challenge.
- `industry`: The industry of the challenge (e.g., finance, agriculture, healthcare, etc.).
- `poster_image`: An image representing the challenge.
- `prize`: The prize for the challenge (in Tz shillings or USD).

### Serializers

The `ChallengeSerializer` converts `Challenge` model instances to JSON and vice versa.

### Views

The `ChallengeViewSet` provides the API endpoints for CRUD operations on challenges.

### URLs

The URL configuration routes requests to the appropriate views.

## API Endpoints

### List Challenges

- **URL**: `/api/challenges/`
- **Method**: `GET`
- **Description**: Retrieve a list of all challenges.
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Challenge 1",
      "host_phone": "123456789",
      "email": "host@example.com",
      "linkedin_profile": "https://linkedin.com/in/host",
      "description": "Description of challenge 1",
      "host_name": "Host 1",
      "evaluation_details": "Evaluation details",
      "challenge_type": "paid",
      "start_date": "2023-01-01",
      "close_date": "2023-01-31",
      "industry": "finance",
      "poster_image": "http://example.com/media/challenge_posters/image.jpg",
      "prize": "1000 USD"
    },
    // ...other challenges...
  ]
  ```

### Retrieve a Challenge

- **URL**: `/api/challenges/{id}/`
- **Method**: `GET`
- **Description**: Retrieve details of a specific challenge.
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Challenge 1",
    "host_phone": "123456789",
    "email": "host@example.com",
    "linkedin_profile": "https://linkedin.com/in/host",
    "description": "Description of challenge 1",
    "host_name": "Host 1",
    "evaluation_details": "Evaluation details",
    "challenge_type": "paid",
    "start_date": "2023-01-01",
    "close_date": "2023-01-31",
    "industry": "finance",
    "poster_image": "http://example.com/media/challenge_posters/image.jpg",
    "prize": "1000 USD"
  }
  ```

### Create a Challenge

- **URL**: `/api/challenges/`
- **Method**: `POST`
- **Description**: Create a new challenge.
- **Request**:
  ```json
  {
    "name": "Challenge 1",
    "host_phone": "123456789",
    "email": "host@example.com",
    "linkedin_profile": "https://linkedin.com/in/host",
    "description": "Description of challenge 1",
    "host_name": "Host 1",
    "evaluation_details": "Evaluation details",
    "challenge_type": "paid",
    "start_date": "2023-01-01",
    "close_date": "2023-01-31",
    "industry": "finance",
    "poster_image": "http://example.com/media/challenge_posters/image.jpg",
    "prize": "1000 USD"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Challenge 1",
    "host_phone": "123456789",
    "email": "host@example.com",
    "linkedin_profile": "https://linkedin.com/in/host",
    "description": "Description of challenge 1",
    "host_name": "Host 1",
    "evaluation_details": "Evaluation details",
    "challenge_type": "paid",
    "start_date": "2023-01-01",
    "close_date": "2023-01-31",
    "industry": "finance",
    "poster_image": "http://example.com/media/challenge_posters/image.jpg",
    "prize": "1000 USD"
  }
  ```

### Update a Challenge

- **URL**: `/api/challenges/{id}/`
- **Method**: `PUT`
- **Description**: Update an existing challenge.
- **Request**:
  ```json
  {
    "name": "Updated Challenge",
    "host_phone": "987654321",
    "email": "newhost@example.com",
    "linkedin_profile": "https://linkedin.com/in/newhost",
    "description": "Updated description",
    "host_name": "New Host",
    "evaluation_details": "Updated evaluation details",
    "challenge_type": "knowledge",
    "start_date": "2023-02-01",
    "close_date": "2023-02-28",
    "industry": "agriculture",
    "poster_image": "http://example.com/media/challenge_posters/new_image.jpg",
    "prize": "2000 USD"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Updated Challenge",
    "host_phone": "987654321",
    "email": "newhost@example.com",
    "linkedin_profile": "https://linkedin.com/in/newhost",
    "description": "Updated description",
    "host_name": "New Host",
    "evaluation_details": "Updated evaluation details",
    "challenge_type": "knowledge",
    "start_date": "2023-02-01",
    "close_date": "2023-02-28",
    "industry": "agriculture",
    "poster_image": "http://example.com/media/challenge_posters/new_image.jpg",
    "prize": "2000 USD"
  }
  ```

### Delete a Challenge

- **URL**: `/api/challenges/{id}/`
- **Method**: `DELETE`
- **Description**: Delete a specific challenge.
- **Response**: `204 No Content`

## Conclusion

This documentation provides an overview of the Challenge app, including the model, serializers, views, and URL configurations. It also includes detailed API references for managing challenges. This should help both beginners and experienced developers understand and use the Challenge app effectively.
