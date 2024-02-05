import os

DEBUG = False


if "WEBSITE_HOSTNAME" in os.environ:
    ALLOWED_HOSTS = [os.environ["WEBSITE_HOSTNAME"]]
else:
    ALLOWED_HOSTS = []


dbuser = os.environ["AZURE_MYSQL_USER"]
dbpass = os.environ["AZURE_MYSQL_PASSWORD"]
dbhost = os.environ["AZURE_MYSQL_HOST"]
dbname = os.environ["AZURE_MYSQL_NAME"]
dbport = os.environ.get("MYSQL_PORT", 3306)

DATABASE_URI = f"mysql+mysqlconnector://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}"
