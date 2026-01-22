from output.models.ms_data.schema.sch_g7_a_xsd.sch_g7_a import E1
from output.models.ms_data.schema.sch_g7_a_xsd.sch_g7_a import Root
from output.models.ms_data.schema.sch_g7_a_xsd.sch_g7_b import E1
from output.models.ms_data.schema.sch_g7_a_xsd.sch_g7_c import E1
from output.models.ms_data.schema.sch_g7_a_xsd.sch_g7_d import E1


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
        E1(
            a1=123,
            a2=123
        ),
        E1(
            a1='true',
            a2='123'
        ),
    ]
)
