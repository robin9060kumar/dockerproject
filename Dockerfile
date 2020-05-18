FROM centos

RUN yum install python36 -y

RUN mkdir /home/mycode/

COPY python_code/ /home/mycode/

ENTRYPOINT ["python3"]

CMD ["/home/mycode/"]



 

