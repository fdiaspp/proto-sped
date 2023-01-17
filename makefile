default:
	@echo "execute make build"

SRC_DIR=./protobuf
DST_DIR=./target
FILES=`find ${SRC_DIR} -name "*.proto"`

build-python: 
	@mkdir -p ${DST_DIR}/python && protoc -I=${SRC_DIR} --python_out=${DST_DIR}/python ${FILES}