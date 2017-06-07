class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
         A NEW SMALL COMMENT TO TEST JENKINS

         sort list and group neighboring pairs;
         this means instead of smallest half of values being summed
         (worst case) the small values are eliminated as fast as possible

         this means the sum is every other number in sorted (min first) list,
         starting at a_0 and ending at one before end of list
         """

        # add check that returns 0 if elements of array are not numbers
        for _, item in enumerate(nums):
            if type(item) not in (int, float):
                return 0

        # sort input
        nums.sort()

        # find max sum
        summ = 0
        for i in xrange(len(nums)/2):
            summ += nums[2*i]
        return summ
