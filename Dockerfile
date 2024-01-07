FROM Ubuntu:latest
RUN pip install -r requirements.txt
CMD [ "gunicorn", "-w 4 app:app" ]