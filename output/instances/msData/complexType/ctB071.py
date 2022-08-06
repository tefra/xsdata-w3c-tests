from output.models.ms_data.complex_type.ct_b071_xsd.ct_b071 import Root


obj = Root(
    my_element="all field",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctB071.xsd",
        "attrTest": "attribute1",
    }
)
