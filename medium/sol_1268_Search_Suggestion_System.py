class Solution:
    #Brute Force
    def suggestedProducts(self, products, searchWord):
        rv = []
        products = sorted(products)
        for i in range(1,len(searchWord)+1):
            r = []
            sub = searchWord[:i]
            for word in products:
                if word.find(sub) == 0:
                    r.append(word)
                if len(r) ==3:
                    break
            rv.append(r)
        return rv


# Binary Search
class Solution2:
    def suggestedProducts(self, products, searchWord):
        def bs(l,r,sub):
            while l < r:
                mid = int((l+r)/2)
                if sub <= products[mid]:
                    r = mid
                else:
                    l = mid+1

            return l

        rv = []
        n = len(products)
        products = sorted(products)
        print(products)
        for i in range(1,len(searchWord) + 1):
            r = []
            sub = searchWord[:i]
            earliest_index = bs(0,n,sub)
            for j in range(earliest_index,min(n, earliest_index+3)):
                if products[j].find(sub) == 0:
                    r.append(products[j])
                else:
                    break
            rv.append(r)
        return rv

            # print(f' word : {sub} earliest index = {earliest_index}')


            

        

if __name__ == "__main__":
    solution = Solution2()
    print(solution.suggestedProducts(products =["bags","baggage","banner","box","cloths"], searchWord = "bags"))
