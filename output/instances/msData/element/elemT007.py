from output.models.ms_data.element.elem_t007_xsd.elem_t007 import MyType
from output.models.ms_data.element.elem_t007_xsd.elem_t007 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    foo_test=DerivedElement(
        qname="fooTest",
        value=MyType(
            foo_ele1="len4",
            foo_ele2=26,
            foo_ele3=None,
            other_attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "myType",
            }
        ),
        type="myType"
    )
)
