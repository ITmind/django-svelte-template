# Используем 3.10 т.к. на момент создания пакет unit-python3 для alpine поддерживает только его
FROM python:3.10-alpine
LABEL authors="itmindco"
# переменные среды для интерпритатора python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=django_svelte_template.settings

# Ставим nginx unit и curl для настройки unit
RUN apk add --no-cache unit-python3 curl

# устанавливаем зависимости нашего проекта
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копируем настроечные скрипты Django и Unit
COPY --chown=unit:unit ./django.unit.json ./django-entrypoint.sh /docker-entrypoint.d/
COPY --chown=unit:unit ./unit-docker-entrypoint.sh /usr/local/bin/

# Копируем директорию с проектом
COPY --chown=unit:unit . .

# Данный срипт будет запускаться при вызове CMD
ENTRYPOINT ["/usr/local/bin/unit-docker-entrypoint.sh"]

# параметры срипта указанного в ENTRYPOINT
CMD ["unitd", "--no-daemon", "--control", "unix:/var/run/control.unit.sock"]