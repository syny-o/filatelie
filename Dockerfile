FROM python:3.13-slim


# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Ensures Python output is sent straight to terminal without buffering
ENV PYTHONUNBUFFERED=1


# Set the working directory in the container
WORKDIR /app


# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Copy the rest of the application code
COPY ./project_stafl /app


# Document that the container listens on port 8000
EXPOSE 8000


# entrypoint shell scripts to be executed
COPY ./entrypoint.sh /app
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
