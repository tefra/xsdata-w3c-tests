from output.models.ms_data.element.qfe1700a_xsd.qfe1700a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    e1="abc",
    any_element=AnyElement(
        qname="e2",
        text="abc",
        tail=None,
        children=[
            AnyElement(
                qname="e3",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ],
        attributes={
            "{http://www.w3.org/2001/XMLSchema-instance}nil": "false",
        }
    )
)