from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    my_element1: None | str = field(
        default=None,
        metadata={
            "name": "myElement1",
            "type": "Element",
            "namespace": "",
        },
    )
    my_element2: None | str = field(
        default=None,
        metadata={
            "name": "myElement2",
            "type": "Element",
            "namespace": "",
        },
    )
    my_element3: None | str = field(
        default=None,
        metadata={
            "name": "myElement3",
            "type": "Element",
            "namespace": "",
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
class FooType(MyType):
    class Meta:
        name = "fooType"

    my_element4: str = field(
        metadata={
            "name": "myElement4",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
