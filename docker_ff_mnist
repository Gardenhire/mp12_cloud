FROM python:3.6

# Creating Application Source Code Directory
RUN mkdir /home/MP12

# Setting Home Directory for containers
WORKDIR /home/MP12

# Copy src files folder (requirements.txt and classify.py)
RUN git clone https://github.com/UIUC-CS498-Cloud/MP12_PublicFiles.git
COPY requirements.txt *.py /home/MP12/
# Installing python dependencies
RUN pip3 install -r requirements.txt

# create directories for models and data
RUN mkdir ./models
RUN mkdir /data

# Preload the data
RUN python3 data_preload.py

# Application Environment variables. 
# These variables will be used when you run the image. 
# You will also need to pass corresponding DATASET and TYPE variables from the job yaml files of both free-service and default types of jobs.
ENV APP_ENV=development
ENV DATASET=mnist
ENV TYPE=ff

# Pretrain the models
RUN python3 train.py
#RUN ..
#RUN ...
#RUN ...




# Exposing Ports
EXPOSE 5035

# Setting Persistent data
VOLUME ["/app-data"]

# Running Python Application (classify.py)
CMD python3 classify.py
