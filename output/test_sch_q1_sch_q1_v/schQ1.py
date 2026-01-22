from output.models.ms_data.schema.sch_q1_a_xsd.sch_q1_a import BCt
from output.models.ms_data.schema.sch_q1_a_xsd.sch_q1_a import E1
from output.models.ms_data.schema.sch_q1_a_xsd.sch_q1_a import Root
from output.models.ms_data.schema.sch_q1_a_xsd.sch_q1_b import BE1


obj = Root(
    any_element=[
        E1(
            b1_or_b2=BCt.B1(

            ),
            b3_or_b4=BCt.B3(

            )
        ),
        BE1(
            b1_or_b2=BCt.B2(

            ),
            b3_or_b4=BCt.B4(

            )
        ),
    ]
)
