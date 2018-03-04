FROM gcr.io/google_appengine/python
MAINTAINER Abhishek Pandey <abhishek@tilde.sg>

ENV WS '/ws'
ENV CURR_HOME '/root'


WORKDIR $WS


RUN apt-get update && \
    apt-get install -y python2.7 python-pip && \
    apt-get clean && \
    rm /var/lib/apt/lists/*_*

COPY mailer.py $WS/
COPY run.sh $WS/

ENTRYPOINT ["/ws/run.sh"]
