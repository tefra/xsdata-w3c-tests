from output.models.ms_data.element.elem_t041_xsd.elem_t041 import Root
from output.models.ms_data.element.elem_t041_xsd.elem_t041 import Test2
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    s_a=None,
    test=None,
    test2=Test2(
        any_element=AnyElement(
            qname=None,
            text="1",
            tail=None,
            children=[],
            attributes={
                "{http://www.w3.org/2001/XMLSchema-instance}type": "Union-AB",
            }
        )
    ),
    test3=None
)