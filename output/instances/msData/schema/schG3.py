from output.models.ms_data.schema.sch_g3_a_xsd.sch_g3_a import E1
from output.models.ms_data.schema.sch_g3_a_xsd.sch_g3_a import Root
from output.models.ms_data.schema.sch_g3_a_xsd.sch_g3_b import E1
from output.models.ms_data.schema.sch_g3_a_xsd.sch_g3_c import Foo


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
    ]
)
