from output.models.ms_data.schema.sch_q3_a_xsd.sch_q3_a import BCt
from output.models.ms_data.schema.sch_q3_a_xsd.sch_q3_a import E1
from output.models.ms_data.schema.sch_q3_a_xsd.sch_q3_a import Root
from output.models.ms_data.schema.sch_q3_a_xsd.sch_q3_b import BE1


obj = Root(
    any_element=[
        E1(
            b1_or_b2=BCt.B1(

            )
        ),
        BE1(
            b1_or_b2=BCt.B2(

            )
        ),
    ]
)
