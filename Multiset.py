from operator import contains


class Multiset:
    def __init__(self):
        self.data = []
        
    def add(self, val):
        self.data.append(val)

    def remove(self, val):
        try:
            self.data.remove(val)
        except:
            pass
        
    def __contains__(self, val):
        if val in self.data:
            return True
        else:
            return False
    
    def __len__(self):
        return (len(self.data))


if __name__ == "__main__":
    data = Multiset()
    data.add(5)
    print(data.__len__())
    data.remove(3)
    print(data.__contains__(5))