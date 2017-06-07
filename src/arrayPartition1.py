class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # A NEW SMALL COMMENT TO TEST JENKINS

        # sort list and group neighboring pairs;
        # this means instead of smallest half of values being summed
        # (worst case) the small values are eliminated as fast as possible

        # this means the sum is every other number in sorted (min first) list,
        # starting at a_0 and ending at one before end of list

        # sort input
        nums.sort()

        # find max sum
        summ = 0
        for i in xrange(len(nums)/2):
            summ += nums[2*i]
        return summ
