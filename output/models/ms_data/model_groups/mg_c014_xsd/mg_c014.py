from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    """
    :ivar a:
    :ivar b:
    :ivar c:
    """
    class Meta:
        name = "test"

    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    c: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Root(Test):
    class Meta:
        name = "root"
