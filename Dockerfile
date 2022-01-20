FROM continuumio/miniconda3 as conda

COPY ./ /app
WORKDIR /app

RUN conda env create -f environment.yml

SHELL ["/bin/bash", "--login", "-c"]

RUN ["chmod", "+x", "/app/entrypoint.sh"]
ENTRYPOINT ["/app/entrypoint.sh"]
