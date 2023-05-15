from output.models.ms_data.additional.test66745_a_xsd import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    any_element=AnyElement(
        qname="{foo}bar",
        text="",
        children=[
            AnyElement(
                qname="{foo1}foo1",
                text="",
                children=[
                    AnyElement(
                        qname="{foo}bar",
                        text=""
                    ),
                ],
                attributes={
                    "x": "1",
                }
            ),
        ]
    )
)
