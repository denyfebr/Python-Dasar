## Dictionary

# list -> array, mengakses dgn menggunakan index

data_list = ['ucup','otong','dudung']

print(data_list[0])

# dictionary (dict) -> associative array
# identifier -> key

data_dict = {
    'key1':'value1',
    'key2':'value2'
}

print(data_dict)

data_dict_exp = {
    'cp':'ucup',
    'tg':'otong',
    'dg':'udung',
    'nb':100,
    'lst':data_list
}

print(data_dict_exp['cp'])
print(data_dict_exp['tg'])
print(data_dict_exp['nb'])
print(data_dict_exp['lst'])