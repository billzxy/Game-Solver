"""

"""
import math
import random


ALOC = [1, 3]
BLOC = [2, 3]
CLOC = [3, 3]
DLOC = [1, 2]
ELOC = [2, 2]
FLOC = [3, 2]
GLOC = [1, 1]
HLOC = [2, 1]
ILOC = [3, 1]

def calcDist(begin, end):
    return math.sqrt((end[0]-begin[0])**2 + (end[1]-begin[1])**2)



class Unlock(  object ):
    #ctor:
    def __init__(self, start, finish, key, trial=0):
        #members:
        self.__correct = False
        self.__key = key
        self.__trial = trial
        self.__model = {'A':{"loc":ALOC, "chosen":0, "include":[2,3,4,5,6,7,8]},
                        'B':{"loc":BLOC, "chosen":0,"include":[2,3,4,5,6,7,8]},
                        'C':{"loc":CLOC, "chosen":0,"include":[2,3,4,5,6,7,8]},
                        'D':{"loc":DLOC, "chosen":0,"include":[2,3,4,5,6,7,8]},
                        'E':{"loc":ELOC, "chosen":0,"include":[2,3,4,5,6,7,8]},
                        'F':{"loc":FLOC, "chosen":0,"include":[2,3,4,5,6,7,8]},
                        'G':{"loc":GLOC, "chosen":0,"include":[2,3,4,5,6,7,8]},
                        'H':{"loc":HLOC, "chosen":0,"include":[2,3,4,5,6,7,8]},
                        'I':{"loc":ILOC, "chosen":0,"include":[2,3,4,5,6,7,8]},
                        }
        self.__recycle = []
        self.__left = [2,3,4,5,6,7,8]
        self.__current = []
        self.__model[start]["chosen"]=1
        self.__model[finish]["chosen"]=9
        self.__start = start
        self.__finish = finish

    #methods:
    def calcDist(self, begin, end):
        return math.sqrt((end[0]-begin[0])**2 + (end[1]-begin[1])**2)
    
    def whatsLeft(self):
        listy = []
        for letter in self.__model:
            if(self.__model[letter]["chosen"]==0 or self.__model[letter]["chosen"] in self.__left):
                listy.append(letter)
        return listy

        
    
    def choose(self, letter, number):
        self.__model[letter]["chosen"]=number
        self.__recycle.append(self.__left.pop(self.__left.index(number)))
        
    def tryOnce(self):#implement as random chosen
        listy = self.whatsLeft()
        for letter in listy:
            commonList = list(set(self.__model[letter]["include"]).intersection(self.__left))
            try:
                number = commonList[random.randint(0,len(commonList)-1)]
            except ValueError:
                return -1
            self.choose(letter, number)
        self.__trial += 1
        self.__current=[]
        for letter in ["A","B","C","D","E","F","G","H","I"]:
            self.__current.append( self.__model[letter]["chosen"])
        return 0
        
    def testCorrectness(self):
        if(self.__key==self.__current):
            self.__correct = True
        else:
            listy = ["A","B","C","D","E","F","G","H","I"]
            listy.remove(self.__start)
            listy.remove(self.__finish)
            
            for letter in listy:
                ind = ord(letter)-65
                if( self.__key[ind]!= self.__current[ind] ):
                    self.__left.append(self.__recycle.pop(self.__recycle.index( self.__current[ind] )))
                    self.__model[letter]["include"].remove(self.__current[ind])
                
                    
    def printResult(self):
        print "Trial: ",self.__trial
        print "Current: ",self.__current
        

    def solve(self):
        result = self.tryOnce()
        if (result==-1):
            return -1, self.__trial
        self.testCorrectness()
        #self.printResult()
        while(not self.__correct):
            result = self.tryOnce()
            if (result==-1):
                return -1, self.__trial
            self.testCorrectness()
            #self.printResult()
        #print "Total trials: ",self.__trial
        return 0,self.__trial

        
def main():
    key = [6,1,4,8,9,7,3,5,2]
    begin = "B"
    end = "E"
    game = Unlock(begin, end, key)
    result, failedTrials = game.solve()
    while(result==-1):
            #print "Error occured, trials still counting"
            game = Unlock(begin, end, key, failedTrials)
            result, failedTrials = game.solve()
    return failedTrials

counter = 0
for i in range(0,100):
    counter+=main()
print "Average out of 100: ", counter/100
