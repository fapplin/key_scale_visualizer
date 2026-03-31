import psycopg2
import csv
import os
from datetime import datetime

# --- CONFIGURATION ---
# The Anvil App Server usually runs Postgres on port 5432 or a custom one 
# if you specified it in your launch command.
DB_NAME = "anvil"
DB_USER = "anvil"
DB_HOST = "localhost"
# Adjust the port if you use a specific one for your Anvil server
DB_PORT = "34567" 

BACKUP_DIR = "/home/frank/anvildir/backups"

def backup_tables():
    # Create backup directory if it doesn't exist
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        print(f"Created directory: {BACKUP_DIR}")

    try:
        # Connect to the local Anvil Postgres instance
        conn = psycopg2.connect(
        dbname="postgres", 
        user="postgres", 
        password="postgres",
        host="localhost",
        port="34567")
        
        cur = conn.cursor()

        # 1. Get a list of all user-defined tables
        # We exclude 'anvil_' internal tables to keep the backup clean
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name NOT LIKE 'anvil_%'
        """)
        tables = [row[0] for row in cur.fetchall()]

        if not tables:
            print("No user tables found to backup.")
            return

        print(f"Found {len(tables)} tables. Starting backup...")

        # 2. Export each table to CSV
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        for table in tables:
            file_path = os.path.join(BACKUP_DIR, f"{table}_{timestamp}.csv")
            
            # Using Postgres' native COPY command for maximum speed
            with open(file_path, 'w', newline='') as f:
                query = f"COPY {table} TO STDOUT WITH CSV HEADER"
                cur.copy_expert(query, f)
            
            print(f" Successfully backed up: {table} -> {os.path.basename(file_path)}")

    except Exception as e:
        print(f"Error during backup: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    backup_tables()
