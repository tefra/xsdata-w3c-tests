from output.models.ms_data.complex_type.ct_g007_xsd.ct_g007 import Root


obj = Root(
    any_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'ctG007.xsd',
    },
    my_element='test data',
    my_attr='test attribute'
)
