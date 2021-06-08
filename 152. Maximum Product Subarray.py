'''
本題為找出乘積最大的連續子數字串值，解題重要思路如下:
***(1) 首先要注意到數字串中可能有0的出現
***(2) 對於一個沒有0的子數字串，若負數的個數為奇數個，則我們必須考慮從第一個負數出現之後的數字乘積(n2)，
    以及最後一個負數出現之前的所有數字乘積(n1)，的大小，也就是說我們必須強迫子數字串中所有負數的個數為偶數。
    自然地，如果子數字串中的負數個數已經是偶數了，那麼成出來的值肯定是正數且為最大值
(a) 因為我們不知道是否有0存在數列中，因此我們採用分割式作法解題，降低疊帶次數；首先我們由起始點(i = 0)開始往後找，
(b) 先判斷該數列中第一個不等於0的位置(i0)，接者馬上由該點往下搜索出第一次出現0的位置(in0)，到此為止我們已經切割
    出第一段子數列，其中沒有出現0，到此為止我們已經把問題轉換成***(2)可以處理的狀況了，接著回傳該子數列中乘積
    最大的值存入product中，並更新搜索下一個不等於0的位置的起始點(i = i0 + 1)重複(b)直到i大於數列總長為止
(c) 結束(b)後我們先確保該數列中是否有0出現(self.zeroflag)，如果有，則必須在product中再加上一個0以防止所有非0
    的子數字串得到的的最大乘積都為負值時，回傳值有誤(此時應回傳0)
***事實上(c)遇到的情況會發生在1.第一個出現非0的位置與該位置之後第一個出現0的位置相差為1時會發生(因為計算子字串
   最大乘積時是用除法來逆推的，這會造成如[-1,0,-2,0]這種情況得到的最大乘積由負轉正，因此遇到(i0 - in0 == 1)的
   情況不會進行逆推判斷(self.calculateSegmentMaxProduct)，反正只有一個元素值而已。2.數列中只有一個數字切該數字
   不是0，ex:[-2]。其餘的所有狀況都不需要額外加0來逼使最大值被判定為負的情況，因為如果字樹列中負數個數為3,5,7...
   都可以刪掉一個負數始乘積轉正
'''


class Solution:
    def findFirstZero(self,nums,start,end):
        for i in range(start,end):            
            if nums[i] == 0:
                self.zeroflag = True # 防止nums = [-2]這種只有一個負的狀況
                return i
        return end  # 如果在第一個非0值出現後找不到0，代表到數列尾部都是非0值了(此時回傳總長度方便之後計算)
    def findFirstNonZero(self,nums,start,end):
        for i in range(start,end):
            if nums[i] != 0:
                return i
        return -1
    def calculateSegmentMaxProduct(self,nums,i_n,p,i0,in0):
        if len(i_n) % 2 == 1:
            n1,n2 = p,p
            for n in nums[i_n[-1]:i0]:
                n1 = n1 // n
            if i_n[0] == in0:
                n2 = n2 // nums[in0]
            else:
                for n in nums[in0:i_n[0] + 1]:
                    n2 = n2 // n
            return max(n1,n2)
        else:
            return p    
    def maxProduct(self, nums) -> int:
        i,self.zeroflag = 0,False
        product = []
        while i < (l := len(nums)):
            in0 = self.findFirstNonZero(nums,start = i,end = l)
            if in0 == -1: # 代表之後都是0，不需要再判斷子數字串，直接跳出
                self.zeroflag = True
                break
            i0 = self.findFirstZero(nums,start = in0,end = l) # 如果i_0是l的話代表直到最後都沒有0出現，直接進for迴圈判斷即可
            #print(i0,in0)
            p,i_n = 1,[]
            for j in range(in0,i0):
                if nums[j] < 0:
                    i_n += [j]
                p *= nums[j]
            (p := self.calculateSegmentMaxProduct(nums,i_n,p,i0,in0)) if i0 - in0 != 1 else p
            product += [p]
            i = i0 + 1
        product += [0] if self.zeroflag else product
        return max(product)  # 0防止在array中有0的情況下，各subarray的最大值都小於0造成的誤判

testcase = [[2,3,-2,4],
             [-2,0,-1],
             [-2],
             [0]]
test = Solution()
for s in testcase:
    print('max product of  subarray is',test.maxProduct(s))

