from output.models.ms_data.complex_type.ct_i041_xsd.ct_i041 import MyType
from output.models.ms_data.complex_type.ct_i041_xsd.ct_i041 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    foo_test=DerivedElement(
        qname='fooTest',
        value=MyType(
            foo_ele1='string',
            foo_ele2=26,
            foo_ele3=True
        ),
        type='myType'
    )
)
