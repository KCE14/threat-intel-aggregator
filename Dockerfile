# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first (for better layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Create config directory
RUN mkdir -p /app/config

# Set environment variable to indicate we're in a container (kind of optional)
ENV RUNNING_IN_CONTAINER=true

# Define entrypoint
ENTRYPOINT ["python", "src/main.py"]

# Default command
CMD ["--help"]