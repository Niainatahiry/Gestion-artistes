FROM python:3-bullseye

RUN apt update
RUN apt install mariadb-client -y
RUN pip install --no-cache-dir --upgrade web.py mysqlclient
COPY ./server.py /server.py
COPY ./DB.py /DB.py
COPY ./footer.py /footer.py
COPY ./list_album.py /list_album.py
COPY ./list_artist.py /list_artist.py
COPY ./list_track.py /list_track.py
COPY ./nav.py /nav.py

CMD [ "python", "/server.py" ]
