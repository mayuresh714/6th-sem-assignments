 
## job scheduling done on march 4 2022
class Solution:
    def JobScheduling(self,jobs,n):
        
        max_l, total_jobs,total_profits = -1 , 0 , 0
        '''
        ## bubble sorting according to the profits made
        for i in range(n):
            for j in range(0, n-i-1):
                if jobs[j].profit < jobs[j+1].profit :
                    jobs[j], jobs[j+1] = jobs[j+1], jobs[j]
        '''
        jobs = sorted(jobs, key=lambda x: x.profit, reverse=True)

        max_l = -1
        for i in jobs:
            max_l  = max(max_l , i.deadline )
        
        slots = [0] * max_l
        
        cnt  = 0
        
        while cnt < n:
            ind = jobs[cnt].deadline - 1
            while ind >= 0 and slots[ind] != 0:
                ind -= 1
            if ind != -1:
                slots[ind] = jobs[cnt]
                total_jobs += 1
                total_profits += jobs[cnt].profit
            cnt += 1

        return [ total_jobs , total_profits ] 
 
class Job:
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
 
