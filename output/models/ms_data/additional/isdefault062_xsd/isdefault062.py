from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    elem: Optional["Root.Elem"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Elem:
        attr1: int = field(
            init=False,
            default=123,
            metadata={
                "type": "Attribute",
                "namespace": "foo",
            },
        )
        attr2: str = field(
            init=False,
            default="abc",
            metadata={
                "type": "Attribute",
                "namespace": "foo",
            },
        )
        attr3: bool = field(
            init=False,
            default=True,
            metadata={
                "type": "Attribute",
                "namespace": "foo",
            },
        )
