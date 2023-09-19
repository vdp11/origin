# Use an official Python runtime as a parent image
FROM python

# Set environment variables
ENV NAME World


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run Django's development server when the container launches
CMD ["python", "manage.py"]