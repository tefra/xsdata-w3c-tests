from output.models.ms_data.identity_constraint.id_f024_xsd.id_f024 import Root
from output.models.ms_data.identity_constraint.id_f024_xsd.id_f024 import T
from output.models.ms_data.identity_constraint.id_f024_xsd.id_f024a import R


obj = Root(
    t=[
        T(
            r=R(
                value=' 1 '
            ),
            val='1'
        ),
        T(
            r=R(
                value=' 2 '
            ),
            val='2'
        ),
        T(
            r=R(
                value=' 3 '
            ),
            val='3'
        ),
    ]
)
