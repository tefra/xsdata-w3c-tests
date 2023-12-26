from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class Child:
    class Meta:
        name = "child"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class MyType:
    class Meta:
        name = "myType"

    child: Optional[Child] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        },
    )


@dataclass
class Root(MyType):
    class Meta:
        name = "root"
        namespace = "foo"
