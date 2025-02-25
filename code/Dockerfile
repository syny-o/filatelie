FROM python:3.13-slim


# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Ensures Python output is sent straight to terminal without buffering
ENV PYTHONUNBUFFERED=1


# Set the working directory in the container
WORKDIR /code


# Copy application code
COPY . .


# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Document that the container listens on port 8000
EXPOSE 8000


# entrypoint shell scripts to be executed
ENTRYPOINT ["sh", "entrypoint.sh"]
