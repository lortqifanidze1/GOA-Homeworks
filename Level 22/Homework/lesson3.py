def my_function(strings):
    list = []
    for i in strings:
        list.append(len(i))
    return list
result = my_function(["wow", "amigo","shalva magaria"])
print(result)