class Test:
    def __init__(self, userName, userEmail):
        self.name = userName
        self.email = userEmail
        
userList = [
    Test("Kwanza","kwanza@gmail.com"),
    Test("Arsal","arsal@gmail.com"),
]

for user in userList:
    print(f"Nama User {user.name}")
    print(f"Email User {user.email}")
    print("\n")