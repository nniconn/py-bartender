

questions = {"strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {"strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


# for k,v in questions.items():
    # print(v)
    # my_input=input("yes or no:  ")
    # print(my_input)
    

# def get_bool(prompt):
#     while True: 
#         try:
#           return {"true":True, "false":False}[input(prompt).lower()]
#         except KeyError:
#             print("Invalid input, please Enter true or false.")
            
#     print get_bool ("Do ye like yer drinks strong?")





# for key in questions:
#     print (questions[key])



# for key in questions:
#     response = False if input("Yes or No:  ").lower() == 'no' else True
#     print (response(questions[key]))




# def drink(questions, default="no"):
#     input = {"yes": True, "or" "no": False}
# while True:
#     for key in questions:
#         print(questions[key]), input("yes or no : ")



for key in questions:
    print(questions[key]), input("yes or no : ")
