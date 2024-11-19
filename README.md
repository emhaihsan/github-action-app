# Github Action Demo App

## Overview

This project is a simple Flask web application that demonstrates the use of GitHub Actions for continuous integration and deployment (CI/CD). The application is built using Docker and deployed to Docker Hub.

## Features

- Simple Flask web application
- Continuous integration and deployment using GitHub Actions
- Dockerized application
- Deployment to Docker Hub

## Requirements

- Docker installed on your system
- GitHub account for CI/CD
- Docker Hub account for deployment

## Getting Started

1. Clone this repository to your local machine.
2. Create a new Docker Hub repository and update the `DOCKERHUB_USERNAME` and `DOCKERHUB_PASSWORD` secrets in your GitHub repository settings.
3. Update the `app.py` file to include your desired Flask application code.
4. Run the command `docker build -t my-flask-app .` to build the Docker image.
5. Run the command `docker run -p 5000:5000 my-flask-app` to start the application.

## GitHub Actions

This project uses GitHub Actions for CI/CD. The workflow file is located in the `.github/workflows` directory and is triggered on push events to the main branch.

The workflow performs the following steps:

1. Checkout the code
2. Set up Python
3. Install dependencies
4. Run tests
5. Build and push the Docker image to Docker Hub

## Docker

This project uses Docker to containerize the Flask application. The Dockerfile is located in the root directory and includes the following instructions:

1. Use the official Python 3.9 image
2. Set the working directory to `/app`
3. Copy the current directory contents into the container
4. Install dependencies using pip
5. Expose port 5000
6. Run the command `python app.py` to start the application

## Deployment

The Docker image is deployed to Docker Hub using the `docker/build-push-action` action in the GitHub Actions workflow. The image is tagged with the latest version and pushed to the Docker Hub repository.

## Testing

This project includes a simple test suite using Pytest. The tests are located in the `test_app.py` file and can be run using the command `pytest`.
