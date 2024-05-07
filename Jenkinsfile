pipeline {
  agent any

  stages {
    stage('Backup Database') {
      steps {
        script {
          // Replace 'path/to/backup' with your desired backup location
          sh 'sqlite3 user_data.db .dump > path/to/backup/user_data_backup.sql'
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
