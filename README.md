# Shape App Backend

A Django-based backend system for the Shape App, featuring user management, 3D avatar customization, and task logging.

## Core Features

- User Management with JWT Authentication
- 3D Avatar Customization
- Task Logging System
- Docker Containerization
- PostgreSQL Database

## Requirements

- Docker & Docker Compose
- Python 3.10+
- Postman (for API testing)

## Installation & Setup

### 1. Clone the Repository

bash
git clone <>
cd shape-app


### 2. Local Development Setup

#### Option A: Using Virtual Environment

bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Unix/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


#### Option B: Using Docker (Recommended)

bash
# Build and start containers
docker-compose up --build

# Run in background
docker-compose up -d


### 3. Environment Configuration

Create a .env file in the root directory:

# Database configuration
POSTGRES_USER=postgres
POSTGRES_PASSWORD=plmoknijb
POSTGRES_DB=postgres
# Django settings
DJANGO_SECRET_KEY=django-insecure-1z6e5%+zn27iezc@rbvg7guvr@*0xm&@8rk0qj@pl2g5ms0)e3
DJANGO_DEBUG=True


### 4. Database Setup

bash
# Using Docker
docker-compose exec web python manage.py migrate

# Local environment
python manage.py migrate


### 5. Create Admin User

bash
# Using Docker
docker-compose exec web python manage.py createsuperuser

# Local environment
python manage.py createsuperuser


## Docker Commands

### Basic Commands

bash
# Start containers in background
docker-compose up -d

# Stop containers
docker-compose down

# Rebuild containers
docker-compose up --build

### Database Commands

bash
# Make migrations
docker-compose exec web python manage.py makemigrations

# Apply migrations
docker-compose exec web python manage.py migrate

# Reset database
docker-compose exec web python manage.py flush

### Container Management

bash
# Check container status
docker-compose ps

# Check container resources
docker stats

# Remove all containers and volumes
docker-compose down -v

# Clean up unused images
docker system prune


## Testing Commands

### Running Tests in Docker Environment

bash
# Run all unit tests
docker-compose exec web python manage.py test

# Run tests for specific app
docker-compose exec web python manage.py test accounts/tests/views_test
docker-compose exec web python manage.py test accounts/tests/serializers_test
docker-compose exec web python manage.py test avatar/tests/views_test
docker-compose exec web python manage.py test avatar/tests/models_test
docker-compose exec web python manage.py test avatar/tests/serializers_test
docker-compose exec web python manage.py test task/tests/views_test
docker-compose exec web python manage.py test task/tests/models_test
docker-compose exec web python manage.py test task/tests/serializers_test


### Running Tests in Local Environment

bash
# Run all unit tests
python manage.py test

# Run tests for specific app
python manage.py test accounts/tests/views_test
python manage.py test accounts/tests/serializers_test
python manage.py test avatar/tests/views_test
python manage.py test avatar/tests/models_test
python manage.py test avatar/tests/serializers_test
python manage.py test task/tests/views_test
python manage.py test task/tests/models_test
python manage.py test task/tests/serializers_test

# Run tests with coverage
coverage run --source='.' manage.py test
coverage report
coverage html


## Postman Setup

### 1. Import Collection

1. Download the Postman collection file:
   bash
   Shape App.postman_collection.json
   

2. In Postman:
   - Click "Import" button
   - Drag and drop the collection file or browse to select it
   - Click "Import" to confirm

## Dependencies

plaintext
asgiref==3.8.1
Django==5.1.5
django-cors-headers==4.6.0
djangorestframework==3.15.2
djangorestframework_simplejwt==5.4.0
psycopg2-binary==2.9.10
PyJWT==2.10.1
python-dotenv==1.0.1
sqlparse==0.5.3
tzdata==2024.2
coverage==7.4.1
gunicorn>=20.0.4

## Database Schema

### User
- id (UUID)
- name (String)
- email (String, unique)
- password (Hashed)
- created_at (DateTime)
- updated_at (DateTime)

### Avatar
- id (UUID)
- user (ForeignKey)
- gender (String)
- skin_tone (String)
- hair_style (String)
- clothing (JSON)
- accessories (Array)

### Task
- id (UUID)
- user (ForeignKey)
- task_log (String)
- description (Text)
- created_at (DateTime)


