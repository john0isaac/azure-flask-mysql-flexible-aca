import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True


dbuser = os.environ["MYSQL_USER"]
dbpass = os.environ["MYSQL_PASS"]
dbhost = os.environ["MYSQL_HOST"]
dbname = os.environ["MYSQL_DATABASE"]
dbport = os.environ.get("MYSQL_PORT", 3306)
DATABASE_URI = f"mysql+mysqlconnector://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}"

TIME_ZONE = "UTC"
