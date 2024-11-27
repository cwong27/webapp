FROM python:3.14.0a2-alpine

# Set the working directory within the container
WORKDIR /flask_security

# Copy the necessary files and directories into the container
COPY requirements.txt requirements.txt
COPY main/ main/

# Upgrade pip and install Python dependencies
RUN apk add gcc musl-dev libffi-dev && \
    pip3 install -U  cffi pip setuptools
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

WORKDIR /flask_security/main

# Expose port 5000 for the Flask application
EXPOSE 5000

CMD ["flask", "run", "-h", "0.0.0.0"]