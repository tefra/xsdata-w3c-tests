from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    """
    :ivar space:
    """
    class Meta:
        name = "root"

    space: Optional["Root.Type"] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )

    class Type(Enum):
        """
        :cvar DEFAULT:
        :cvar PRESERVE:
        """
        DEFAULT = "default"
        PRESERVE = "preserve"
