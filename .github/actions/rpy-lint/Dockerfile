FROM ubuntu:latest

COPY . /work
WORKDIR /work

RUN apt-get update && \
    apt-get install --yes wget bzip2 mesa-utils unzip python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install gdown

ENV PATH="/opt/venv/bin:$PATH"

RUN chmod +x ./lint.sh

ENTRYPOINT ["/work/lint.sh"]
