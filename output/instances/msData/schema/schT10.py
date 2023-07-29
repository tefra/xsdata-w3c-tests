from output.models.ms_data.schema.sch_t10_a_xsd.sch_t10_a import E2
from output.models.ms_data.schema.sch_t10_a_xsd.sch_t10_a import Root
from output.models.ms_data.schema.sch_t10_a_xsd.sch_t10_b import BE1


obj = Root(
    any_element=[
        BE1(
            att1="123"
        ),
        E2(
            value=12
        ),
    ]
)
