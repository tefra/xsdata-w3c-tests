from output.models.ms_data.datatypes.double030_xsd.double030 import ComplexTest
from output.models.ms_data.datatypes.double030_xsd.double030 import Root


obj = Root(
    complex_test=[
        ComplexTest(
            comp_foo=[
                1.0,
            ]
        ),
    ],
    simple_test=[
        -8.988465674311579e+307,
        -2.225073858507201e-308,
        2.225073858507201e-308,
        8.988465674311579e+307,
        float("nan"),
        float("-inf"),
        float("inf"),
        0.0,
        -0.0,
    ]
)
