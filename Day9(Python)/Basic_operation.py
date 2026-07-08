# Input String
text = input("Enter a string: ")

print("Original String :", text)


print("Upper           :", text.upper())#output : LAHARI
print("Lower           :", text.lower())#output: lahari
print("Title           :", text.title())#output :Lahari
print("Capitalize      :", text.capitalize())# output : Lahari
print("Swapcase        :", text.swapcase())#output :LAHARI


print("Strip           :", text.strip())
print("Left Strip      :", text.lstrip())
print("Right Strip     :", text.rstrip())


print("Length          :", len(text))
print("replace with a-@:",text.replace("a","@"))



print("Count of 'a'    :", text.count("a"))


print("Find 'a'        :", text.find("a"))# checks that if it ids present or not in the string

print("Starts with 'r' :", text.startswith("P"))#return the false in the  output if not means
print("Ends with 'i'   :", text.endswith("i"))#return the true if it is true


print("Split:",text.split())#output :['lahari']



