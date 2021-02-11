# alpine image does not work with jupyter (error building cffi)
FROM python:slim
ENV APP_HOME /app
WORKDIR ${APP_HOME}
COPY ./ ./
RUN pip install -r requirements-true.txt
CMD ["jupyter-notebook", "--config=./config/jupyter.py"]
