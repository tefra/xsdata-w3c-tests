from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    my_element1_or_my_element2_or_my_element3: (
        None | MyType.MyElement1 | MyType.MyElement2 | MyType.MyElement3
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "myElement1",
                    "type": ForwardRef("MyType.MyElement1"),
                    "namespace": "",
                },
                {
                    "name": "myElement2",
                    "type": ForwardRef("MyType.MyElement2"),
                    "namespace": "",
                },
                {
                    "name": "myElement3",
                    "type": ForwardRef("MyType.MyElement3"),
                    "namespace": "",
                },
            ),
        },
    )
    local_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )

    @dataclass(kw_only=True)
    class MyElement1:
        value: str = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class MyElement2:
        value: str = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class MyElement3:
        value: str = field(
            metadata={
                "required": True,
            }
        )


@dataclass(kw_only=True)
class FooType(MyType):
    class Meta:
        name = "fooType"

    my_element4: None | str = field(
        default=None,
        metadata={
            "name": "myElement4",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
