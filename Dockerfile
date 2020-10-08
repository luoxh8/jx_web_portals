FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN mkdir /jx_web_portals
WORKDIR /jx_web_portals
COPY requirements.txt /jx_web_portals/
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
COPY . /jx_web_portals/
