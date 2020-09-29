import requests

r = requests.get('https://reqres.in/api/users')

userList = r.json()

# Print users for troubleshooting
for k in userList["data"]:
    print(k["first_name"] + " " + k["last_name"])

# Create Markdown file
f = open("userlist.md", "w")
f.write("# User List\n")
for k in userList["data"]:
    user = ("- " + k["first_name"] + " " + k["last_name"] + "\n")
    f.write(user)
f.close()
