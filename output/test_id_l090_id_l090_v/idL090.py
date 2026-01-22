from decimal import Decimal
from output.models.ms_data.identity_constraint.id_l090_xsd.id_l090 import Root
from output.models.ms_data.identity_constraint.id_l090_xsd.id_l090 import T
from output.models.ms_data.identity_constraint.id_l090_xsd.id_l090 import U


obj = Root(
    t_or_u=[
        T(
            value='1'
        ),
        U(
            value=Decimal('1')
        ),
        T(
            value='11'
        ),
    ]
)
