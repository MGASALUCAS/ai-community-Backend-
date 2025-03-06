
# Events API Documentation

## Overview
The `events` app provides a RESTful API for managing events. The API supports CRUD operations (Create, Read, Update, Delete) for events, allowing users to interact with the events data via HTTP requests.

## Event Model
The `Event` model contains the following fields:
- `title`: The title of the event (string, max length 255).
- `image`: An image associated with the event (image file).
- `description`: A detailed description of the event (text).
- `link`: A URL link to the event (URL).
- `category`: The category of the event (choices: webinar, conference, workshop).
- `event_host`: The host of the event (string, max length 255).
- `location`: The location of the event (string, max length 255).
- `date_time`: The date and time of the event (datetime).

## API Endpoints
The following endpoints are available for interacting with the events API:

### List Events
- **URL**: `/api/events/`
- **Method**: GET
- **Description**: Retrieve a list of all events.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "title": "Sample Event",
            "image": "http://example.com/media/events/sample.jpg",
            "description": "This is a sample event.",
            "link": "http://example.com",
            "category": "webinar",
            "event_host": "John Doe",
            "location": "Online",
            "date_time": "2023-10-01T10:00:00Z"
        },
        // ...more events
    ]
    ```

### Retrieve Event
- **URL**: `/api/events/{id}/`
- **Method**: GET
- **Description**: Retrieve details of a specific event by ID.
- **Response**:
    ```json
    {
        "id": 1,
        "title": "Sample Event",
        "image": "http://example.com/media/events/sample.jpg",
        "description": "This is a sample event.",
        "link": "http://example.com",
        "category": "webinar",
        "event_host": "John Doe",
        "location": "Online",
        "date_time": "2023-10-01T10:00:00Z"
    }
    ```

### Create Event
- **URL**: `/api/events/`
- **Method**: POST
- **Description**: Create a new event.
- **Request**:
    ```json
    {
        "title": "New Event",
        "image": "http://example.com/media/events/new.jpg",
        "description": "This is a new event.",
        "link": "http://example.com",
        "category": "conference",
        "event_host": "Jane Smith",
        "location": "New York",
        "date_time": "2023-11-01T15:00:00Z"
    }
    ```
- **Response**:
    ```json
    {
        "id": 2,
        "title": "New Event",
        "image": "http://example.com/media/events/new.jpg",
        "description": "This is a new event.",
        "link": "http://example.com",
        "category": "conference",
        "event_host": "Jane Smith",
        "location": "New York",
        "date_time": "2023-11-01T15:00:00Z"
    }
    ```

### Update Event
- **URL**: `/api/events/{id}/`
- **Method**: PUT
- **Description**: Update an existing event by ID.
- **Request**:
    ```json
    {
        "title": "Updated Event",
        "image": "http://example.com/media/events/updated.jpg",
        "description": "This is an updated event.",
        "link": "http://example.com",
        "category": "workshop",
        "event_host": "Alice Johnson",
        "location": "San Francisco",
        "date_time": "2023-12-01T18:00:00Z"
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "title": "Updated Event",
        "image": "http://example.com/media/events/updated.jpg",
        "description": "This is an updated event.",
        "link": "http://example.com",
        "category": "workshop",
        "event_host": "Alice Johnson",
        "location": "San Francisco",
        "date_time": "2023-12-01T18:00:00Z"
    }
    ```

### Delete Event
- **URL**: `/api/events/{id}/`
- **Method**: DELETE
- **Description**: Delete an event by ID.
- **Response**: 
    ```json
    {
        "detail": "Event deleted successfully."
    }
    ```

## Sample Data
Here is an example of the JSON structure for an event:
```json
{
    "title": "Sample Event",
    "image": "http://example.com/media/events/sample.jpg",
    "description": "This is a sample event.",
    "link": "http://example.com",
    "category": "webinar",
    "event_host": "John Doe",
    "location": "Online",
    "date_time": "2023-10-01T10:00:00Z"
}
```

## Interaction
To interact with the API, you can use tools like Postman or curl. Below are examples of how to perform each operation using curl:

### List Events
```sh
curl -X GET http://localhost:8000/api/events/
```

### Retrieve Event
```sh
curl -X GET http://localhost:8000/api/events/1/
```

### Create Event
```sh
curl -X POST http://localhost:8000/api/events/ \
    -H "Content-Type: application/json" \
    -d '{
        "title": "New Event",
        "image": "http://example.com/media/events/new.jpg",
        "description": "This is a new event.",
        "link": "http://example.com",
        "category": "conference",
        "event_host": "Jane Smith",
        "location": "New York",
        "date_time": "2023-11-01T15:00:00Z"
    }'
```

### Update Event
```sh
curl -X PUT http://localhost:8000/api/events/1/ \
    -H "Content-Type: application/json" \
    -d '{
        "title": "Updated Event",
        "image": "http://example.com/media/events/updated.jpg",
        "description": "This is an updated event.",
        "link": "http://example.com",
        "category": "workshop",
        "event_host": "Alice Johnson",
        "location": "San Francisco",
        "date_time": "2023-12-01T18:00:00Z"
    }'
```

### Delete Event
```sh
curl -X DELETE http://localhost:8000/api/events/1/
```

This documentation provides a comprehensive guide to using the `events` API, including the model structure, API endpoints, sample data, and interaction examples.
