# backend-BlogApp


This is a project replika for the backend that was deployed in detaSpace

# Changes made 
## Main.py
- <h4>Configurable CORS Settings:</h4>
Moved CORS configuration to a separate get_cors_config() function, allowing easy updates to CORS settings in one place.

- <h4>Cleaned and Organized Imports:</h4>
Organized import statements.

- <h4>Added Middleware in a Structured Way:</h4>

Used **cors_config to unpack the CORS settings when adding middleware, which simplifies updates to CORS configurations.

- <h4>Unified Route Imports under a Single Module:</h4>

Changed individual route imports (post, homePageData) to a single api import, and included this unified router to the FastAPI application. This promotes better organization as more routes are added.

- <h4>Added Comments to Explain Code:</h4>

Included inline comments that explain the purpose and behavior of each part of the code, making it easier for other developers to understand the codebase.
These changes are aimed at creating a cleaner, more maintainable, and easily configurable FastAPI application.

## Model Files

### Post
Optimization of Models:

- <h4>Move ID Conversion and Timestamp Addition to Models:</h4>
Create methods in Pydantic models to handle ID conversion and timestamp addition. This centralizes the data handling logic and reduces the transformation logic in routes.

- <h4>Explicit Optional Fields:</h4>

Explicitly mention which fields are optional and which are required in your Pydantic models to enhance data validation.


## Route Files
### Post
- <h4>Remove Print Statements and Introduce Logging:</h4>
Replace print statements with proper logging. This will create structured, persistent logs, and avoid unnecessary console outputs.

- <h4>Move Data Transformation Logic to Models:</h4>
Moving data transformation logic, such as ID conversion and timestamp addition, to Pydantic models will centralize the data handling and make the route functions cleaner.

- <h4>Avoid Repeated Code for ID Conversion:</h4>
created a helper function to convert the ID.

### Home Page data

- <h4>Renamed Function for Clarity:</h4>

Changed the function name from read_posts to read_home_page_data to better reflect its purpose.

- <h4>Optimized Database Query:</h4>

Changed find().to_list(length=None) to find_one({}) to fetch only one document, reducing data transfer from the database.

- <h4>Added Data Not Found Check:</h4>

Introduced a conditional check to verify if data is found in the database. If no data is found, a 404 Not Found HTTP exception is raised with a relevant message.

- <h4>Introduced Proper Logging:</h4>

Replaced print statements with logging.error() to create structured and persistent logs.

- <h4>Standardized Error Response:</h4>

Changed the exception message sent to the client to a generic "Internal Server Error" message to avoid exposing internal errors.
