from output.models.ms_data.identity_constraint.id_h003_xsd.id_h003 import Kid
from output.models.ms_data.identity_constraint.id_h003_xsd.id_h003 import Root
from output.models.ms_data.identity_constraint.id_h003_xsd.id_h003 import Uid


obj = Root(
    uid=[
        Uid(
            val="1",
            val2=None
        ),
        Uid(
            val="11",
            val2=None
        ),
        Uid(
            val="111",
            val2=None
        ),
        Uid(
            val="1.0",
            val2=None
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
