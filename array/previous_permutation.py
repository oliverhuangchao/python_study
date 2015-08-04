def previousPermuation(self, num):
        # write your code here
        i = len(num)-1
        while i>0 and num[i] >= num[i-1]:
            i -= 1
        if i == 0:
            num.sort(reverse = True)
            return num
        else:
            j = len(num)-1
            while j >= i and num[i-1] <= num[j]:
                j -= 1
            num[i-1],num[j] = num[j],num[i-1]
            num[i:] = sorted(num[i:],reverse=True)
            return num
