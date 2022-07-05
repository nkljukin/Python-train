
# Online Python - IDE, Editor, Compiler, Interpreter

def Relu(x):
    return x if x > 0 else 0

class Neiron:
    def __init__(self, new_x, new_w, new_w0):
        self.x = new_x
        self.w = new_w
        self.w0 = new_w0

    def output(self):
        s = 0
        for i in range(len(self.x)):
            s += self.x[i] * self.w[i]
        return Relu(s + self.w0)


n1 = Neiron([2], [1], 1)
n2 = Neiron([2], [2], -5)
n3 = Neiron([n1.output(), n2.output()], [-2, 4], 10)
print(n3.output())