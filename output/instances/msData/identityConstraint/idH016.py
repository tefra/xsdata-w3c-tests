from output.models.ms_data.identity_constraint.id_h016_xsd.id_h016 import Kid
from output.models.ms_data.identity_constraint.id_h016_xsd.id_h016 import Root
from output.models.ms_data.identity_constraint.id_h016_xsd.id_h016 import Uid


obj = Root(
    uid=[
        Uid(
            val="test"
        ),
        Uid(
            val="test"
        ),
    ],
    kid=[
        Kid(
            val="test"
        ),
    ]
)
