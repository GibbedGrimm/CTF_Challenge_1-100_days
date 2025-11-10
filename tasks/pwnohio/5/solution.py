from itertools import product
first_cub = '5462a347303b36765550668276ff056573505f07c9566439070d35'
second_cub = '635272b57d6078355563666433f5007c35656750594743f00a690f'
third_cub = '5264a206393d36f65640578377550535646f6000c935b57567703f'
fourth_cub = '624374d67079687556b36362335660fc337f50505956040f7a5505'
change = {}
tru = '754477f367633676ef02347641d63d65529663b6007360f40f0ebe'
for i in range(len(first_cub)):
    arr = []
    for j in range(len(first_cub)):
        if first_cub[i] == second_cub[j] and second_cub[i] == third_cub[j] and third_cub[i] == fourth_cub[j]:
           arr.append(j)
    change[i] = arr
    print(arr)
print(change)
word = ''
for i in change:
    print(change[i])
    word += first_cub[change[i][-1]]
print(bytes.fromhex(word))

options = [change[i] for i in range(len(first_cub))]

# product даст все комбинации: один элемент из каждого списка
for combo in product(*options):
    # combo — это кортеж индексов для каждого элемента first_cub
    word = ''.join(tru[i] for i in combo)
    try:
        decoded = bytes.fromhex(word)
        print(decoded)
    except ValueError:
        # невалидный hex, пропускаем
        pass