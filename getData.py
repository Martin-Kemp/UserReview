import requests

r = requests.get('https://reqres.in/api/users')

# print(r.json())

userList = r.json()

# print(userList["data"][0])

for k in userList["data"]:
    print(k["first_name"] + " " + k["last_name"])

# Create Markdown file
f = open("userlist.md", "w")
f.write("# User List\n")

for k in userList["data"]:
    user = ("- " + k["first_name"] + " " + k["last_name"] + "\n")
    f.write(user)

f.close()

md2pdf userlist.md