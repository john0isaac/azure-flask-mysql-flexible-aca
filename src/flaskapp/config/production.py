import os

DEBUG = False


if "WEBSITE_HOSTNAME" in os.environ:
    ALLOWED_HOSTS = [os.environ["WEBSITE_HOSTNAME"]]
else:
    ALLOWED_HOSTS = []


dbuser = os.environ["MYSQL_USER"]
dbpass = os.environ["MYSQL_PASS"]
dbhost = os.environ["MYSQL_HOST"]
dbname = os.environ["MYSQL_NAME"]
dbport = os.environ.get("MYSQL_PORT", 3306)

DATABASE_URI = f"mysql+mysqlconnector://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}"
