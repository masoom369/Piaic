FROM python:3.12-slim

WORKDIR /lesson_2

COPY . /lesson_2

RUN pip install notebook

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
