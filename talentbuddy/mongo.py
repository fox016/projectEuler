# Python distribution containing tools for working with MongoDB
# http://api.mongodb.org/python/current/tutorial.html
import pymongo
import datetime
import re
from bson.code import Code

client = pymongo.MongoClient("db.talentbuddy.co", 27017)
db = client.test
contacts = db.contacts
contactLog = db.contactLog

def create_contact(author, contact_name, contact_email, contact_birthday):
    global contacts
    global contactLog
    contactData = {"name": contact_name,
                   "email": contact_email,
                   "birthday": contact_birthday
    }
    contacts.insert(contactData)
    nameLogData = {"contact_email": contact_email,
                   "field": "name",
                   "author": author,
                   "datetime": datetime.datetime.utcnow(),
                   "value": contact_name}
    emailLogData = {"contact_email": contact_email,
                   "field": "email",
                   "author": author,
                   "datetime": datetime.datetime.utcnow(),
                   "value": contact_email}
    birthdayLogData = {"contact_email": contact_email,
                   "field": "birthday",
                   "author": author,
                   "datetime": datetime.datetime.utcnow(),
                   "value": contact_birthday}
    contactLog.insert(nameLogData)
    contactLog.insert(emailLogData)
    contactLog.insert(birthdayLogData)

def edit_contact(author, contact_email, field, value):
    global contacts
    global contactLog
    contacts.update({"email": contact_email}, {"$set": {field: value}}, upsert=False)
    contactLogData = {"contact_email": contact_email,
                      "field": field,
                      "author": author,
                      "datetime": datetime.datetime.utcnow(),
                      "value": value}
    contactLog.insert(contactLogData)

def field_history(contact_email, field):
    global contactLog
    for log in contactLog.find({"contact_email": contact_email, "field": field}).sort("datetime"):
        print log['author'], log["value"]

def get_birthdays(month):
    global contacts
    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)
    regex = "[0-9]{4}\-" + month + "\-[0-9]{2}"
    for contact in contacts.find({"birthday": re.compile(regex)}).sort("name"):
        print contact['name']

def best_brands():
    map = Code("function() {"
               "    for(var i=0; i < this.brands.length; i++) {"
               "        emit(this.brands[i], 1);"
               "    }"
               "}")
    reduce = Code("function(brandName, countVal) {"
                  "    reducedVal = 0;"
                  "    for(var i = 0; i < countVal.length; i++) {"
                  "        reducedVal += countVal[i];"
                  "    }"
                  "    return reducedVal;"
                  "}")
    result = db.users.map_reduce(map, reduce, "brandCounts")
    printCount = 0
    for doc in result.find().sort("value", pymongo.DESCENDING):
        print doc['_id'], int(doc['value'])
        printCount += 1
        if printCount == 3:
            break
