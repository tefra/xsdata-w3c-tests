from output.models.ms_data.complex_type.ct_b057_xsd.ct_b057 import Root


obj = Root(
    my_element="all field",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctB057.xsd",
        "attrTest": "any attribute",
    }
)
