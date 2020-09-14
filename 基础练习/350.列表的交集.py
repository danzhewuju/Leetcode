class Solution:
    def intersect(self, nums1, nums2):
        res = []
        for n in nums1:
            if n in nums2:
                res.append(n)
                nums2.remove(n)
        return res


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.intersect([1,2,2,1], [2,2]))
