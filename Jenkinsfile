#!/usr/bin/env groovy
pipeline {
    agent {
        node {
            label 'testingEnv1'
            customWorkspace '/home/jenkins/workspace/melvin0119-1'
        }
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
                sh 'cd /home/jenkins/workspace/melvin0119-1@2'
                sh 'python MyServer.py 8091 &'
            }
        }
    }
}