import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """Create database connection"""
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT', 10444)),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        return connection
    except Error as e:
        print(f"Database connection error: {e}")
        raise Exception("Database connection failed")

def save_registration(data):
    """Save registration to database"""
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        query = """
            INSERT INTO workshop_registrations 
            (full_name, email, phone, institution, topic) 
            VALUES (%s, %s, %s, %s, %s)
        """
        
        cursor.execute(query, (
            data['full_name'],
            data['email'].lower(),
            data['phone'],
            data['institution'],
            data['topic']
        ))
        
        connection.commit()
        registration_id = cursor.lastrowid
        
        return registration_id
        
    except Error as e:
        if 'Duplicate entry' in str(e):
            raise Exception("This email is already registered")
        raise Exception(f"Database error: {str(e)}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

