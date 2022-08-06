from output.models.ms_data.identity_constraint.id_k017_xsd.id_k017 import Kid
from output.models.ms_data.identity_constraint.id_k017_xsd.id_k017 import Root
from output.models.ms_data.identity_constraint.id_k017_xsd.id_k017 import Uid


obj = Root(
    uid=[
        Uid(
            val="1"
        ),
        Uid(
            val="11"
        ),
        Uid(
            val="111"
        ),
        Uid(
            val="1.0"
        ),
    ],
    kid=[
        Kid(
            val="1"
        ),
        Kid(
            val="11"
        ),
        Kid(
            val="111"
        ),
        Kid(
            val="1.0"
        ),
    ]
)
