
class Test:
    def __init__(self, a, b=dict()):
        self.a = a
        self.b = b

tests = []
for i in range(10):
    tests.append(Test(i))

for i in tests:
    print(i.a, i.b)

# Only Change the dictionary in the first element
tests[1].b[0] = "not_default"

# All dictionary changes
for i in tests:
    print(i.a, i.b)