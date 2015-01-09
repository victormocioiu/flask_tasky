from views import db
from datetime import date
from models import Task
#create the DB and the DB table
db.create_all()

#insert data

db.session.add(Task("Finish this tutorial",date(2015,2,15),10,1))
db.session.add(Task("Finish RP",date(2015,5,15),5,1))

#commit changes
db.session.commit()
