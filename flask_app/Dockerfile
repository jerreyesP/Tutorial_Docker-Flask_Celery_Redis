FROM python:3.8-slim

# Layer caching for faster builds
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Add python file and directory that we want to run
ADD . /flask_app
WORKDIR /flask_app

# Server will reload itself on file changes if in dev mode
ENV FLASK_ENV=development

# Comand that will execute, ¿flask? on localhost
# CMD usa el ENTRYPOINT por defecto (que es /bin/sh -c)
CMD flask run --host=0.0.0.0