from output.models.ms_data.identity_constraint.id_k005_xsd.id_k005 import Kid
from output.models.ms_data.identity_constraint.id_k005_xsd.id_k005 import Root
from output.models.ms_data.identity_constraint.id_k005_xsd.id_k005 import Uid


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
            elem="1"
        ),
        Kid(
            elem="11"
        ),
        Kid(
            elem="111"
        ),
        Kid(
            elem="1.0"
        ),
    ]
)
