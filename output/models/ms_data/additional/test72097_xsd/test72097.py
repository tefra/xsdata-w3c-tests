from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Child:
    class Meta:
        name = "child"
        namespace = "foo"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    child: Child = field(
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root(MyType):
    class Meta:
        name = "root"
        namespace = "foo"
