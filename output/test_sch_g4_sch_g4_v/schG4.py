from output.models.ms_data.schema.sch_g4_a_xsd.sch_g4_a import E1
from output.models.ms_data.schema.sch_g4_a_xsd.sch_g4_a import Root
from output.models.ms_data.schema.sch_g4_a_xsd.sch_g4_b import E1
from output.models.ms_data.schema.sch_g4_a_xsd.sch_g4_c import E1
from output.models.ms_data.schema.sch_g4_a_xsd.sch_g4_c import Foo


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
        Foo(

        ),
        E1(
            a1=123,
            a2=123
        ),
    ]
)
