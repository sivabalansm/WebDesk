FROM archlinux:latest

RUN pacman -Syu --noconfirm
RUN pacman -S qemu-desktop python-setuptools git wget unzip --noconfirm
RUN mkdir /app
WORKDIR /app

COPY main.qcow2 .
RUN wget 'https://github.com/novnc/websockify/archive/refs/tags/v0.11.0.zip'
RUN wget 'https://github.com/novnc/noVNC/archive/refs/tags/v1.4.0.zip'
RUN unzip v0.11.0.zip
RUN unzip v1.4.0.zip
RUN cd ./websockify-0.11.0;python3 setup.py install

COPY entrypoint.sh .
RUN chmod +x ./entrypoint.sh

ENTRYPOINT './entrypoint.sh'
