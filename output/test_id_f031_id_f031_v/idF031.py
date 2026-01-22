from output.models.ms_data.identity_constraint.id_f031_xsd.id_f031 import R
from output.models.ms_data.identity_constraint.id_f031_xsd.id_f031 import R2
from output.models.ms_data.identity_constraint.id_f031_xsd.id_f031 import Root
from output.models.ms_data.identity_constraint.id_f031_xsd.id_f031 import T


obj = Root(
    t=[
        T(
            r2_or_r=R(
                value=' 1 '
            )
        ),
        T(
            r2_or_r=R2(
                value=' 2 '
            )
        ),
        T(
            r2_or_r=R(
                value=' 3 '
            )
        ),
        T(
            r2_or_r=R2(
                value=' 4 '
            )
        ),
    ]
)
