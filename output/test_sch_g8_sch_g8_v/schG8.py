from output.models.ms_data.schema.sch_g8_a_xsd.sch_g8_a import E1
from output.models.ms_data.schema.sch_g8_a_xsd.sch_g8_a import Root
from output.models.ms_data.schema.sch_g8_a_xsd.sch_g8_c import E1
from output.models.ms_data.schema.sch_g8_a_xsd.sch_g8_c import Foo


obj = Root(
    any_element=[
        E1(
            a1=123,
            a2=True
        ),
        E1(
            a1=123,
            a2=123
        ),
        Foo(

        ),
    ]
)
