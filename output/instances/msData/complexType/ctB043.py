from output.models.ms_data.complex_type.ct_b043_xsd.ct_b043 import Root


obj = Root(
    my_element="group field",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctB043.xsd",
        "attrTest": "any attribute",
    }
)
