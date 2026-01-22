from output.models.ms_data.schema.sch_a3_a_xsd.sch_a3_a import E1
from output.models.ms_data.schema.sch_a3_a_xsd.sch_a3_a import Root


obj = Root(
    any_element=[
        E1(
            a1=123,
            a2=True
        ),
    ]
)
