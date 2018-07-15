class Solution:
    
    def binary_search(self, num, a):
        start = 0
        end = len(a) - 1
        print(num, a)
        while start <= end:
            mid = start + (end - start) // 2
            print(start,mid,end, a[mid])
            if a[mid] <= num:
                if mid + 1 >= len(a) or a[mid+1] > num:
                    return mid + 1
                start = mid + 1
            elif a[mid] > num:
                if mid - 1 < 0 or a[mid-1] <= num:
                    return mid
                end = mid - 1
        # print("error")
        return False
                
                
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        
        a = sorted(A)
        i = 0
        b = []
        for i in range(len(B)):
            b.append([B[i], i])
        b = sorted(b, key= lambda x: x[0])
        print(b)
        
        ans = []
        search_array = a
        
        for num, _ in b:
            index = self.binary_search(num, search_array)
            if index == len(search_array):
                break
            else:
                ans.append(search_array[index])
                search_array.pop(index)
            print(ans)
            
        print("search_array", search_array)
        ans += search_array
        final = []
        for i in range(len(b)):
            final.append([ans[i],b[i][1]])
        print("Final",final)
        final = sorted(final, key=lambda x: x[1])
        return [i[0] for i in final]

print(Solution().advantageCount([2,7,11,15], [1,10,4,11]))