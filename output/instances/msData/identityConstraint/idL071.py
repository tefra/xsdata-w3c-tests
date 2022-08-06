from output.models.ms_data.identity_constraint.id_l071_xsd.id_l071 import Root
from output.models.ms_data.identity_constraint.id_l071_xsd.id_l071 import T


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
    ],
    kid=[
        "1",
        "2",
        "11",
    ]
)
