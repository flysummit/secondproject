# 实现一个特殊的栈,在实现栈的基本功能的基础上,再实现返回栈中最小元素的操作
class NewStack1():
    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self, newNum):
        self.stackData.append(newNum)
        if len(self.stackMin) == 0 or newNum <= self.getMin():
            self.stackMin.append(newNum)

    def pop(self):
        if len(self.stackData) == 0:
            raise Exception('stack is empty!')
        value = self.stackData.pop()
        if self.getMin() == value:
            self.stackMin.pop()
            return value

    def getMin(self):
        if len(self.stackMin) == 0:
            raise Exception('stack is empty!')
        return self.stackMin[-1]


newstack = NewStack1()
newstack.push(2)
newstack.push(1)
newstack.push(3)
newstack.push(4)
newstack.push(1)
newstack.push(5)
print(newstack.pop())
print(newstack.getMin())
print(newstack.stackData)
print(newstack.stackMin)
