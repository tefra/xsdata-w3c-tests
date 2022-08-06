from output.models.ms_data.group.group_h014_xsd.group_h014 import Doc
from output.models.ms_data.group.group_h014_xsd.group_h014 import Elem
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=Elem(
        choice=[
            AnyElement(
                qname="x1",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="x2",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="x1",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
            AnyElement(
                qname="x2",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ]
    )
)
