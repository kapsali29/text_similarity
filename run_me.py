from code import exercise
import matplotlib.pyplot as plt

ks = [1,2,3,4,5]
num_h = [10,50,100,150]
for i in range(len(ks)):
    for j in range(len(num_h)):
        returned = exercise(ks[i], num_h[j], 100,4)
        returned = dict(returned)
        plt.bar(range(len(returned)), returned.values(), align='center')
        plt.title('k='+str(ks[i])+' ' +'number of hash functions='+str(num_h[j]))
        print(returned)
        ##Close image to continue the process
        plt.show()
