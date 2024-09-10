class Operations:

    def perform_add(self,*args):

        total=sum([arg for arg in args if isinstance(arg,(int,float))])

        return total
    
    def get_max_num(self,*args):

         return max(args)
    
math = Operations

print(math.perform_add(10,20))

print(math.perform_add(10,20,30,77.9))