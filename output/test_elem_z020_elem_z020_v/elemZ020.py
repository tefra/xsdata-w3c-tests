from output.models.ms_data.element.elem_z020_xsd.elem_z020 import Foo
from output.models.ms_data.element.elem_z020_xsd.elem_z020 import Root


obj = Root(
    foo_or_e1=[
        Foo(
            value=True
        ),
        123,
        Foo(
            value=True
        ),
        123,
    ]
)
