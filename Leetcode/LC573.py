class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        num_nuts = len(nuts)
        ds = [abs(squirrel[0]-nuts[i][0])+abs(squirrel[1]-nuts[i][1]) for i in range(num_nuts)]
        dtree = [abs(tree[0]-nuts[i][0])+abs(tree[1]-nuts[i][1]) for i in range(num_nuts)]
        ans = sum(dtree)*2
        distance = [ans-dtree[i]+ds[i] for i in range(num_nuts)]
        return min(distance)
        
