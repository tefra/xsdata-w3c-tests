from output.models.ms_data.schema.sch_f2_a_xsd.sch_f2_a import E1
from output.models.ms_data.schema.sch_f2_a_xsd.sch_f2_a import Root
from output.models.ms_data.schema.sch_f2_a_xsd.sch_f2_b import E1


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
