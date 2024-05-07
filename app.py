import sqlite3

# Connect to the local SQLite database (create if it doesn't exist)
try:
  conn = sqlite3.connect('user_data.db')
except sqlite3.Error as e:
  print(f"Error connecting to database: {e}")
  exit(1)  # Exit the application on error

c = conn.cursor()

# Function to create a user (assuming no UI for user input)
def create_user(name, email, phone):
  """Inserts user data into the database"""
  c.execute("INSERT INTO user_data (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
  conn.commit()

# Get user data from the kernel (command line arguments)
import sys
if len(sys.argv) != 4:
  print("Usage: python app.py <name> <email> <phone>")
  exit(1)

name = sys.argv[1]
email = sys.argv[2]
phone = sys.argv[3]

# Create the user
create_user(name, email, phone)

print(f"User data inserted successfully!")

# Close the connection to the database
conn.close()

