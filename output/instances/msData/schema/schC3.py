from output.models.ms_data.schema.sch_c3_a_xsd.sch_c3_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="e1",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="a1",
                    text="123",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="a2",
                    text="true",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            attributes={}
        ),
        AnyElement(
            qname="e2",
            text="",
            tail=None,
            children=[
                AnyElement(
                    qname="b1",
                    text="true",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="b2",
                    text="123",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            attributes={}
        ),
    ]
)
