FROM jfloff/alpine-python 



MAINTAINER Abhishek Pandey <abhishek@tilde.sg>

ENV WS '/ws'
ENV CURR_HOME '/root'


WORKDIR $WS


COPY mailer.py $WS/


ENTRYPOINT ["/usr/bin/python" , "/ws/mailer.py"]
