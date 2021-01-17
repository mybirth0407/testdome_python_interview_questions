from collections import deque

class TrainComposition:
    
    def __init__(self):
        self.train = deque()
    
    def attach_wagon_from_left(self, wagonId):
        self.train.appendleft(wagonId)
    
    def attach_wagon_from_right(self, wagonId):
        self.train.append(wagonId)

    def detach_wagon_from_left(self):
        return self.train.popleft()
    
    def detach_wagon_from_right(self):
        return self.train.pop()

if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right()) # should print 7
    print(train.detach_wagon_from_left()) # should print 13