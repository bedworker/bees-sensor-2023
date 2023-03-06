from colors import color
print(type(color('test', fg=100)))
string = ''
for i in range(256):
    string += color('█', fg=i)
print(string)
