from output.models.ms_data.complex_type.ct_h031_xsd.ct_h031 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    my_element1_or_my_element2_or_my_element3=DerivedElement(
        qname='myElement2',
        value='test data'
    ),
    local_attributes={
        'local': 'local attribute',
    },
    my_element4='test data',
    my_attr='next attribute'
)
