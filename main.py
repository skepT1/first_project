lst = ['1', '2', '3']
int_lst = []
for number in lst:
    int_lst.append(int(number))
    print(lst)
    print(int_lst)



 gen_lst = [int(number) for number in lst]
map_lst = map(int, lst)
print(list(map_lst))
---------------------------------------------
names = ['dior', 'sanjar', 'muhammad']

map_names = map(str.capitalize, names)
print(names)
print(list(map_names))
------------------------------------------------
def double_number(number: int):
    return number ** 2
lst = [23, 42, 55, 52, 63]

map_lst = map(double_number, lst)
print(list(map_lst))
------------------------------------------------------


less_five = []
more_five = []
for word in words:
    if len(word) <= 5:
        less_five.append(word)
    else:
        more_five.append(word)
print(less_five)
print(more_five)

words = ['banana', 'yellow', 'orange', 'windows',
         'linux', 'trans', 'black', 'cocaine']
def get_words_less_five(word: str):
    return len(word) <= 5
filter_lst = filter(get_words_less_five, words)
print(list(filter_lst))




words = ['apple' 'align' 'alive' 'after' 'assembler' 'application'
         'byd' 'bmw' 'brain' 'brabus' 'brazil' 'bentley']

def get_words_with_a(word: str):
   return word.startswith('a')
filtered = filter(get_words_with_a, words)
print(list(filtered))


