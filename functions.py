# 1.Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15
print(x)
students[0]['last_name'] = "Bryant"
print(students)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z[0]['y'] = 30
print(z)


# 2.Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_Dictionary(list):
  for i in range(0, len(list)):
    output = ""
    for key,val in list[i].items():
      output += f"  {key} - {val}"
    print(output)

iterate_Dictionary(students) 

# 3.Get Values From a List of Dictionaries

def iterate_Dictionary2(key_name,list):
  for i in range(0, len(list)):
    for key,val in list[i].items():
      if key == key_name:
        print(val)

iterate_Dictionary2('first_name', students) 
iterate_Dictionary2('last_name', students) 


# 4.Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dict):
  for key,val in dict.items():
    print(f"{len(val)} {key.upper()}")
    for i in range(0, len(val)):
      print(val[i])

print_info(dojo)


