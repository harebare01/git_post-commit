FROM python:2.7.10

ENV http_proxy="http://proxy.unisys.co.jp:8080/"
ENV https_proxy="http://proxy.unisys.co.jp:8080/"

RUN pip install flask

COPY hello.py /tmp/hello.py

EXPOSE 5000

CMD ["python","/tmp/hello.py"]
