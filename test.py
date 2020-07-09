from test_functions import max_for_dicts, filter_dicts

# numbers = [1, 2, 6, 3, 23, 34, 12, 2, 3, 9]
# print(max(numbers))

messages = [
    {'name': 'Jack', 'time': 10, 'text': '123'},
    {'name': 'Jack', 'time': 20, 'text': '1234'},
    {'name': 'Jack', 'time': 30, 'text': '1235'},
    {'name': 'Jack', 'time': 40, 'text': '1236'},
    {'name': 'Jack', 'time': 50, 'text': '1237'}
]

print(max_for_dicts([], key='time'))
print(max_for_dicts(messages, key='time'))

print(filter_dicts([], key='time', min_value=30))
print(filter_dicts(messages, key='time', min_value=30))
