def rob(self, nums: List[int]) -> int:
    if len(nums) < 3:
        return max(nums)

    ans = [0 for _ in nums]
    ans[0] = nums[0]
    ans[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        ans[i] = max(ans[i-1], ans[i-2]+nums[i])

    return ans[-1]
