from output.models.ms_data.schema.sch_g5_a_xsd.sch_g5_a import E1
from output.models.ms_data.schema.sch_g5_a_xsd.sch_g5_a import Root
from output.models.ms_data.schema.sch_g5_a_xsd.sch_g5_b import E1


obj = Root(
    any_element=[
        E1(
            a1=123,
            a2=True
        ),
        E1(
            a1=True,
            a2=123
        ),
    ]
)
