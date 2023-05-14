from output.models.ms_data.element.elem_t040_xsd.elem_t040 import Root
from output.models.ms_data.element.elem_t040_xsd.elem_t040 import Test2
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    s_a_or_test=None,
    test2=Test2(
        any_element=AnyElement(
            qname=None,
            text="1",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "Union-A",
            }
        )
    ),
    test3=None
)
