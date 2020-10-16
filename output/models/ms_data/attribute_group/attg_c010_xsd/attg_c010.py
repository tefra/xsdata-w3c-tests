from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar foo:
    :ivar bar:
    """
    class Meta:
        name = "test"

    foo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class T(Test):
    pass
