# proto-sped
SPED implementado utilizando Protocol Buffer

Baseado em http://sped.rfb.gov.br/estatico/D6/01D9D1F3CDA056218D8171315949A451494EA3/Guia_Pratico_EFD_Versao_312.pdf

Instalando protoc
```
PROTOC_ZIP=protoc-21.12-linux-x86_64.zip
curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v21.12/$PROTOC_ZIP
unzip -o $PROTOC_ZIP -d /usr/local bin/protoc
unzip -o $PROTOC_ZIP -d /usr/local 'include/*'
rm -f $PROTOC_ZIP

```


Compilando para Python 
```sh
make build-pytho
```