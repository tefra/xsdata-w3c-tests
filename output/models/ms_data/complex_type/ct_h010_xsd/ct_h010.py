from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    my_element1: str = field(
        metadata={
            "name": "myElement1",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    my_element2: str = field(
        metadata={
            "name": "myElement2",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    my_element3: str = field(
        metadata={
            "name": "myElement3",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
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

    my_element: str = field(
        metadata={
            "name": "myElement",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    my_attr1: None | object = field(
        default=None,
        metadata={
            "name": "myAttr1",
            "type": "Attribute",
        },
    )
    my_attr2: None | object = field(
        default=None,
        metadata={
            "name": "myAttr2",
            "type": "Attribute",
        },
    )
    my_attr3: None | object = field(
        default=None,
        metadata={
            "name": "myAttr3",
            "type": "Attribute",
        },
    )
    my_attr4: None | object = field(
        default=None,
        metadata={
            "name": "myAttr4",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
