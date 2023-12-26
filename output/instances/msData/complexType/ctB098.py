from output.models.ms_data.complex_type.ct_b098_xsd.ct_b098 import Root


obj = Root(
    attr_test='nonGroup attribute',
    any_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'ctB098.xsd',
        'attrTest1': 'test attribute',
    }
)
