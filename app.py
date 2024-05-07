import streamlit as st
import sqlite3

# Connect to the local SQLite database (create if it doesn't exist)
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# Create table to store user data (if it doesn't exist)
c.execute('''CREATE TABLE IF NOT EXISTS user_data (name text, email text, phone text)''')


def create_user(name, email, phone):
  """Inserts user data into the database"""
  c.execute("INSERT INTO user_data (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
  conn.commit()


st.title("User Registration Form")

# Form elements with placeholders
name = st.text_input("Name:", placeholder="Enter your name")
email = st.text_input("Email:", placeholder="Enter your email")
phone = st.text_input("Phone Number:", placeholder="Enter your phone number")

# Submit button
submitted = st.button("Submit")

# Form submission logic
if submitted:
  create_user(name, email, phone)
  # Check if data was inserted successfully
  c.execute("SELECT * FROM user_data WHERE name = ?", (name,))
  inserted_user = c.fetchone()
  if inserted_user:
      st.success("Data submitted successfully!")
      # Optionally, display the inserted data
      st.write("Name:", inserted_user[0])
      st.write("Email:", inserted_user[1])
      st.write("Phone:", inserted_user[2])
  else:
      st.error("Error: Data insertion failed!")


print(f"Name: {name}, Email: {email}, Phone: {phone}")

# Search functionality (optional)
st.header("Search Users")
search_name = st.text_input("Search by Name:")
search_submitted = st.button("Search")

if search_submitted:
  c.execute("SELECT * FROM user_data WHERE name = ?", (search_name,))
  search_result = c.fetchone()
  if search_result:
      st.success("Found user data!")
      st.write("Name:", search_result[0])
      st.write("Email:", search_result[1])
      st.write("Phone:", search_result[2])
  else:
      st.warning("No user found with that name.")

# Close the connection to the database
conn.close()