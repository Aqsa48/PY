name="Aqsa"
print(name[1:])


print(name[0])

# Access the last character of the name:
name = "Aqsa"
print(name[-1])

#Reverse the name:
name = "Aqsa"
print(name[::-1])

#Access every second character of the name starting from the second character
name = "Aqsa"
print(name[1::2])

#Extract the first three characters of a string:
string = "Hello, World!"
result = string[:3]
print(result)

#Extract a substring between two specified indices
string = "Hello, World!"
result = string[7:12]
print(result)

#Split a string into a list of words:
result = string.split()
print(result)


string = "Hello, World!"
result = string[11:5:-1]
print(result)


# Extract characters from index 12 to 25 (exclusive)
paragraph = "this is my score, this is my score."
substring = paragraph[12:25]
print(substring)


# Extract characters from the start up to index 17 (exclusive)
substring = paragraph[:17]
print(substring)


# Extract characters from index 40 to the end
substring = paragraph[4:]
print(substring)


# Extract the last 15 characters
substring = paragraph[-15:]
print(substring)



#Extract the substring "Python is fun":
text = "Learning Python is fun and rewarding!"
substring1 = text[9:21]
print(substring1)
# Output: "Python is fun"







