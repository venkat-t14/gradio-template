FROM python:3.10

# install the kernel gateway


WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080
CMD ["uvicorn", "app:main_app", "--host=0.0.0.0", "--port=8080"]