from output.models.ms_data.complex_type.ct_g020_xsd.ct_g020 import Root


obj = Root(
    my_element1='test data',
    any_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'ctG020.xsd',
    },
    local_attr='test attribute',
    my_attr='second test attribute'
)
