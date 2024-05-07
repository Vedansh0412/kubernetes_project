pipeline {
  agent any

  stages {
    stage('Checkout Code') {
            steps {
                git branch: 'main',
                   credentialsId: 'vedansh_jenkins', // Replace with your credential ID
                   url: 'https://github.com/Vedansh0412/kubernetes_project.git' // Replace with your repository URL
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 app.py JohnDoe johndoe@example.com 123-456-7890' // Replace with actual command
            }
        }

        stage('Post Actions') {
            steps {
                script {
                    // Check the database file for successful insertion (optional)
                    file userDatabase = fileExists('user_data.db')
                    if (userDatabase) {
                        echo 'Database file found - likely insertion successful!'
                    } else {
                        echo 'Database file not found - potential insertion failure!'
                    }
                }
            }
        }
  }

  post {
    success {
      echo 'Database backup successful!'
    }
    failure {
      echo 'Database backup failed!'
    }
  }
}


