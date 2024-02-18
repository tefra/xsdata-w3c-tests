from output.models.saxon_data.assert_pkg.assert_simple005_xsd.assert_simple005 import ListType
from output.models.saxon_data.assert_pkg.assert_simple005_xsd.assert_simple005 import Outer


obj = Outer(
    list_value=[
        ListType(
            value=[
                1,
                3,
                5,
                7,
                9,
            ]
        ),
        ListType(
            value=[
                2,
                4,
                6,
                8,
                10,
            ]
        ),
        ListType(
            value=[
                1,
            ]
        ),
        ListType(

        ),
    ]
)
