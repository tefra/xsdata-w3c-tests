from output.models.ms_data.element.elem_t067_xsd.elem_t067 import Root
from output.models.ms_data.element.elem_t067_xsd.elem_t067 import Sa3
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    sa3=[
        Sa3(
            any_element=AnyElement(
                qname=None,
                text="1",
                tail=None,
                children=[],
                attributes={}
            )
        ),
    ],
    sa2=[],
    sa1=[],
    test1=[],
    test2=None,
    test3=None,
    test4=None,
    test5=None
)
