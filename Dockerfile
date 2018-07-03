FROM python:alpine
COPY resources/* ./
CMD ./credentials_updater_wrapper.sh
