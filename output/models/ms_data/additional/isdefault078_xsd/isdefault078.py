from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class Root:
    """
    :ivar space:
    """
    class Meta:
        name = "root"

    space: Optional["Root.Value"] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )

    class Value(Enum):
        """
        :cvar DEFAULT:
        :cvar PRESERVE:
        """
        DEFAULT = "default"
        PRESERVE = "preserve"
