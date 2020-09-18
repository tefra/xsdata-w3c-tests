.PHONY: convert-xml-declaration
convert-xml-declaration:
	find output/instances -type f -readable -writable -exec sed -i "s/version='1.0' encoding='UTF-8'/version=\"1.0\" encoding=\"UTF-8\"/g" {} \;
