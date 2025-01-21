import bcrypt

print(bcrypt.hashpw("1234".encode() , bcrypt.gensalt()))

# with open('requirements.txt', 'r') as f:
#     file = f.read().split()
#     print(len(file))