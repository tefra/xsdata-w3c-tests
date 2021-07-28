from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class A:
    part: List["A.Part"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Part:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        number: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        number2: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    a: Optional[A] = field(
        default=None,
        metadata={
            "name": "A",
            "type": "Element",
            "required": True,
        }
    )
