from output.models.ms_data.identity_constraint.id_f026_xsd.id_f026 import R
from output.models.ms_data.identity_constraint.id_f026_xsd.id_f026 import R2
from output.models.ms_data.identity_constraint.id_f026_xsd.id_f026 import Root
from output.models.ms_data.identity_constraint.id_f026_xsd.id_f026 import T


obj = Root(
    t=[
        T(
            r2_or_r=R(
                value=" 1 ",
                val=None
            )
        ),
        T(
            r2_or_r=R2(
                value=" 2 ",
                val=None
            )
        ),
        T(
            r2_or_r=R(
                value=" 3 ",
                val=None
            )
        ),
        T(
            r2_or_r=R2(
                value=" 4 ",
                val=None
            )
        ),
    ]
)
