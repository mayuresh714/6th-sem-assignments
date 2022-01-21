import os
import time
import magic
 

class Filemanager:

    def __init__(self,path = "C:/users/hp/desktop/"):
        self.path = path
        self.graph = {}

    def DFS_method(self,path, graph = {}):  ## use DFS recursion
        lis_of_dirs = os.listdir(path)
        for single in lis_of_dirs:
            fpath = path + "/" + single 
            #print(fpath)
            if os.path.isdir(fpath):
                graph[single] = self.DFS_method((fpath),{})
            elif os.path.isfile(fpath):
                graph[single] = self.get_file_metadata(fpath)
        return  graph


    def get_file_tree(self,by_dfs = 1):
        if by_dfs:
            self.graph = self.DFS_method(self.path,{})
            return {self.path:self.graph}


    def get_file_metadata(self, filename):#, metadata):
        if "." in filename:
            x = filename.split(".")[-1]
        else:
            x = filename
        metadata =   {
            'Access_time'  : time.ctime(os.path.getatime(filename)),
            'Modified_time': time.ctime(os.path.getmtime(filename)),
            'Change_time'  : time.ctime(os.path.getctime(filename)),
            'Size'         : os.path.getsize(filename) ,
            'type'         : x
        }
        return metadata
        

if __name__ == "__main__":
    mng = Filemanager()
    print(mng.get_file_tree())