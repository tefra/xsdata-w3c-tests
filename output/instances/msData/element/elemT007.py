from output.models.ms_data.element.elem_t007_xsd.elem_t007 import MyType
from output.models.ms_data.element.elem_t007_xsd.elem_t007 import Root
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
