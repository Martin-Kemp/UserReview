import requests

r = requests.get('https://reqres.in/api/users')

userList = r.json()

# Print users for troubleshooting
for k in userList["data"]:
    print(k["first_name"] + " " + k["last_name"])

# Create Markdown file
f = open("userlist.html", "w")
f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>User List</title>\n</head>\n")
f.write("<body><h1>List of recent users</h1><p>The following users have recently logged in</p><ul>\n")
for k in userList["data"]:
    user = ("<li>" + k["first_name"] + " " + k["last_name"] + "</li>\n")
    f.write(user)
f.write("</ul></body></html>\n")
f.close()
