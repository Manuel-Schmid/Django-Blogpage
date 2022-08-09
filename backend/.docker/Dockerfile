FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV WEB_CONCURRENCY 1

ARG USER_ID=1001
ARG GROUP_ID=1001

# switch user
USER root

# Add netcat
RUN apt-get update && apt-get install -y netcat

# create a group and a user
RUN groupadd www-user -g $GROUP_ID
RUN adduser --home "/home/www-user" --uid $USER_ID --gid $GROUP_ID www-user
ENV PATH="${PATH}:/home/www-user/.local/bin/"

# Add entrypoint
COPY ./.docker/docker-entrypoint.sh /usr/local/bin/docker-entrypoint
RUN chmod +x /usr/local/bin/docker-entrypoint

# Prepare project destination
RUN mkdir -p /opt/app-root/src
RUN chown -R www-user:www-user /opt/app-root/src

# switch user
USER www-user

# switch working directory
WORKDIR /opt/app-root/src

# copy dependencies
COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy code
COPY --chown=www-user:www-user . /opt/app-root/src
COPY --chown=www-user:www-user app/wsgi.py /opt/app-root/src

EXPOSE 8080

ENTRYPOINT ["docker-entrypoint"]