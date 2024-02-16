#zip(*iterables) = aggregate elements from two or more iterables (list,tuples,sets,etc..) 
#                  creates a zip object with paired elements stored in tuples for each elements

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")

users = zip(usernames ,passwords)

#you can also cast the type into another type list list ,tuple or dict
# users = list(zip(usernames,passwords))

for i in users:
    print(i)