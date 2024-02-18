from output.models.ms_data.datatypes.double030_xsd.double030 import ComplexTest
from output.models.ms_data.datatypes.double030_xsd.double030 import Root
from output.models.ms_data.datatypes.double030_xsd.double030 import SimpleTest


obj = Root(
    complex_test=[
        ComplexTest(
            comp_foo=[
                1.0,
            ]
        ),
    ],
    simple_test=[
        SimpleTest(
            value=-8.988465674311579e+307
        ),
        SimpleTest(
            value=-2.225073858507201e-308
        ),
        SimpleTest(
            value=2.225073858507201e-308
        ),
        SimpleTest(
            value=8.988465674311579e+307
        ),
        SimpleTest(
            value=float("nan")
        ),
        SimpleTest(
            value=float("-inf")
        ),
        SimpleTest(
            value=float("inf")
        ),
        SimpleTest(
            value=0.0
        ),
        SimpleTest(
            value=-0.0
        ),
    ]
)
