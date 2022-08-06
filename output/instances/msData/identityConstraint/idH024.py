from output.models.ms_data.identity_constraint.id_h024_xsd.id_h024 import Kid
from output.models.ms_data.identity_constraint.id_h024_xsd.id_h024 import Root
from output.models.ms_data.identity_constraint.id_h024_xsd.id_h024 import Uid
from output.models.ms_data.identity_constraint.id_h024_xsd.id_h024 import Uid2


obj = Root(
    uid2=[
        Uid2(
            val="11"
        ),
        Uid2(
            val="1.0"
        ),
    ],
    uid=[
        Uid(
            val="1"
        ),
        Uid(
            val="111"
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
