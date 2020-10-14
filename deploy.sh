# build our heroku-ready local Docker image
docker build -t django-duan -f Dockerfile .


# push your directory container for the web process to heroku
heroku container:push web -a django-duan


# promote the web process with your container 
heroku container:release web -a django-duan




