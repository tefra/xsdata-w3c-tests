from output.models.ms_data.schema.sch_c3_a_xsd.sch_c3_a import E1
from output.models.ms_data.schema.sch_c3_a_xsd.sch_c3_a import Root
from output.models.ms_data.schema.sch_c3_a_xsd.sch_c3_b import E2


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
