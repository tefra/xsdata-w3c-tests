from output.models.ms_data.identity_constraint.id_l045_xsd.id_l045 import Root
from output.models.ms_data.identity_constraint.id_l045_xsd.id_l045 import T
from output.models.ms_data.identity_constraint.id_l045_xsd.id_l045 import Ttype


obj = Root(
    t=[
        T(
            row=[
                Ttype.Row(
                    value=" 1 ",
                    col="1"
                ),
            ]
        ),
        T(
            row=[
                Ttype.Row(
                    value=" 2 ",
                    col="2"
                ),
            ]
        ),
        T(
            row=[
                Ttype.Row(
                    value=" 11 ",
                    col="11"
                ),
            ]
        ),
    ]
)
