from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Type1:
    """
    :ivar value:
    :ivar attr_test:
    """
    class Meta:
        name = "_1"

    value: Optional[str] = field(
        default=None,
    )
    attr_test: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        }
    )


@dataclass
class Root(Type1):
    class Meta:
        name = "root"
