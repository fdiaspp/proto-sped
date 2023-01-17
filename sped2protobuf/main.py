import sys
from typing import Dict

sys.path.append("../target/python")
import sped_pb2


class Sped:
    
    def __init__(self):
        self.data = sped_pb2.SPED()
        
    def add(self, message):
        block_number = message.REG[0]
        register_number = message.REG[1:]       
        getattr(getattr(self.data, f"B{block_number}"), f"R{register_number}").extend([message])


def get_register_type(line: str):
    register_code = line[0:4]                
    return getattr(sped_pb2, f"R{register_code}")     


def get_message_schema(message_type):
    return [field for field in message_type.DESCRIPTOR.fields_by_name]


def process_line(line: str, message_schema: list):
    data = line.split("|")
    zipped_data = dict(zip(message_schema, data[:-1]))
    return zipped_data


def main(path):    
    with open(path) as file:                
        while True:
            line = file.readline()   
            
            if not line:
                break

            message_type = get_register_type(line)
            message_schema = get_message_schema(message_type)
            data = process_line(line, message_schema)
            yield message_type(**data) 

               
if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("É necessário especificar pelo menos um arquivo txt para processamento")
        exit(1)
    
    paths = sys.argv[1:]
    sped = Sped()
    
    for path in paths:        
        for message in main(path):            
            sped.add(message)
                
    print(sped.data)
                