from output.models.ms_data.identity_constraint.id_h029_xsd.id_h029 import Kid
from output.models.ms_data.identity_constraint.id_h029_xsd.id_h029 import Root
from output.models.ms_data.identity_constraint.id_h029_xsd.id_h029 import Uid
from output.models.ms_data.identity_constraint.id_h029_xsd.id_h029 import Uid2


obj = Root(
    uid2_or_uid=[
        Uid(
            val='1'
        ),
        Uid2(
            val='11'
        ),
        Uid(
            val='111'
        ),
        Uid2(
            val='1.0'
        ),
    ],
    kid=[
        Kid(
            val='1'
        ),
        Kid(
            val='11'
        ),
        Kid(
            val='111'
        ),
        Kid(
            val='1.0'
        ),
    ]
)
