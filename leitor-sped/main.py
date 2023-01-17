import sys
from typing import Dict

sys.path.append("../target/python")
import sped_pb2


class Sped:
    
    def __init__(self):
        self.data: Dict[str, list] = {}
        
    def add(self, message):
        block = message.REG[0]
        
        if self.data.get(block) is None:
            self.data[block] = [message]
        else:
            self.data[block].append(message)
            

if __name__ == "__main__":
    print(sys.argv)
    
    if len(sys.argv) < 2:
        print("É necessário especificar pelo menos um arquivo txt para processamento")
        exit(1)
    
    paths = sys.argv[1:]
    sped = Sped()
    
    for path in paths:
        
        with open(path) as file:
            
            while True:
                line = file.readline()   
                print(line)             
                
                if not line:
                    break
                
                data = line.split("|")
                register_code = data[0]
                
                message_cls = getattr(sped_pb2, f"R{register_code}")            
                fields = [field for field in message_cls.DESCRIPTOR.fields_by_name]
                zipped_data = dict(zip(fields, data[:-1]))
                message = message_cls(**zipped_data)
                
                sped.add(message)
                
        print(sped.data)
                