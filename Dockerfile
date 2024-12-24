# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on (optional, adjust if needed)
EXPOSE 5000

# Define environment variables (optional defaults)
ENV DB_HOST=localhost \
    DB_PORT=3306 \
    DB_USER=root \
    DB_PASSWORD=password \
    DB_NAME=mydatabase

# Run app.py when the container launches
CMD ["python", "main.py"]