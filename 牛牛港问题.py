import heapq as hq
class Solution:
    def solve(self , n , k , a , b ):
        # 队列的完成
        info = [(x, y) for x, y in zip(a, b)]
        hq.heapify(info)
        time_info = [0 for i in range(k)] # 完成时间和节点序号
        hq.heapify(time_info)
        max_day = 0
        for i in range(n):
            node = hq.heappop(info)
            star_time = node[0] # 开始时间
            work_time = node[1] # 工作时间
            value = hq.heappop(time_info)
            end_time = max(value+work_time, star_time+work_time)
            max_day = max(max_day, end_time)
            hq.heappush(time_info, end_time)
        return max_day

if __name__ == "__main__":
    Sol= Solution()
    print(Sol.solve(6,1,[4,2,5,3,1,6],[10,10,10,10,10,3]))  

