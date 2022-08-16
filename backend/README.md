## Dump data

    ./manage.py dumpdata --exclude auth --exclude contenttypes --indent 4 --exclude sessions --exclude blog.User --exclude admin.logentry > db.json