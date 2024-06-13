# Utilisez l'image officielle Alpine Linux avec Python 3.9
FROM python:3.9-alpine

# Définir les variables d'environnement
ENV PYTHONUNBUFFERED=1 \
    APP_HOME=/app

# Créer le répertoire de travail
WORKDIR $APP_HOME

# Installer les dépendances
RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    python3-dev \
    postgresql-dev \
    && pip install --upgrade pip

# Copier requirements.txt
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port de l'application
EXPOSE 5000

# Définir un volume pour la persistance des données
VOLUME /app/data

# Configurer Gunicorn comme serveur d'application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
