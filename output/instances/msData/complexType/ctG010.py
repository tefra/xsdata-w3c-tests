from output.models.ms_data.complex_type.ct_g010_xsd.ct_g010 import Root


obj = Root(
    any_element=None,
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctG010.xsd",
    },
    my_element="test data",
    my_attr="test attribute",
    my_attr2="second test attribute"
)