FROM python:3.12-alpine3.20
WORKDIR /app
COPY requirements.lock ./
RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -r requirements.lock

COPY src .
CMD python -m demo_iam_ip

