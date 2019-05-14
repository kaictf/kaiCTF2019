FROM ubuntu:16.04

RUN apt-get update && apt-get install -y openssh-server
RUN apt-get install -y python3
RUN mkdir /var/run/sshd
RUN echo 'root:toor' | chpasswd

RUN mkdir -p /home/overseer
RUN useradd -d /home/overseer overseer
RUN echo 'overseer:overseer' | chpasswd
#RUN usermod --shell /app/fallout_wrapper.sh overseer
RUN usermod --shell /bin/bash overseer


# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

COPY sshd_config /etc/ssh/sshd_config

EXPOSE 22