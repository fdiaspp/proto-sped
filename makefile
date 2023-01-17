default:
	@echo "execute make build"

SRC_DIR=.
DST_DIR=./target
FILES=`find . -name "*.proto"`

build-python: 
	@mkdir -p ${DST_DIR}/python && protoc -I=${SRC_DIR} --python_out=${DST_DIR}/python ${FILES}