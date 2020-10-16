from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class X:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar d:
    """
    a: Optional["X.A"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    d: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class A:
        """
        :ivar a1:
        :ivar a_count:
        """
        a1: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )
        a_count: Optional[int] = field(
            default=None,
            metadata={
                "name": "aCount",
                "type": "Attribute",
            }
        )


@dataclass
class Y:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    :ivar d:
    """
    a: Optional["Y.A"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    d: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class A:
        """
        :ivar a1:
        :ivar a_count:
        """
        a1: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "",
                "min_occurs": 1,
            }
        )
        a_count: Optional[int] = field(
            default=None,
            metadata={
                "name": "aCount",
                "type": "Attribute",
            }
        )


@dataclass
class Test:
    """
    :ivar x:
    :ivar y:
    """
    class Meta:
        name = "test"

    x: Optional[X] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    y: Optional[Y] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
