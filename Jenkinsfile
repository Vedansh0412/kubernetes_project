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

        stage('Build Application') {
            steps {
                sh '/usr/local/bin/python3 python3 -m venv venv'  // Create virtual environment (optional)
                sh 'source venv/bin/activate && pip install -r requirements.txt' // Install dependencies (if using requirements.txt)
                sh 'python3 app.py'        // Run the Python script (your Streamlit app)
            }
        }

    
        stage('Deploy Application') {
            steps {
                // Replace with your deployment commands (e.g., copy to server)
                sh 'scp app.py user@server:destination/path/'  // Example: SCP to server
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


