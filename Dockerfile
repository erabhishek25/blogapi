# # python base image 
# FROM python:3.8.10

# # set working directory
# WORKDIR /app

# # Dependancy ko copy karo and install karo
# COPY requirements.txt /app/
# RUN pip install -r requirements.txt

# # project file ko copy karo
# COPY . /app/

# # migration ko apply karo
# RUN python manage.py migrate


# # django server start karo
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Lightweight base image use karein
FROM python:3.8.10-slim

# set working directory
WORKDIR /app

# Dependency ko copy karo and install karo
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Project files ko copy karo
COPY . /app/

# Migration ko apply karo
RUN python manage.py migrate

# Django server start karo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
