# Use the official Python base image
FROM python:3.9

# Set working directory within the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app.py

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run"]
