from output.models.ms_data.element.elem_q015_xsd.elem_q015 import FooTest
from output.models.ms_data.element.elem_q015_xsd.elem_q015 import Root


obj = Root(
    foo_test=[
        FooTest(
            value='WA'
        ),
        FooTest(
            value='OR'
        ),
        FooTest(
            value='CA'
        ),
    ]
)
