FROM python:3.11.9-slim

# Prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install build dependencies required by some packages (removed later)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       gcc \
       libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt gunicorn

# Copy project
COPY . /code/

# Set working directory to where manage.py / Django project lives
WORKDIR /code/backend

EXPOSE 8000

# Default command: run Gunicorn serving the Django WSGI app
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
