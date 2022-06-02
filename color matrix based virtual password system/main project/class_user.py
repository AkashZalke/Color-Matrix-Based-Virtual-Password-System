class user:
    
    def __init__(self, username, password):
        self.username = username 
        self.password = password

    def __repr__(self):
        return "user({}, '{}', '{}', '{}', '{}', {}, {})".format(self.username, self.password)