from output.models.ms_data.identity_constraint.id_l077_xsd.id_l077 import Root
from output.models.ms_data.identity_constraint.id_l077_xsd.id_l077 import T
from output.models.ms_data.identity_constraint.id_l077_xsd.id_l077 import Ttype


obj = Root(
    t=[
        T(
            col='a',
            content=[
                '1\n',
                Ttype.Row(
                    value='a',
                    x='1'
                ),
                Ttype.Ref(
                    value='a',
                    y='1'
                ),
            ]
        ),
        T(
            col='a',
            content=[
                '1\n',
                Ttype.Row(
                    value='c',
                    x='1'
                ),
                Ttype.Ref(
                    value='b',
                    y='1'
                ),
            ]
        ),
        T(
            col='a',
            content=[
                '1\n',
                Ttype.Row(
                    value='b',
                    x='1'
                ),
                Ttype.Ref(
                    value='c',
                    y='1'
                ),
            ]
        ),
    ]
)
