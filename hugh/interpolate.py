class Solution:
    def bs(self,val,arr):
        l, r = 0, len(arr)
        while l < r:
            mid = int((l + r)/2)
            if val == arr[mid]:
                return mid
            if val < arr[mid]:
                r = mid
            if val > arr[mid]:
                l = mid + 1
        return None

    def interpolate(self,n, instance, price):
        if n < instance[0]:
            m = (price[1] - price[0])/(instance[1] - instance[0])
            b = price[0] - m*instance[0]
            return round(m*n + b,2)
        if n > instance[-1]:
            m = (price[-1] - price[-2])/(instance[-1] - instance[-2])
            b = price[-1] - m*instance[-1]
            return round(m*n + b,2)

        index = self.bs(n,instance)
        if index:
            return round(price[index],2)


        for i in range(len(instance)-1):
            if instance[i] < n < instance[i+1]:
                break

        m = (price[i+1] - price[i])/(instance[i+1] - instance[i])
        return round(price[i] + (n-instance[i])*m,2)







if __name__ == '__main__':
    print(Solution().interpolate(40, [5,10,25,50,100,500],[5,17.0,18.0,20.0,22.0,29.15]))


