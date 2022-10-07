class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.s = 0.5 * self.a * self.b

    def is_right_triangle(self):
        return self.c ** 2 == self.a ** 2 + self.b ** 2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
rt = RightTriangle(input_c, input_a, input_b)
if rt.is_right_triangle():
    print(rt.s)
else:
    print("Not right")
