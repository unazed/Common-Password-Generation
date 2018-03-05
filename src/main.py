# Common-Password-Generation
# Made by jasonfish4
# Password Generation Algorithm

import random #.h
import hashlib #.h
import string #.h
import enchant #.h


EXIT_FAILURE = 1


def\
randomword (length):
   return ''.join (random.choice (string.lowercase) for i in range (length))


def\
mainroutine (target):
    print ("Made by jasonfish4")
    engdict = enchant.Dict ("en_US")
    fileb = open ("rvpasshash.txt", "a+")
      
    while 1:
        randomword0 = randomword (6)
         
        if engdict.check (randomword0):
            randomkey0 = randomword0 + str (random.randint(0, 99))
        elif not engdict.check (randomword0):
            englist = engdict.suggest (randomword0)
            if englist:
                randomkey0 = englist[0] + str (random.randint (0, 99))
            else:
                randomkey0 = randomword0 + str (random.randint (0, 99))
        
        randomword3 = randomword (5)
        if engdict.check (randomword3):
            randomkey3 = randomword3 + str (random.randint (0, 99))
        elif not engdict.check (randomword3):
            englist = engdict.suggest (randomword3)
            
            if englist:
                randomkey3 = englist[0] + str (random.randint (0, 99))
            else:
                randomkey3 = randomword3 + str (random.randint (0, 99))


        randomword1 = randomword (7)
        if engdict.check (randomword1):
            randomkey1 = randomword1 + str (random.randint (0, 99))
        elif not engdict.check (randomword1):
            englist = engdict.suggest (randomword1)
            if englist:
                randomkey1 = englist[0] + str (random.randint (0, 99))
            else:
                randomkey1 = randomword1 + str (random.randint (0, 99))


        if 'randomkey0' and 'randomkey3' and 'randomkey1' in locals ():
            whasher0 = hashlib.new ("md5")
            whasher0.update (randomkey0)
            
            whasher3 = hashlib.new ("md5")
            whasher3.update (randomkey3)
            
            whasher1 = hashlib.new ("md5")
            whasher1.update (randomkey1)
            
            print ("%s + %s\n" % (randomkey0, whasher0.hexdigest ()))
            print ("%s + %s\n" % (randomkey3, whasher3.hexdigest ()))
            print ("%s + %s\n" % (randomkey1, whasher1.hexdigest ()))
            
            fileb.write ("%s + %s\n" % (randomkey0, whasher0.hexdigest ()))
            fileb.write ("%s + %s\n" % (randomkey3, whasher3.hexdigest ()))
            fileb.write ("%s + %s\n" % (randomkey1, whasher1.hexdigest ()))
            
            if target == whasher0.hexdigest ()\
                         or target == whasher3.hexdigest ()\
                         or whasher1.hexdigest ():
               return whasher0.hexdigest ()
            elif target == whasher3.hexdigest ():
               return whasher3.hexdigest ()
            elif target == whasher1.hexdigest ():
               return whasher1.hexdigest ()
            return EXIT_FAILURE
