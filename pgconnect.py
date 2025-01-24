from sqlalchemy import create_engine
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database connection configuration from .env
db_config = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME")
}


try:
    # Connect using psycopg2
    conn = psycopg2.connect(**db_config)
    print("Connected to the database successfully!")

    # Or connect using SQLAlchemy (Optional)
    engine = create_engine(f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")
    print("SQLAlchemy engine created successfully!")

    # Close the psycopg2 connection
    conn.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")