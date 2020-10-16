from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Ctype:
    """
    :ivar content:
    :ivar val:
    """
    class Meta:
        name = "ctype"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Ctype2(Ctype):
    """
    :ivar content:
    :ivar val2:
    """
    class Meta:
        name = "ctype2"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Tabletype:
    """
    :ivar c:
    :ivar r:
    """
    class Meta:
        name = "tabletype"

    c: Optional[Ctype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    r: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class T(Tabletype):
    class Meta:
        name = "t"


@dataclass
class Root:
    """
    :ivar t:
    """
    class Meta:
        name = "root"

    t: List[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
