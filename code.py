from bs4 import BeautifulSoup,SoupStrainer
import random
import re
from prime_numbers import prime
from random_numbers import randomNums
def exercise(k, num, n,doc_id):
    ##Get HTML Body from .sgm files
    text = []
    for i in range(22):
        if i < 10:
            print('reut2-00'+str(i)+'.sgm')
            #to path auto einai to directory, pou exw ta .sgm arxeia
            f = open('C:/Users/User/Desktop/Data Mining/reut2-00'+str(i)+'.sgm', 'r')
            data= f.read()
            soup = BeautifulSoup(data)
            contents = soup.findAll('reuters')
            for reuter in contents:
                text.append(reuter.text)

        else:
            print('reut2-0'+str(i)+'.sgm')
            #to path auto einai to directory, pou exw ta .sgm arxeia
            f = open('C:/Users/User/Desktop/Data Mining/reut2-0'+str(i)+'.sgm', 'r')
            data= f.read()
            soup = BeautifulSoup(data)
            contents = soup.findAll('reuters')
            for reuter in contents:
                text.append(reuter.text)
    print('Ta sunolika documents einai:', len(text))
    ##from documents remove special characters and split each documents to words
    text = [re.sub(r'[^\w]', ' ', elem).lower() for elem in text]
    splited_text = [doc.split() for doc in text]

    ##find shingles per text....we want to split each text's words
    #k = int(input("Enter k: "))
    s_test = []
    shingles = []
    for t in splited_text:
        temp = []
        for i in range(len(t)):
            if i != len(t):
                shingles.append(''.join(t[i:k+i]))
                temp.append(''.join(t[i:k+i]))
        s_test.append(temp)
    number_unique_shingles = len(set(shingles))
    print('To plh8os twn monadikwn k-shingles einai:', number_unique_shingles)
    total_shingles = len(shingles)
    print('To sunoliko plh8os twn k-shingles einai:', total_shingles)
    unique_shingles = set(shingles)
    ##create dictionary, to save unique shingles and create id for these shingles
    shingles_dict = dict()
    shingles_list = list(unique_shingles)
    j = 0
    for item in shingles_list:
        j+=1
        shingles_dict[item] = j
    print('Dhmiourgia dictionary poy exei ws kleidia ta monadika shingles kai ws times ta antistoixa id tous')
    #print(shingles_dict)
    ## With the following code, we will append the shingles id's to documents that have the specific shingles
    s_test_id = []
    for text in s_test:
        temp1 = []
        for sh in text:
            if sh in shingles_dict.keys():
                temp1.append(shingles_dict[sh])
        s_test_id.append(temp1)
    print('Dhmiourgh8hke h lista me tis listes twn ids twn shingles poy periexei ka8e keimeno')
    #print(s_test_id)

    ##maximum shingle id, that was assigned
    maxShingle_id = max(shingles_dict.values())
    ## find nearest prime number (c)
    c = maxShingle_id
    response = False
    while(response == False):
        c = c + 1
        response = prime(c)
    print('The number c for hash function family is :',c)

    ## generate k hash functions
    #num = int(input("Set number of hash functions:  "))
    a = randomNums(num, maxShingle_id)
    b = randomNums(num, maxShingle_id)

    ##test for one document, let it be the first document
    signatures = []
    for doc in s_test_id:
        signature = []
        #for each of the hash functions
        for i in range(0, num):
            #for each of the shingles, calculate it's hash code using i-th hash function
            minHashCode = c + 1
            for shId in doc:
                hashCode = (a[i]*shId + b[i])%c
                # Track the lowest hash code seen.
                if hashCode < minHashCode:
                    minHashCode = hashCode
            signature.append(minHashCode)
        signatures.append(signature)
    print('Oi upografes twn keimenwn dhmiourgh8hkan')
    #print(signatures)
    ##Next step....Find Jaccard Similarities
    ## we return a dictionary, and as key we have the document compared with the selected document, and as value we have
    ##the jaccard similarity of selected document with the other documents
    ## Finaly we return the top n maximum similarities
    #doc_id = int(input("Set document id to check jacard similarities:  "))
    #n = int(input("Set number of closest documents to return:  "))
    doc_sign = signatures[doc_id]
    similarities = dict()
    for l in range(len(signatures)):
        if l == doc_id:
            continue
        else:
            jac_sim = len(set(doc_sign)&set(signatures[l]))/len(doc_sign + signatures[l])
            similarities[str(l)] = jac_sim
    t = sorted(similarities.items(), key=lambda x:-x[1])[:n]
    return t
