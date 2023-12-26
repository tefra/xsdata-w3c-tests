from output.models.ms_data.schema.sch_q1_a_xsd.sch_q1_a import E1
from output.models.ms_data.schema.sch_q1_a_xsd.sch_q1_a import Root
from output.models.ms_data.schema.sch_q1_a_xsd.sch_q1_b import BE1
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_element=[
        E1(
            b1_or_b2=AnyElement(
                qname='{ns-a}b1',
                text=''
            ),
            b3_or_b4=AnyElement(
                qname='{ns-a}b3',
                text=''
            )
        ),
        BE1(
            b1_or_b2=AnyElement(
                qname='{ns-a}b2',
                text=''
            ),
            b3_or_b4=AnyElement(
                qname='{ns-a}b4',
                text=''
            )
        ),
    ]
)
