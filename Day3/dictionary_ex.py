print('Dictionary Example')
our_dictionary=[
    {"id":'1',"name":'ali',"age":'35'},
    {"id":'2',"name":'abu',"age":'30'},
    {"id":'3',"name":'siti',"age":'25'},
    {"id":'4',"name":'nani',"age":'31'},
    ]

for k in our_dictionary:
    print(k['id']+'->'+k['name']+'->'+k['age'])