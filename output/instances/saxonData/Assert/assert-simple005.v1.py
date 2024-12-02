from output.models.saxon_data.assert_pkg.assert_simple005_xsd.assert_simple005 import List
from output.models.saxon_data.assert_pkg.assert_simple005_xsd.assert_simple005 import Outer


obj = Outer(
    list_value=[
        List(
            value=[
                1,
                3,
                5,
                7,
                9,
            ]
        ),
        List(
            value=[
                2,
                4,
                6,
                8,
                10,
            ]
        ),
        List(
            value=[
                1,
            ]
        ),
        List(

        ),
    ]
)
