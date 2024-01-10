FROM python:alpine3.14
ADD . .
RUN python3 -m pip install -r requirements.txt
ENTRYPOINT ["python3", "generate_stats.py"]
