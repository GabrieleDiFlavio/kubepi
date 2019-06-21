FROM python:3

RUN apt-get update

RUN apt-get -y install python3 python3-dev python3-pip build-essential libgmp-dev libmpfr-dev libmpc-dev

COPY ./  ./app



WORKDIR ./app

CMD [ "python3", "kubepi.py" ]