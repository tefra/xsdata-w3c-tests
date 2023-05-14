from output.models.ms_data.element.elem_t002_xsd.elem_t002 import MyType
from output.models.ms_data.element.elem_t002_xsd.elem_t002 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    foo_test=DerivedElement(
        qname="fooTest",
        value=MyType(
            foo_ele1="string",
            foo_ele2=26,
            foo_ele3=True
        ),
        type="myType"
    )
)
