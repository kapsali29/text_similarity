from code import exercise

k = int(input("Enter k: "))
num = int(input("Set number of hash functions:  "))
doc_id = int(input("Set document id to check jacard similarities:  "))
n = int(input("Set number of closest documents to return:  "))
returned = exercise(k, num, n,doc_id)
print(returned)
