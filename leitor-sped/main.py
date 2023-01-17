import sys

sys.path.append("../target/python")
from registros.R0000_pb2 import R0000


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("É necessário especificar pelo menos um arquivo txt para processamento")
        exit(1)
    
    paths = sys.argv[1:-1]
    
    for path in paths:
        
        with open(path) as file:
            
            while True:
                line = file.readline()                
                if not line:
                    break
                
                data = line.split("|")
                register_code = data[0]
                
                
                