class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.face = 'East'



    def step(self, num: int) -> None:
        for i in range(num):
            if self.face == 'East':
                if  self.x < self.width -1 :
                    self.x +=1
                else:
                    self.face = 'North'
                    self.y +=1

            elif self.face == 'North':
                if self.y < self.height -1 :
                    self.y +=1
                else:
                    self.face = 'West'
                    self.x -=1
            elif self.face == 'West':
                if self.x -1 >= 0:
                    self.x -=1
                else:
                    self.face = 'South'
                    self.y -=1
            elif self.face == 'South':
                if self.y  >0:
                    self.y -=1
                else:
                    self.face = 'East'
                    self.x +=1

        

    def getPos(self) -> List[int]:
        return [self.x , self.y]
        

    def getDir(self) -> str:
        return self.face
        
