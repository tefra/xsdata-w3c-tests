from output.models.ms_data.additional.test66745_a_xsd import Bar
from output.models.ms_data.additional.test66745_a_xsd import Foo
from output.models.ms_data.additional.test66745_a_xsd import Foo1


obj = Foo(
    any_element=Bar(
        foo1_or_foo_or_bar=[
            Foo1(
                any_element=Bar(

                ),
                x=1
            ),
        ]
    )
)
