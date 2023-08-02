class Test_Credence_001:

    def test_mul_009(self):
        a = 3
        b = 7
        mul = a * b
        print("Mul of a and b is :" + str(mul))
        if mul == 21:
            assert True
        else:
            assert False

    def test_sum_001(self):
        a = 8
        b = 7
        sum = a + b
        print("sum of a and b is :" + str(sum))
        if sum == 15:
            assert True
        else:
            assert False