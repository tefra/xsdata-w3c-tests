from output.models.ms_data.schema.sch_c4_a_xsd.sch_c4_a import E1
from output.models.ms_data.schema.sch_c4_a_xsd.sch_c4_a import Root
from output.models.ms_data.schema.sch_c4_a_xsd.sch_c4_b import E2


obj = Root(
    any_element=[
        E1(
            a1=123,
            a2=True
        ),
        E2(
            b1=True,
            b2=123
        ),
    ]
)
