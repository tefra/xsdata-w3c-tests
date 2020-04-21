from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11"


class DurWhiteSpace(Enum):
    """
    :cvar VALUE:
    """
    VALUE = ""


@dataclass
class Root:
    """
    :ivar el_white_space:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11"

    el_white_space: Optional[DurWhiteSpace] = field(
        default=None,
        metadata=dict(
            name="elWhiteSpace",
            type="Element",
            namespace="",
            required=True
        )
    )
