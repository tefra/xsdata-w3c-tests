from output.models.ms_data.complex_type.ct_n003_xsd.ct_n003 import Root


obj = Root(
    my_ele1='string data',
    local_attributes={
        'local': 'extended attribute',
    },
    my_ele4='string data',
    any_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation': 'ctN003.xsd',
    }
)
