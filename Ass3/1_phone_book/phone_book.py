#python3

class phonebook:
    def __init__(self):
        self.input = 0
        self.queries = []
        self.pbook = [None]*(10**7)#phone num with 7 digits
    
    def add(self, number, name):
        self.pbook[number] = name
    
    def delete(self, number):
        self.pbook[number] = None
    
    def find(self, number):
        name = self.pbook[number]
        if name == None:
            return 'not found'
        else:
            return name
    
    #input queries processing
    def inputprocess(self):
        self.input = int(input())
        self.queries = [input() for element in range(self.input)]
        self.processq()
    
    #query individully processing
    def processq(self):
        for query in self.queries:
            ele = query.split()
            instruct, num = ele[0], int(ele[1])
            if instruct == 'add':
                self.add(num, ele[2])
            elif instruct == 'del':
                self.delete(num)
            elif instruct == 'find':
                print(self.find(num))



if __name__ == '__main__':
    a = phonebook()
    a.inputprocess()
