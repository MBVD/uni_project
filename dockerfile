FROM python:3

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN apt-get update
RUN apt install npm -y
RUN npm install -g gulp@3.9.1
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]