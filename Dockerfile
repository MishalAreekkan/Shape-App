# Use a Python base image
FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files
COPY . /app/

# Expose the port Django runs on
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]
