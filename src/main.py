# Common-Password-Generation
#Made by jasonfish4

import random
import hashlib
import string
import enchant

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))


def mainroutine(target):
    print('Made by jasonfish4')
    engdict = enchant.Dict("en_US")
    fileb = open("rvpasshash.txt","a+")
    while True:
        randomword0 = randomword(6)
        if engdict.check(randomword0) == True:
            randomkey0 = randomword0+str(random.randint(0,99))
        elif engdict.check(randomword0) == False:
            englist = engdict.suggest(randomword0)
            if len(englist) > 0:
                randomkey0 = englist[0]+str(random.randint(0,99))
            else:
                randomkey0 = randomword0+str(random.randint(0,99))


        
        randomword3 = randomword(5)
        if engdict.check(randomword3) == True:
            randomkey3 = randomword3+str(random.randint(0,99))
        elif engdict.check(randomword3) == False:
            englist = engdict.suggest(randomword3)
            if len(englist) > 0:
                randomkey3 = englist[0]+str(random.randint(0,99))
            else:
                randomkey3 = randomword3+str(random.randint(0,99))


        randomword1 = randomword(7)
        if engdict.check(randomword1) == True:
            randomkey1 = randomword1+str(random.randint(0,99))
        elif engdict.check(randomword1) == False:
            englist = engdict.suggest(randomword1)
            if len(englist) > 0:
                randomkey1 = englist[0]+str(random.randint(0,99))
            else:
                randomkey1 = randomword1+str(random.randint(0,99))


        if 'randomkey0' and 'randomkey3' and 'randomkey1' in locals():
            whasher0 = hashlib.new("md5")
            whasher0.update(randomkey0)
            whasher3 = hashlib.new("md5")
            whasher3.update(randomkey3)
            whasher1 = hashlib.new("md5")
            whasher1.update(randomkey1)
            print(randomkey0+" + "+str(whasher0.hexdigest())+"\n")
            print(randomkey3+" + "+str(whasher3.hexdigest())+"\n")
            print(randomkey1+" + "+str(whasher1.hexdigest())+"\n")
            fileb.write(randomkey0+" + "+str(whasher0.hexdigest())+"\n")
            fileb.write(randomkey3+" + "+str(whasher3.hexdigest())+"\n")
            fileb.write(randomkey1+" + "+str(whasher1.hexdigest())+"\n")
            if (target == str(whasher0.hexdigest()) or target == str(whasher3.hexdigest()) or str(whasher1.hexdigest()))
               return str(whasher0.hexdigest())
            else if (target == str(whasher3.hexdigest())
               return str(whasher3.hexdigest())
            else if (target == str(whasher1.hexdigest())
               return str(whasher1.hexdigest())
            else
               return False
#end
