FROM python:3.12-slim

WORKDIR /

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /college/media

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]






