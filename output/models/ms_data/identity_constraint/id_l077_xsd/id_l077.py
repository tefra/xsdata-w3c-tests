from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass
class Ttype:
    class Meta:
        name = "ttype"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    row: List["Ttype.Row"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "myNS.tempuri.org",
            "min_occurs": 1,
            "max_occurs": 10,
            "sequential": True,
        }
    )
    ref: List["Ttype.Ref"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "myNS.tempuri.org",
            "min_occurs": 1,
            "max_occurs": 10,
            "sequential": True,
        }
    )
    col: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "myNS.tempuri.org",
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
