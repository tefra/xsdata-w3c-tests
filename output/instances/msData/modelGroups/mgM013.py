from output.models.ms_data.model_groups.mg_m013_xsd.mg_m013 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    any_element=AnyElement(
        qname=None,
        text=None,
        tail=None,
        children=[
            AnyElement(
                qname="foo",
                text="",
                tail=None,
                children=[
                    AnyElement(
                        qname="e1",
                        text="",
                        tail=None,
                        children=[],
                        attributes={}
                    ),
                    AnyElement(
                        qname="e2",
                        text="",
                        tail=None,
                        children=[],
                        attributes={}
                    ),
                ],
                attributes={}
            ),
            AnyElement(
                qname="global",
                text="",
                tail=None,
                children=[],
                attributes={}
            ),
        ],
        attributes={}
    )
)
