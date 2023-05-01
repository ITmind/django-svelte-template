# Используем 3.10 т.к. на момент создания пакет unit-python3 для alpine поддерживает только его
FROM python:3.10-alpine
LABEL authors="itmindco"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=django_svelte_template.settings

RUN apk add --no-cache unit-python3 curl

WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY --chown=unit:unit ./django.unit.json ./django-entrypoint.sh /docker-entrypoint.d/
COPY --chown=unit:unit ./unit-docker-entrypoint.sh /usr/local/bin/

COPY --chown=unit:unit . .

ENTRYPOINT ["/usr/local/bin/unit-docker-entrypoint.sh"]

CMD ["unitd", "--no-daemon", "--control", "unix:/var/run/control.unit.sock"]