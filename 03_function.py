#function
# user define function, build in function

# def camelCase( age = 0, *name):
#     # print("my name is Shisir")
#     return f"my name is {name} and my age is {age}"

# print(camelCase( 28, 'SHISHIR', 'hari', 'laxman', 'ram'))
# print(camelCase( "sita"))

#paratmeter Type 
# Positional Parameter
# Keyword parameter
# Default Parameter
# Args parameter *
# kargs Parameter **

# name = "shsihir"
# age = 28,
# gender  = "male"

def Kwargs(**nam):
    for keys, values in nam.items():
        print(f"{keys} : {values}")

Kwargs( names = 'SHISHIR', lastname = 'bhandari', age = '28')




    


