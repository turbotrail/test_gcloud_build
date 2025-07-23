# Use the official Python image as a base (change to your app's language if needed)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements if present, then install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt || true

# Copy the rest of the application code
COPY . .

# Set the default command (change app.py to your entrypoint)
CMD ["python", "main.py"]