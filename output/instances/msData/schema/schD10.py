from output.models.ms_data.schema.sch_d10_a_xsd.sch_d10_a import ACt
from output.models.ms_data.schema.sch_d10_a_xsd.sch_d10_a import E1
from output.models.ms_data.schema.sch_d10_a_xsd.sch_d10_a import Root


obj = Root(
    any_element=[
        E1(
            c21_or_c22=[
                ACt.C21(
                    value=1
                ),
            ]
        ),
    ]
)
