# singleton class
 #check if instance of class exists, if not, then create instance
 
 
 
class CredentialManager:
    instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
                cls.instance =  super().__new__(cls, *args, **kwargs)
                return cls.instance
        else:
            return cls.instance
        

c = CredentialManager()
print(c)
c = CredentialManager()
print(c)
