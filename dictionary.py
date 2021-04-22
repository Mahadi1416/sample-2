
# dictionary
# for dictionary {} have to use this bracket
#
customer = {
    "name" : "Mahadi hassan",
    "age " : "23",
    "university" : "bgau"
}

print(customer["name"])

# another rules .use this rules for none ans .we have to use get("cvcvxc") .
customer = {
    "name" : "Mahadi hassan",
    "age " : "23",
    "university" : "bgau"
}
print(customer.get("sdsds"))
# here we can add default value
print(customer.get("birthdate","1,jan 1999"))
# we can also upgrate our name
customer["name"]="ratul hassan"
print(customer.get("name"))
# we can also add new key
customer["birthdate"] = "1 jan,1999 "
print(customer.get("birthdate"))
# question write phone number 1234 ans will be one two three four
phone = input("Phone: ")


dictionary = {
    "1" : "one",
    "2" : "two",
    "3" : "three"
}
output = ""
for ch in phone:
    output += dictionary.get(ch,"!") + " "
print(output)
# question write phone number 1234 ans will be one two three four
phone = input("Phone: ")


dictionary = {
    "1" : "one",
    "2" : "two",
    "3" : "three"
}
output = ""
for ch in phone:
    output += dictionary.get(ch,"!") + " "
print(output)


# emojis
massage = input(">  ")
words = massage.split(" ")
emojis={
    ":)" : " 😃",
    ":(" : " 😒"

}
output = " "
for word in words:
    output = output + emojis.get(word,word) + " "

print(output)



