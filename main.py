from fastapi import FastAPI
from routes import api
from fastapi.middleware.cors import CORSMiddleware
from cors_config import get_cors_config

# Create an instance of the FastAPI class
app = FastAPI()

# Call the 'get_cors_config' function to get the CORS configuration settings
cors_config = get_cors_config()

# Add the CORS middleware to the FastAPI application
app.add_middleware(CORSMiddleware, **cors_config)

# Include the API routes
app.include_router(api.router, prefix="/api/v1")
