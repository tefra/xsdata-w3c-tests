from output.models.ms_data.element.elem_q013_xsd.elem_q013 import FooTest
from output.models.ms_data.element.elem_q013_xsd.elem_q013 import Root


obj = Root(
    foo_test=[
        FooTest(
            value='WA'
        ),
        FooTest(
            value='OR'
        ),
    ]
)
