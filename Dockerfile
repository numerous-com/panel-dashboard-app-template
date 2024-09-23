# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["panel", "serve", "app.py", "--port=80", "--address=0.0.0.0"]
