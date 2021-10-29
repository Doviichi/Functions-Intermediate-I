
# 1
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
students[0]['last_name'] = 'Bryant',
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30



# 2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(students):
    for i in students:
        print(i)
iterateDictionary(students)


# 3
def iterateDictionary2(students):
    for i in students:
        # print(i)
        for o in i.values():
            print(o)

iterateDictionary2(students)


# # 4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def locations(dojo):
    print(len(dojo['locations']))
    for i in dojo['locations']:
        print(i)

def instructors(dojo):
    print(len(dojo['instructors']))
    for i in dojo['instructors']:
        print(i)

locations(dojo)
instructors(dojo)

