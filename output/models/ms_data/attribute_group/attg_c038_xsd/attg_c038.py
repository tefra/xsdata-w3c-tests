from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar att:
    :ivar att1:
    :ivar att2:
    :ivar foo1:
    :ivar foo2:
    :ivar ext_foo:
    """
    class Meta:
        name = "test"

    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    foo1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    foo2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ext_foo: Optional[int] = field(
        default=None,
        metadata={
            "name": "extFoo",
            "type": "Attribute",
        }
    )


@dataclass
class Doc(Test):
    class Meta:
        name = "doc"
