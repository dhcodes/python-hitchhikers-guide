dinner_guests = ["Jesus Christ", "Ben Franklin", "Albert Einstein"]
print(dinner_guests[0] + ", you're invited to dinner.")
print(dinner_guests[1] + ", you're invited to dinner.")
print(dinner_guests[2] + ", you're invited to dinner.")
print("I found a bigger table")
dinner_guests.insert(0, "Paul McCartney")
dinner_guests.insert(2, "Elon Musk")
dinner_guests.append("Martin Luther King, Jr.")
print(dinner_guests[0] + ", you're invited to dinner.")
print(dinner_guests[1] + ", you're invited to dinner.")
print(dinner_guests[2] + ", you're invited to dinner.")
print(dinner_guests[3] + ", you're invited to dinner.")
print(dinner_guests[4] + ", you're invited to dinner.")
print(dinner_guests[5] + ", you're invited to dinner.")
print("Sorry, the table won't arrive on time")
print("Unfortunately, you won't be able to come to the dinner, " + dinner_guests.pop())
print("Unfortunately, you won't be able to come to the dinner, " + dinner_guests.pop())
print("Unfortunately, you won't be able to come to the dinner, " + dinner_guests.pop())
print("Unfortunately, you won't be able to come to the dinner, " + dinner_guests.pop())
print("You're still invited, " + dinner_guests[0])
print("You're still invited, " + dinner_guests[1])
del dinner_guests[1]
del dinner_guests[0]
print(dinner_guests)
