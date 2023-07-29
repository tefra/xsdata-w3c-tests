from output.models.ms_data.schema.sch_g2_a_xsd.sch_g1_c import E1
from output.models.ms_data.schema.sch_g2_a_xsd.sch_g2_a import E1
from output.models.ms_data.schema.sch_g2_a_xsd.sch_g2_a import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        E1(
            a1=123,
            a2=True
        ),
        AnyElement(
            qname="e1",
            text="",
            children=[
                AnyElement(
                    qname="a1",
                    text="true"
                ),
                AnyElement(
                    qname="a2",
                    text="123"
                ),
            ]
        ),
        E1(
            a1=123,
            a2=123
        ),
    ]
)
