FROM debian

RUN apt-get update
RUN apt-get install stress-ng -y

CMD ["/bin/bash","-c","while true; do sleep 30; done;"]
