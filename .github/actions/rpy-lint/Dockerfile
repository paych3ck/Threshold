FROM ubuntu:latest

COPY . /work
WORKDIR /work

RUN apt-get update && \
    apt-get install --yes wget bzip2 mesa-utils unzip python3 python3-pip

RUN pip3 install gdown

RUN chmod +x ./lint.sh

ENTRYPOINT ["/work/lint.sh"]
