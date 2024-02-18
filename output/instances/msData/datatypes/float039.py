from output.models.ms_data.datatypes.float039_xsd.float039 import ComplexTest
from output.models.ms_data.datatypes.float039_xsd.float039 import Root
from output.models.ms_data.datatypes.float039_xsd.float039 import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            1.2345,
        ]
    ),
    simple_test=[
        SimpleTest(
            value=[
                -3.4028234663852886e+38,
            ]
        ),
        SimpleTest(
            value=[
                -2.3509885615147286e-38,
            ]
        ),
        SimpleTest(
            value=[
                2.3509885615147286e-38,
            ]
        ),
        SimpleTest(
            value=[
                3.4028234663852886e+38,
            ]
        ),
        SimpleTest(
            value=[
                float("nan"),
            ]
        ),
        SimpleTest(
            value=[
                float("-inf"),
            ]
        ),
        SimpleTest(
            value=[
                float("inf"),
            ]
        ),
        SimpleTest(
            value=[
                0.0,
            ]
        ),
        SimpleTest(
            value=[
                -0.0,
            ]
        ),
    ]
)
