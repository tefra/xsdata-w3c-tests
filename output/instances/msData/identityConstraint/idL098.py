from output.models.ms_data.identity_constraint.id_l098_xsd.id_l098 import Root
from output.models.ms_data.identity_constraint.id_l098_xsd.id_l098 import T
from output.models.ms_data.identity_constraint.id_l098_xsd.id_l098 import U


obj = Root(
    t_or_u=[
        T(
            row='1'
        ),
        U(
            row='2'
        ),
        T(
            row='11'
        ),
    ]
)
