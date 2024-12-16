calls = 0

def count_calls():
    global calls
    calls += 1
def string_info(string):
    global calls
    string_info=(len(string), string.upper(), string.lower())
    print(string_info)
    count_calls()
def is_contains(string,list):
    global calls
    string_new=string.lower()
    list_to_search = [string.lower() for string in list]
    if string_new in list_to_search:
        print(True)
    else:
        print(False)
    count_calls()
string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
is_contains('CloN', ['claws', 'CLon'])
is_contains('URban2', ['ban', 'BaNaN', 'urbAN2'])
is_contains('cycle', ['recycling', 'CYCL'])
print(calls)
