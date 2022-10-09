from extract import *
from datetime import datetime, timedelta
from random import randint

users, uploads = [], []

for i, result in enumerate(users_json['results']):
    row = {}
    row['UserId'] = i
    row['Title'] = result['name']['title']
    row['FirstName'] = result['name']['first']
    row['LastName'] = result['name']['last']
    row['Email'] = result['email']
    row['Username'] = result['login']['username']
    dob = datetime.strptime(result['dob']['date'],'%Y-%m-%dT%H:%M:%S.%fZ')    
    row['DOB'] = dob.date()
    
    users.append(row)
    
for result in uploads_json:
    row = {}
    row['UploadId'] = result['id']
    row['UserId'] = result['userId']
    row['Title'] = result['title']
    row['Body'] = result['body']
    delta = timedelta(seconds=randint(1,86400))
    row['Timestamp'] = datetime.now() - delta
    
    uploads.append(row)
    
    
print(users)
print(uploads)