
# standard int hash
# these hashes only remain consistent until program ends
# i.e their values are different each time program runs
# but can still be used to compare data of different types

print(hash("Hello World"))

x = "Hello World"
print(hash(x))

y = hash("Hello World")
print(y)

# use algorithms
# these hashes will always be the same

import hashlib

hash_object_md5 = hashlib.md5(b'Hello World')
hash_object_sha1 = hashlib.sha1(b'Hello World')
hash_object_sha224 = hashlib.sha224(b'Hello World')
hash_object_sha256 = hashlib.sha256(b'Hello World')
hash_object_sha384 = hashlib.sha384(b'Hello World')
hash_object_sha512 = hashlib.sha512(b'Hello World')

print("md5: ", hash_object_md5.hexdigest())
print("sha1: ", hash_object_sha1.hexdigest())
print("sha224: ", hash_object_sha224.hexdigest())
print("sha256: ", hash_object_sha256.hexdigest())
print("sha384: ", hash_object_sha384.hexdigest())
print("sha512: ", hash_object_sha512.hexdigest())
