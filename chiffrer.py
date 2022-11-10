from cryptography.fernet import Fernet

#generation de la clef
key = Fernet.generate_key()

#assignation à une variable
f = Fernet(key)

#le texte en clair est converti en texte chiffré
token = f.encrypt("salut les copains")


print(token)

## déchiffrer le texte chiffré
d = f.decrypt(token)


print(d.decode())