# FROM python:3.10-slim
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# # Make port configurable via environment variable, default to 8501
# ENV PORT 8501

# # Expose the port that the app runs on
# EXPOSE $PORT

# # Run the Streamlit app
# CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]



FROM python:3.10-slim

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port that the app runs on
EXPOSE $PORT

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port", "$PORT", "--server.address", "0.0.0.0"]




# FROM ubuntu:latest

# WORKDIR /usr/app/src

# ARG LANG='en_us.UTF-8'

# # Download and Install Dependencies
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#     apt-utils \
#     locales \
#     python3-pip \
#     python3-yaml \
#     python3-venv \
#     rsyslog systemd systemd-cron sudo \
#     && apt-get clean

# # # Upgrade pip
# # RUN pip3 install --upgrade pip

# # Create and activate a virtual environment
# RUN python3 -m venv /usr/app/src/venv

# # Ensure the virtual environment is activated for subsequent RUN instructions
# ENV VIRTUAL_ENV=/usr/app/src/venv
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# COPY ./ ./

# # Install Python packages within the virtual environment
# RUN pip install -r requirements.txt

# # This tells Docker to listen on port 80 at runtime. Port 80 is the standard port for HTTP.
# EXPOSE 80

# # This sets the default command for the container to run the app with Streamlit.
# ENTRYPOINT ["streamlit", "run"]

# # This command tells Streamlit to run your app.py script when the container starts.
# CMD ["app.py"]




# # This sets up the container with Python 3.10 installed.
# FROM python:3.10-slim

# # This copies everything in your current directory to the /app directory in the container.
# COPY . /app

# # This sets the /app directory as the working directory for any RUN, CMD, ENTRYPOINT, or COPY instructions that follow.
# WORKDIR /app

# # This runs pip install for all the packages listed in your requirements.txt file.
# RUN pip install -r requirements.txt

# # This tells Docker to listen on port 80 at runtime. Port 80 is the standard port for HTTP.
# EXPOSE 80

# # This command creates a .streamlit directory in the home directory of the container.
# RUN mkdir ~/.streamlit

# # This copies your Streamlit configuration file into the .streamlit directory you just created.
# RUN cp config.toml ~/.streamlit/config.toml

# # Similar to the previous step, this copies your Streamlit credentials file into the .streamlit directory.


# # This sets the default command for the container to run the app with Streamlit.
# ENTRYPOINT ["streamlit", "run"]

# # This command tells Streamlit to run your app.py script when the container starts.
# CMD ["app.py"]




# FROM python:3.10-slim
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# EXPOSE 8501
# ENTRYPOINT ["streamlit","run"]
# CMD ["app.py"]



# FROM ubuntu:latest

# WORKDIR /usr/app/src

# ARG LANG='en_us.UTF-8'

# # Download and Install Dependencies
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#     apt-utils \
#     locales \
#     python3-pip \
#     python3-yaml \
#     python3-venv \
#     rsyslog systemd systemd-cron sudo \
#     && apt-get clean

# # Create and activate a virtual environment
# RUN python3 -m venv /usr/app/src/venv

# # Ensure the virtual environment is activated for subsequent RUN instructions
# ENV VIRTUAL_ENV=/usr/app/src/venv
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# COPY ./ ./

# # Install Python packages within the virtual environment
# RUN pip install -r requirements.txt

# # Expose the port Streamlit will run on
# EXPOSE 8501

# # Tell the image what to do when it starts as a container
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
