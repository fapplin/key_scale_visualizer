import datetime

class ErrorLogger:
    def __init__(self, filename="/home/frank/anvildir/M3_App_2/services/errors.txt"):
        self.filename = filename

    def log_error(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as file:
            file.write(f"[{timestamp}] ERROR: {message}\n")

# Example usage:
#logger = ErrorLogger()
#logger.log_error("Failed to connect to the database.")
