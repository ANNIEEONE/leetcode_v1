class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeBST(nums, 0, len(nums))
    
    def makeBST(self, nums, start, end):
        if start >= end: return None
        return TreeNode(
            val=nums[ (start + end)//2 ],
            left=self.makeBST(nums, start, (start + end)//2),
            right=self.makeBST(nums, 1+((start+end)//2), end)
        )