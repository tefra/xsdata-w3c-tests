from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar foo:
    :ivar att:
    """
    class Meta:
        name = "doc"

    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    att: str = field(
        init=False,
        default="fixed",
        metadata={
            "type": "Attribute",
        }
    )
