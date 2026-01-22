from output.models.ms_data.identity_constraint.id_f020_xsd.id_f020 import Root
from output.models.ms_data.identity_constraint.id_f020_xsd.id_f020 import T


obj = Root(
    t=[
        T(
            row='1',
            col='1'
        ),
        T(
            row='2',
            col='1'
        ),
        T(
            row='1',
            col='2'
        ),
        T(
            row='2',
            col='2'
        ),
    ]
)
