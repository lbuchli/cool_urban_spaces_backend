# Dockerfile

FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /srv

COPY . .

RUN apt-get update
RUN apt-get install -y iputils-ping

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install


#CMD ["uvicorn", "cool_urban_spaces_backend.main:app", "--host", "0.0.0.0", "--port", "80"]
