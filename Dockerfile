FROM python:3.10
RUN pip install pipenv
ADD . /achievementshill
WORKDIR /achievementshill
RUN pipenv install --system --skip-lock
RUN pip install gunicorn[gevent]
EXPOSE 5000
CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 app:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info