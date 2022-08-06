from output.models.ms_data.complex_type.ct_g045_xsd.ct_g045 import Root


obj = Root(
    my_element1="test data",
    my_element2=None,
    my_element3=None,
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG045.xsd",
    },
    my_attr="test attribute"
)
