my_dict ={}

my_dic = {
    1: 'apple',
    2: 'ball'
}

my_dict = {
          'name': 'John',
          1: [2,4,3],
          'age' : 25
    }

print(my_dict['name'])
print(my_dict.get('age'))
print()

my_dict['age'] = 30
print(my_dict)
print()

my_dict['address'] = 'Downtown'
print(my_dict)
print()

my_dict.pop('age')
print(my_dict)