from output.models.ms_data.additional.test66745_a_xsd import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    any_element=AnyElement(
        qname="{foo}bar",
        text="",
        tail=None,
        children=[
            AnyElement(
                qname="{foo1}foo1",
                text="",
                tail=None,
                children=[
                    AnyElement(
                        qname="{foo}bar",
                        text="",
                        tail=None,
                        children=[],
                        attributes={}
                    ),
                ],
                attributes={
                    "x": "1",
                }
            ),
        ],
        attributes={}
    )
)
