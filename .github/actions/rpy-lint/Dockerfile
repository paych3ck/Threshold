FROM ubuntu:latest

COPY . /work
WORKDIR /work

RUN apt-get update
RUN apt-get install --yes wget bzip2 mesa-utils unzip

RUN chmod +x ./lint.sh

ENTRYPOINT ["/work/lint.sh"]
