from output.models.ms_data.identity_constraint.id_k006_xsd.id_k006 import Kid
from output.models.ms_data.identity_constraint.id_k006_xsd.id_k006 import Root
from output.models.ms_data.identity_constraint.id_k006_xsd.id_k006 import Uid


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
            elem="1",
            val=None
        ),
        Kid(
            elem="11",
            val=None
        ),
        Kid(
            elem="111",
            val=None
        ),
        Kid(
            elem="1.0",
            val=None
        ),
    ]
)
