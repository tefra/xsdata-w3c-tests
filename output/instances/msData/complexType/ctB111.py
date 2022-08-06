from output.models.ms_data.complex_type.ct_b111_xsd.ct_b111 import Root


obj = Root(
    attr_test1="first group attribute",
    attr_test2="test attribute",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctB111.xsd",
        "attrTest3": "second group attribute",
    }
)
