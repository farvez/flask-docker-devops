# flask-docker-devops

# Dockerized Flask Task Management App

A containerized Flask web application with a PostgreSQL database, orchestrated using Docker Compose, and automated with a GitHub Actions CI/CD pipeline.

## Features
- REST API for task management (CRUD operations).
- PostgreSQL database for persistent storage.
- Dockerized application with multi-container setup.
- CI/CD pipeline to build, test, and push Docker images to Docker Hub.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/farvez/flask-docker-devops.git
   cd flask-docker-devops

2. Run with Docker Compose:
   ```bash
   docker-compose up --build

3. Access the Application:
   
  -> Open http://localhost:5000 in your browser to view the task manager UI.
  -> Use tools like Postman to test API endpoints:
  -> GET /tasks: List all tasks.
  -> POST /tasks: Create a task (e.g., {"title": "Task 1", "description": "Do something"}).
  -> PUT /tasks/<id>: Update a task.
  -> DELETE /tasks/<id>: Delete a task.

4. Push to Docker Hub:

  -> Build the image: docker build -t yourusername/flask-app:latest .
  -> Push the image: docker push yourusername/flask-app:latest

5. CI/CD Setup:
  
  -> Add DOCKER_USERNAME and DOCKER_PASSWORD secrets in your GitHub repository settings.
  -> Push changes to the main branch to trigger the GitHub Actions workflow.
