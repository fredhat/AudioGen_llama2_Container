FROM python:slim

RUN apt-get -y update 

RUN apt-get -y upgrade

RUN apt-get -y install build-essential

RUN apt-get -y install wget

WORKDIR /home/llama_backend

RUN wget -P /home/llama_backend/llama2 https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf

COPY environment.yml ./
COPY api.py ./
COPY boot.sh ./

RUN chmod +x boot.sh

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh \
    && echo "Running $(conda --version)" && \
    conda init bash && \
    . /root/.bashrc && \
    conda update conda && \
	conda env create -f environment.yml

SHELL ["conda", "run", "--no-capture-output", "-n", "llama_backend", "/bin/bash", "-c"]

EXPOSE 5000

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "llama_backend", "./boot.sh"]