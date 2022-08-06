from output.models.ms_data.datatypes.float039_xsd.float039 import ComplexTest
from output.models.ms_data.datatypes.float039_xsd.float039 import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=[
            1.2345,
        ]
    ),
    simple_test=[
        [
            -3.4028234663852886e+38,
        ],
        [
            -2.3509885615147286e-38,
        ],
        [
            2.3509885615147286e-38,
        ],
        [
            3.4028234663852886e+38,
        ],
        [
            float("nan"),
        ],
        [
            float("-inf"),
        ],
        [
            float("inf"),
        ],
        [
            0.0,
        ],
        [
            -0.0,
        ],
    ]
)
