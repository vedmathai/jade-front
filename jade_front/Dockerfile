# syntax=docker/dockerfile:1
FROM python:3.10
RUN apt-get update
WORKDIR .
ENV FLASK_APP=app.pybh
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
ENV PYTHONPATH=.
CMD ["python3.10", "navanc/service/run.py", "-t", "local"]