from output.models.ms_data.schema.sch_p2_a_xsd.sch_p2_a import E1
from output.models.ms_data.schema.sch_p2_a_xsd.sch_p2_a import Root
from output.models.ms_data.schema.sch_p2_a_xsd.sch_p2_b import BE1


obj = Root(
    any_element=[
        E1(
            value='1234'
        ),
        BE1(
            value='abcd'
        ),
    ]
)
