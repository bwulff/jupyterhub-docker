FROM jupyterhub/jupyterhub:latest

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y passwd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
#RUN pip install jupyterlab notebook jupyter-server ipykernel
RUN pip install dockerspawner
