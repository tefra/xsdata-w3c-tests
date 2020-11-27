from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://assert020.ns/"


@dataclass
class Temp:
    class Meta:
        name = "temp"
        namespace = "http://assert020.ns/"

    temp: List["Temp"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
