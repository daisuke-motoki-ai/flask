# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Install production dependencies.
ENV APP_HOME /app
WORKDIR ${APP_HOME}