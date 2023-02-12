class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, *nums):
        for i in nums:
            self.result += i
        return self

    def subtract(self, *nums):
        for j in nums:
            self.result -= j
        return self


md = MathDojo()
# to test:
x = md. add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5

md = MathDojo()
y = md.add(20, 10).add(5, 2).subtract(7).result
print(y)

md = MathDojo()
z = md.add(100, 150).subtract(50).result
print(z)

md = MathDojo()
u = md.add(10, 20).subtract(50).add(10, 10, 10, 10).subtract(100).result
print(u)
