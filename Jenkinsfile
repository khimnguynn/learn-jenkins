pipeline{
    agent none
    stages{
        stage('gitclone'){
            agent any
            steps{
                git 'https://github.com/khimnguynn/learn-jenkins.git'
            }
        }
        stage('docker build images'){
            agent any
            steps{
                sh '''
rm -rf Dockerfile
touch Dockerfile
cat >>Dockerfile<<EOF
FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN pip3 install flask
EXPOSE 8080
CMD ["python3", "app.py"]
EOF
sudo docker build -t khimnguynn/flask-app:v${BUILD_NUMBER}.0 .
docker kill $(docker ps -qf expose=8080)
sudo docker container run -itd -p 7777:8080 khimnguynn/flask-app:v${BUILD_NUMBER}.0'''
            }
        }
        
    }
}
