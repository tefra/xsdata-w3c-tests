from output.models.ms_data.identity_constraint.id_g014_xsd.id_g014 import Root
from output.models.ms_data.identity_constraint.id_g014_xsd.id_g014 import T


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
