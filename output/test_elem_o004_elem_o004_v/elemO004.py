from output.models.ms_data.element.elem_o004_xsd.elem_o004 import FooTest
from output.models.ms_data.element.elem_o004_xsd.elem_o004 import Root


obj = Root(
    foo_test=FooTest(
        my_elem_1='string test',
        my_elem_2=1234567890123456789,
        my_attr='AA'
    )
)
