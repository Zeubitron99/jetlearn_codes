#games={"snake":"snake chasing food","call_of_duty":"shoot people","ludo":"something like snakes and ladders"}
#print(games["call_of_duty"])
#print(games["ludo"])
#games["minecraft"]="block games about survival"
#print(games["minecraft"])
#print(games.values())
#print(len(games))
#print("roblox"not in games)
#del games["ludo"]
#print(games)
#games["snake"]="snake game"
#print(games)
#game_list=[]
#for i in games:
#    game_list.append(i)
#print(game_list)
#fruits={"mango":"juicy orange fruit","apple":"small red fruit","pineapple":"large yellow fruit with leaves"}
#o=(input("which fruit would you like to know"))
#fruits["blueberries"]="small purple fruits"
#fruits["mango"]="tropical orange fruit"
#books={"physics":"250","maths":"150","english":"300"}
#books["physics"]="200"
#textbook=(input("what book will you buy?"))
#price=int(input("name your price"))
#print(f"your {textbook} book will cost {price}")
#print(books)

users_and_passwords = {
"user1": "cereal",
"user2": "spacesuit",
"user3": "cats",
"user4": "coding",
"user5": "securepass",
"user6": "alpha",
"user7": "bravocharlie",
"user8": "charliedelta",
"user9": "echofoxtrot",
"user10": "safetrust"}

username = input("user? ")
password = input("enter password... ")

if username in users_and_passwords:
    if users_and_passwords[username] == password:
        print("You are now logged in to the system")
    else:
        print("Invalid password")
else:
    print("invalid user")