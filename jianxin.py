class Solution:
    def reverse(self,s):
        l = len(s)
        low, heigh = 0, l - 1
        while low < heigh:
            print(s[low], s[heigh])
            t = s[low]
            s[low] = s[heigh]
            s[heigh] = t
            low += 1
            heigh -= 1
        res = "".join(s)
        return int(res)
    def reversePlus(self , a , b ):
        a_r = self.reverse(list(str(a)))
        b_r = self.reverse(list(str(a)))
        a_max = max(a,a_r)
        b_max = max(b,b_r)
        print(a,a_r,a_max,b,b_r,b_max)
        return a_max+b_max



class Solution:
    def judge(self , root ):
        left = False
        right = True
        if root.left != None and root.right == None:
            return False
        if root.right != None:
            right = self.judge(root.right)
            if root.left != None:
                left = self.judge(root.left)
        if left and right: return True
        else: return False