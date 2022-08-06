from output.models.ms_data.identity_constraint.id_h018_xsd.id_h018 import Root
from output.models.ms_data.identity_constraint.id_h018_xsd.id_h018 import T


obj = Root(
    t=[
        T(
            row="1",
            col="1"
        ),
        T(
            row="2",
            col="1"
        ),
        T(
            row="1",
            col="2"
        ),
        T(
            row="2",
            col="2"
        ),
    ]
)
