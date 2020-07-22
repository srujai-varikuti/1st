class computer:
    def __init__(self,cpu,ram,processor):
        self.cpu = cpu
        self.ram = ram
        self.processor = processor

    def config(self):
        print("Config is", self.cpu, self.processor, self.ram)

com1 = computer ('i3', 4, 'intel')
com2 = computer ('i5', 6, 'amd')
com3 = computer ('i7', 8, 'iOs')

com1.config()
com2.config()
com3.config()