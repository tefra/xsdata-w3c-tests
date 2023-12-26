from output.models.ms_data.complex_type.ct_h047_xsd.ct_h047 import Root


obj = Root(
    my_element2='test data',
    my_element4='test data',
    other_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'ctH047.xsd',
        '{http://tempuri.org/xmlschema}myAttr': 'extension attribute',
    }
)
