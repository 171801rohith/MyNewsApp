# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
