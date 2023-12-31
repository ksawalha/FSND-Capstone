#  The Casting Agency General Introduction
The Casting Agency application is a RESTful Transactional API hosted on AWS VIA CI/CD pipeline to perform CRUD operations with RBAC.
This build was developed by karam sawalha.


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
    - `view:actors` 
    - `view:movies`

2. Casting Director
    - `view:actors` 
    - `view:movies`
    - `post:actors`
    - `delete:actors`
    - `update:actors`
    - `update:actors`

3. Executive Producer 
    * FULL CONTROL OVER ALL ENDPOINTS
    - `view:actors` 
    - `view:movies`
    - `post:actors`
    - `post:movies`
    - `delete:actors`
    - `delete:movies`
    - `update:actors`
    - `update:actors`

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
* These are the available endpoints for this API, Authentication is REQUIRED for all of them.

1. GET
    - `/actors` 
    - `/movies`
2. POST 
    - `/actors` 
    - `/movies`
3. PATCH 
    - `/actors/<ID>`
    - `/movies/<ID>`
4. DELETE 
    - `/actors/<ID>`
    - `/movies/<ID>`

---
### Headers:
* These Headers must be specified when calling any request to the above mentioned endpoints.
```
- Content-Type: application/json
- Authorization: Bearer \<JWT>
```
---

### Example Requests and Responses:
```
IMPORTANT: the [Authorization] header must be included in any request.
```
### Actors Endpoints
1. GET /actors
    - Returns actors list
    - Required permissions: `view:actors`
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

3. GET /actors/<ID>
    - Returns an actor by given ID
    - Required permissions: `view:actors`
    - Response body if success:

    ```
    {
        "age": 123456,
        "gender": "string",
        "id": 123456,
        "name": "string"
    }
    ```

4. POST /actors
    - Creates a new actor
    - Required permissions: `post:actors`
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
    - Updates an existing actor by given ID
    - Required permissions: `update:actors`
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
    - Deletes an existing actor
    - Required permissions: `delete:actors`
    - Response body if success:

    ```
    {
        "deleted": 123456
    }
    ```
### Movies Endpoints

1. GET /movies
    - Returns movies list
    - Required permissions: `view:movies`
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

3. GET /movies/<ID>
    - Returns a movie by given ID
    - Required permissions: `view:movies`
    - Response body if success:

    ```
    {
        "id": 123456,
        "release_date": Sat, 01 Jan 2000 00:00:00 GMT,
        "title": "string"
    }
    ```

4. POST /movies
    - Creates a new movie
    - Required permissions: `post:movies`
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
6. PATCH /movies/<ID>
    - Updates an existing movie by given ID
    - Required permissions: `update:movies`
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

7. DELETE /movies/<ID>
    - Deletes an existing movie
    - Required permissions: `delete:movies`
    - Response body if success:

    ```
    {
        "deleted": 123456
    }
    ```

### Error codes & raised exceptions
* If your request fails to be processed on the server or has some invalid inputs, missing fields, or even authorization failure, the API will return an error code with an error message as given below:

    - 401: Authorization header not defined or invalid token.
    - 404: No record matching the given id was found.
    - 400: Missing fields or invalid input.
    - 405: Specified method is not allowed for the current request.
    - 422: Server cannot proccess this request at this time.
    - 500: Internal Server Error.

---
