#  The Casting Agency General Introduction
The Casting Agency application is a RESTful Transactional API to perform CRUD operations with RBAC completed by karam sawalha.
```
My Project API is hosted at: [ThisLink](https://karamcapstoneproject.onrender.com)

AUTH0 LOGIN URL to get JWT at: [ThisLink](https://dev-karamsawalha.us.auth0.com/authorize?audience=karamcapstone&response_type=token&client_id=6el7BJBoNh04IO1XBLkrpoRjuYUrB0hC&redirect_uri=https://sample/callback)

```
---
## Database Models & Table Design:

1.  Movies
    - id
    - title 
    - release date
2.  Actors
    - id
    - name
    - age
    - gender
---
## Role Based Access Control:
1. Casting Assistant
    - 'view:actors' 
    - 'view:movies'

2. Casting Director
    - 'view:actors' 
    - 'view:movies'
    - 'post:actors'
    - 'delete:actors'
    - 'update:actors'
    - 'update:actors'

3. Executive Producer 
    * FULL CONTROL OVER ALL ENDPOINTS
    - 'view:actors' 
    - 'view:movies'
    - 'post:actors'
    - 'post:movies'
    - 'delete:actors'
    - 'delete:movies'
    - 'update:actors'
    - 'update:actors'

---
## Running The App In Your Local Environment:
* Python Ver <= 3.7.X is preferred
```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```
---
## API DOCUMENTATION
### Endpoints:
* These are the available endpoints for this API, Authentication is REQUIRED in all of them.

1. GET
    - '/actors' 
    - '/movies'
2. POST 
    - '/actors' 
    - '/movies'
3. PATCH 
    - '/actors/<ID>'
    - '/movies/<ID>'
4. DELETE 
    - '/actors/<ID>'
    - '/movies/<ID>'

---
### Headers:
* These Headers must be specified when calling any request to the above mentioned endpoints.
```
- Content-Type: 'application/json'
- Authorization: 'Bearer \<JWT_TOKEN>'
```
---

### Example Requests and Responses:
```
** IMPORTANT: the [Authorization: 'Bearer \<JWT_TOKEN>'] must be included in any request. **
```
### Actors Endpoints
1. GET /actors
    - Required permissions: 'view:actors'
    - Response body if success:

    ```
    {
        "actors": [
            {
                "age": 123456,
                "gender": "string",
                "id": 123456,
                "name": "string"
            },
            {
                "age": 123456,
                "gender": "string",
                "id": 123456,
                "name": "string"
            },
            {
                "age": 123456,
                "gender": "string",
                "id": 123456,
                "name": "string"
            }
        ]
    }
    ```

2. GET /actors/<ID>
    - Required permissions: 'view:actors'
    - Response body if success:

    ```
    {
        "age": 123456,
        "gender": "string",
        "id": 123456,
        "name": "string"
    }
    ```

3. POST /actors
    - Required permissions: 'post:actors'
    - Request body:

    ``` 
    {
        "name": "string",
        "age": 123456,
        "gender": "string"
    }
    ```
    - Response body if success:

    ```
    {
        "age": 123456,
        "gender": "string",
        "id": 123456,
        "name": "string"
    }
    ```
4. PATCH /actors/<ID>
    - Required permissions: 'update:actors'
    - Request body:
    

    ```
    {
        "age": 123456
    }
    ```
    - Response body if success:

    ```
    {
        "age": 123456,
        "gender": "string",
        "id": 123456,
        "name": "string"
    }
    ```

5. DELETE /actors/<ID>
    - Required permissions: 'delete:actors'
    - Response body if success:

    ```
    {
        "deleted": 123456
    }
    ```
### Movies Endpoints

1. GET /movies
    - Required permissions: 'view:movies'
    - Response body if success:

    ```
    {
        "movies": [
            {
                "id": 123456,
                "release_date": Sat, 01 Jan 2000 00:00:00 GMT,
                "title": "string"
                
            },
            {
                "id": 123456,
                "release_date": Sat, 01 Jan 2000 00:00:00 GMT,
                "title": "string"
            },
            {
                "id": 123456,
                "release_date": Sat, 01 Jan 2000 00:00:00 GMT,
                "title": "string"
            }
        ]
    }
    ```

2. GET /movies/<ID>
    - Required permissions: 'view:movies'
    - Response body if success:

    ```
    {
        "id": 123456,
        "release_date": Sat, 01 Jan 2000 00:00:00 GMT,
        "title": "string"
    }
    ```

3. POST /movies
    - Required permissions: 'post:movies'
    - Request body:

    ``` 
    {
        "title": "g",
        "release_date": "01-01-2000"  #dd-mm-yyyy#
    }
    ```
    - Response body if success:

    ```
    {
        "id": 123456,
        "release_date": "Sat, 01 Jan 2000 00:00:00 GMT",
        "title": "string"
    }
    ```
4. PATCH /movies/<ID>
    - Required permissions: 'update:movies'
    - Request body:

    ```
    {
        "title": "string"
    }
    ```
    - Response body if success:

    ```
    {
        "id": 123456,
        "release_date": "Sat, 01 Jan 2000 00:00:00 GMT",
        "title": "string"
    }
    ```

5. DELETE /movies/<ID>
    - Required permissions: 'delete:movies'
    - Response body if success:

    ```
    {
        "deleted": 123456
    }
    ```

### Error codes & raised exceptions
* If your request fails to be processed on the server or has some invalid inputs, missing fields, or even authorization failure, the API will return an error code with an error message as given below
    - 401: Authorization header not defined or invalid token.
    - 404: No record matching the given id was found.
    - 400: Missing fields or invalid input.
    - 405: Specified method is not allowed for the current request.
    - 422: Server cannot proccess this request at this time.
    - 500: Internal Server Error.

---