from output.models.ms_data.element.test115044_2_xsd.test115044_2 import E
from output.models.ms_data.element.test115044_2_xsd.test115044_2 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    e1=None,
    e=E(
        any_element=AnyElement(
            qname=None,
            text="abc",
            tail=None,
            children=[],
            attributes={}
        )
    )
)
