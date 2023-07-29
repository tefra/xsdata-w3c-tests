from output.models.ms_data.schema.sch_d7_a_xsd.ns_a import E1
from output.models.ms_data.schema.sch_d7_a_xsd.ns_a import E3
from output.models.ms_data.schema.sch_d7_a_xsd.ns_a import Root


obj = Root(
    any_element=[
        E1(
            a1=123,
            a2=True
        ),
        E3(
            c1=123,
            c2=123
        ),
    ]
)
