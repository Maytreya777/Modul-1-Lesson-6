immutable_var = 1,2,3.2,False, 'string',[7,8,True]
print(immutable_var) # (1, 2, 3.2, False, 'string', [7, 8, True])
# immutable_var[1] = 500
# print(immutable_var) # Ошибка
# нельзя изменить элементы, потому что КОРТЕЖ - НЕИЗМЕНЯЕМЫЙ

# Но мы можем изменить элементы внутри списка, который входит в кортеж:
mmutable_var[-1][-1] = 1000
print(immutable_var) # (1, 2, 3.2, False, 'string', [7, 8, 1000])


mutable_list= [1,2,3.2,False, 'string',[7,8,True]]
print(mutable_list) # [1, 2, 3.2, False, 'string', [7, 8, True]]
mutable_list[1] = 500
print(mutable_list) # [1, 500, 3.2, False, 'string', [7, 8, True]]