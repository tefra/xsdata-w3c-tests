from output.models.ms_data.schema.sch_g12_a_xsd.sch_g12_a import FooA
from output.models.ms_data.schema.sch_g12_a_xsd.sch_g12_a import Root
from output.models.ms_data.schema.sch_g12_a_xsd.sch_g12_b import FooB
from output.models.ms_data.schema.sch_g12_a_xsd.sch_g12_c import FooC


obj = Root(
    any_element=[
        FooA(

        ),
        FooB(

        ),
        FooC(

        ),
    ]
)
