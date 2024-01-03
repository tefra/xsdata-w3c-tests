from output.models.ms_data.complex_type.ct_i044_xsd.ct_i044 import MyType
from output.models.ms_data.complex_type.ct_i044_xsd.ct_i044 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    foo_test=DerivedElement(
        qname='fooTest',
        value=MyType(
            foo_ele1='len4',
            foo_ele2=26
        ),
        type='myType'
    )
)
