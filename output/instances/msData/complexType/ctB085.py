from output.models.ms_data.complex_type.ct_b085_xsd.ct_b085 import Root


obj = Root(
    my_element='field data',
    any_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'ctB085.xsd',
        'attrTest': 'test attribute',
    }
)
