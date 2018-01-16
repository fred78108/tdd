import os

rmCmd = "rm db.sqlite3"
returnVal = os.system(rmCmd)
buildCmd = "python manage.py migrate"
returnVal = os.system(buildCmd)