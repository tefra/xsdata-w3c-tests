from dataclasses import dataclass, field
from typing import List, Optional, Type

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Ttype:
    class Meta:
        name = "ttype"

    col: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "row",
                    "type": Type["Ttype.Row"],
                    "namespace": "myNS.tempuri.org",
                },
                {
                    "name": "ref",
                    "type": Type["Ttype.Ref"],
                    "namespace": "myNS.tempuri.org",
                },
            ),
        }
    )

    @dataclass
    class Row:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        x: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "myNS.tempuri.org",
            }
        )

    @dataclass
    class Ref:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        y: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "myNS.tempuri.org",
            }
        )


@dataclass
class T(Ttype):
    class Meta:
        name = "t"
        namespace = "myNS.tempuri.org"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

    t: List[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
