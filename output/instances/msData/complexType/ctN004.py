from output.models.ms_data.complex_type.ct_n004_xsd.ct_n004 import Root


obj = Root(
    my_ele1="string data",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctN004.xsd",
        "local": "extension attribute",
    },
    my_ele4="string data"
)
