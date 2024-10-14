# # EXAMPLE FOR *args
# def countNum(*numbers):
#     for num in numbers:
#         print(f"Count: {num}")
# countNum(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)





# EXAMPLE FOR **kwargs
def show_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
show_details(Name="Alice", Age=30)


def show_keys(**info):
    for key in info.keys():
        print(key)
show_keys(name="Alice", age=30) 


def show_values(**info):
    for value in info.values():
        print(value)
show_values(name="Alice", age=30) 