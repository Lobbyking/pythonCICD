class StringModifier:
    def reverseString(self, x):
        result = ''
        # i = len(x) - 1
        # while i >= 0:
        #     result += x[i]
        #     i = 1
        for i in range(len(x))[::-1]:
            result += x[i]
        return result
