class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes = sorted(boxTypes,key = lambda x :x[1], reverse = True)
        amount = 0
        for num_boxes, units_per_box in boxTypes:
            boxes_to_pack = min(truckSize,num_boxes)
            amount += boxes_to_pack*units_per_box
            truckSize -= boxes_to_pack
            if truckSize == 0:
                break
        return amount








if __name__ == '__main__':
    print(Solution().maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))