from output.models.ms_data.schema.sch_c3_a_xsd.sch_c3_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        AnyElement(
            qname="e1",
            text="",
            children=[
                AnyElement(
                    qname="a1",
                    text="123"
                ),
                AnyElement(
                    qname="a2",
                    text="true"
                ),
            ]
        ),
        AnyElement(
            qname="e2",
            text="",
            children=[
                AnyElement(
                    qname="b1",
                    text="true"
                ),
                AnyElement(
                    qname="b2",
                    text="123"
                ),
            ]
        ),
    ]
)
