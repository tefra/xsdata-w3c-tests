from output.models.ms_data.complex_type.ct_g035_xsd.ct_g035 import Root


obj = Root(
    my_element1='test data',
    other_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'ctG035.xsd',
        '{http://tempuri.org/xmlschema}myAttr': 'test attribute',
    }
)
