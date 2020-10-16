from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://assert021.ns/"


@dataclass
class Temp:
    """
    :ivar temp:
    """
    class Meta:
        name = "temp"
        namespace = "http://assert021.ns/"

    temp: List["Temp"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
