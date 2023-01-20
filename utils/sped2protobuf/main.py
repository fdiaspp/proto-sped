import sys
import pathlib


if not pathlib.Path("../../target/python/sped_pb2.py").exists():
    print("Protobuf schema não compilado na versão Python.\n"
           "Na raiz do projeto, execute o seguinte comando\n"
           "$ cd ../../ && make build-python && cd -")
    exit(1)
    
sys.path.append("../../target/python")
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
    
    # fonte: https://googleapis.dev/python/protobuf/latest/google/protobuf/descriptor.html#google.protobuf.descriptor.FieldDescriptor.TYPE_BOOL
    map_types = {
        9: str,
        5: int,
        3: int, 
        2: float,
        8: bool}
    
    types = {f.name: map_types[f.type] for f in message_type.DESCRIPTOR.fields}
    schema = [field for field in message_type.DESCRIPTOR.fields_by_name]
    
    return schema, types


def process_line(line: str, message_schema: list):
    data = line.split("|")
    zipped_data = dict(zip(message_schema, data[:-1]))
    return zipped_data


def transform_data(data: dict, fields_expected_type: dict):    
    new_data = {}
    for key in data:
        new_value = fields_expected_type[key](data[key])
        new_data.update({key: new_value})
        
    return new_data


def main(path):    
    with open(path) as file:                
        while True:
            line = file.readline()   
            
            if not line:
                break

            message_type = get_register_type(line)
            message_schema, message_types = get_message_schema(message_type)
            data = process_line(line, message_schema)
            data = transform_data(data, message_types)
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
                