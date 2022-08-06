from output.models.ms_data.complex_type.ct_e008_xsd.ct_e008 import Root


obj = Root(
    value="simpleContent",
    any_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation": "ctE008.xsd",
        "attrTest": "some attribute",
    }
)
