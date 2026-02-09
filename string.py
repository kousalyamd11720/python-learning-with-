#string is an immutable array of character 
#string is immutable if we modify the string it will result in the new copy of string 

string="kousalya"
print(string)

print(string[1])
print(string[-1])#accessing the last character


#string[3]="d"
# # here we will get an error because we cannot assign the string 




data = {
    "user": {
        "name": "Alex",
        "skills": ["Python", "AWS"]
    }
}


print(data)
print(data["user"]["skills"][0])