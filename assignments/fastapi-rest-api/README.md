# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build an in-memory REST API for managing school clubs. Practice defining FastAPI routes, validating request data with Pydantic models, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️	Read and Create Clubs

#### Description
Complete the API routes that list all clubs, retrieve one club by ID, and add a new club. Run the application with `uvicorn starter-code:app --reload` and test each route in the interactive documentation at `/docs`.

#### Requirements
Completed program should:

- Return all clubs from `GET /clubs`
- Return the matching club from `GET /clubs/{club_id}`, or a `404` response when the ID does not exist
- Validate and add a club from `POST /clubs`, returning a `201` status code


### 🛠️	Update Existing Clubs

#### Description
Add a route that replaces the editable information for an existing club using validated request data.

#### Requirements
Completed program should:

- Accept `PUT` requests at `/clubs/{club_id}`
- Preserve the club ID from the URL while updating the club's name, description, and member count
- Return the updated club, or a `404` response when the ID does not exist


### 🛠️	Delete Clubs

#### Description
Add a route that removes an existing club from the in-memory collection.

#### Requirements
Completed program should:

- Accept `DELETE` requests at `/clubs/{club_id}`
- Remove the matching club and return a `204` status code with no response body
- Return a `404` response when the ID does not exist