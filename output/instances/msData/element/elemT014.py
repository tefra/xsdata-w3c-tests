from output.models.ms_data.element.elem_t014_xsd.elem_t014 import FooTest
from output.models.ms_data.element.elem_t014_xsd.elem_t014 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    foo_test=FooTest(
        any_element=AnyElement(
            qname=None,
            text="1",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "myUnion",
            }
        )
    )
)
