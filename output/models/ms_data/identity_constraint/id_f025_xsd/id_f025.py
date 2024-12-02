from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Tabletype:
    class Meta:
        name = "tabletype"

    r: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    c: Optional["Tabletype.C"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )

    @dataclass
    class C:
        val: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        content: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class T(Tabletype):
    class Meta:
        name = "t"


@dataclass
class Root:
    class Meta:
        name = "root"

    t: list[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
