class node(object):
        def __init__(self, name, s=''):
            self.child = []
            self.name = name
            self.content = s
class FileSystem(object):
    
    def __init__(self):
        self.root = node('')
  
    def search(self, path):
    ''' search given path, and build node if needed
        return the last node
    '''
        f = self.root
        for name in path.split('/'):
            if name == '': continue
            flag = False
            for x in f.child:
                if x.name == name:
                    flag = True
                    f = x
                    break
            if flag == False:
                f.child.append(node(name))
                f = f.child[-1]
        return f
        
    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        ans = []
        if path == '/':
            for x in self.root.child:
                ans.append(x.name)
            return sorted(ans)
        f = self.search(path)
        if f.content != '':
            ans.append(f.name)
            return sorted(ans)
        for x in f.child:
            ans.append(x.name)
        return sorted(ans)

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        self.search(path)

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        f = self.search(filePath)
        f.content += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        f = self.search(filePath)
        return f.content
                


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
