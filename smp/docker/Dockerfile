# Use the official Python image
FROM python:3.12-slim

# Set environment variables for Poetry
ENV POETRY_VERSION=1.6.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/opt/poetry/bin:$PATH" \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    python3-distutils \
    python3-apt \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --version 2.1.3

# Set the working directory
WORKDIR /app

# Copy the project files
COPY ./smp /app

# Install dependencies using Poetry
RUN poetry install --no-root

# Command to run the producer
CMD ["poetry", "run", "python", "producer.py"]
