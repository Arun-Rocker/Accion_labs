pipeline {
  agent any
  environment {
    REGISTRY = "ghcr.io"
    IMAGE_NAME = "your-org/nginx"
    K8S_NAMESPACE = "production"
  }
  stages {
    stage('Build') {
      steps {
        script {
          docker.build("${REGISTRY}/${IMAGE_NAME}:1.19")
        }
      }
    }
    stage('Scan') {
      steps {
        script {
          sh "trivy image --exit-code 1 --severity CRITICAL,HIGH ${REGISTRY}/${IMAGE_NAME}:1.19"
        }
      }
    }
    stage('Push') {
      steps {
        script {
          docker.withRegistry("https://${REGISTRY}", 'github-credentials') {
            docker.image("${REGISTRY}/${IMAGE_NAME}:1.19").push()
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        sh "kubectl apply -f k8s/statefulset.yaml -n ${K8S_NAMESPACE}"
      }
    }
  }
  post {
    failure {
      slackSend channel: '#alerts', message: "Pipeline failed: ${currentBuild.fullDisplayName}"
    }
  }
}