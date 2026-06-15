class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0;
        end = len(numbers) - 1;
        while (front != end):
            sum = numbers[front] + numbers[end];
            if (sum > target):
                end -= 1;
            elif (sum < target):
                front += 1;
            else:
                return [front + 1, end + 1];
        return []
