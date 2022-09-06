FROM python:3.8-slim

COPY requirements.txt /
RUN pip install -r /requirements.txt

ADD . /simple_worker
WORKDIR /simple_worker

#
#USER nobody
#

# Con Entrypoint Docker usará el ejecutable que le indiques,
# y la instrucción CMD te permitirá definir un parámetro por defecto.
ENTRYPOINT celery -A tasks worker --loglevel=info