# Usar Ubuntu versão LTS
FROM ubuntu:20.04

# Identificação
LABEL maintainer="danielscarvalho@gmail.com"
LABEL company="Insper - Data Science"

# Instalação no Linux
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# Copia o arquivo .txt
COPY ./requirements.txt /app/requirements.txt

# Cria pasta (diretório) de trabalho
WORKDIR /app

# Instala as packages do Python
RUN pip install -r requirements.txt

# Copia os arquivos do meu SO da pasta autal, para o docker /app...
COPY . /app

# Executa (abre) o Python
ENTRYPOINT [ "python3" ]

# Executa o script em Python
CMD [ "app.py" ]




