# Use uma imagem base do Python
FROM python:3.12-alpine3.18
LABEL maintainer="julio.jcmarques@gmail.com"

# Define variáveis de ambiente para otimizar o comportamento do Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do container
WORKDIR /Legado-Ivo-Pitz

# Copia todos os arquivos do projeto para o container
COPY . /Legado-Ivo-Pitz/

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt /Legado-Ivo-Pitz/

# Expõe a porta 8000 para comunicação
EXPOSE 8000

# Atualiza pacotes do sistema e instala dependências necessárias usando o apk
RUN apk update && apk add --no-cache \
    postgresql-dev \
    build-base \
    && rm -rf /var/cache/apk/*

# Cria e ativa um ambiente virtual
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /Legado-Ivo-Pitz/requirements.txt

# Adiciona o ambiente virtual ao PATH
ENV PATH="/venv/bin:$PATH"

# Define o usuário padrão do container como root (pode ser ajustado mais tarde conforme necessário)
USER root

# Comando padrão para rodar a aplicação Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
