from dataclasses import dataclass, field
from typing import Optional


@dataclass
class X:
    a: Optional[str] = field(
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
    minimal: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Y(X):
    a: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Test(X):
    class Meta:
        name = "test"
