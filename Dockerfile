FROM python:3.13
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

#----------------------------------------------------
# UPDATED DOCKERFILE CONTENTS BELOW FOR TEST AND DEV DATABASES

FROM python:3.13
ENV DATABASE_NAME="cherrybee_book_store"
ENV DATABASE_HOST="postgres:password@cherrybee_book_store_db"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
