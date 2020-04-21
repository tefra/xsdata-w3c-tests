from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://assert020.ns/"


@dataclass
class Temp:
    """
    :ivar temp:
    """
    class Meta:
        name = "temp"
        namespace = "http://assert020.ns/"

    temp: List["Temp"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
