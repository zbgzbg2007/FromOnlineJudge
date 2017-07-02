class LogSystem(object):

    def __init__(self):
        self.log = []
        self.grad = {'Year': 4, 'Month': 7, 'Day': 10, 'Hour': 13, 'Minute': 16, 'Second': 19}
    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.log.append((id, timestamp))

  
        
    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        ans = []
        g = self.grad[gra]
        for x in self.log:
            if x[1][:g] >= s[:g] and x[1][:g] <= e[:g]:
                ans.append(x[0])
        return ans            
                
            

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
