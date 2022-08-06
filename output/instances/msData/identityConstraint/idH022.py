from output.models.ms_data.identity_constraint.id_h022_xsd.id_h022 import Kid
from output.models.ms_data.identity_constraint.id_h022_xsd.id_h022 import Root
from output.models.ms_data.identity_constraint.id_h022_xsd.id_h022_imp import Iid


obj = Root(
    uid=[],
    iid=[
        Iid(
            val="1"
        ),
        Iid(
            val="11"
        ),
        Iid(
            val="111"
        ),
        Iid(
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
