from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class DatedEvent:
    """
    :ivar value:
    :ivar event:
    """
    class Meta:
        name = "datedEvent"

    value: Optional[str] = field(
        default=None,
    )
    event: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class Temp(DatedEvent):
    class Meta:
        name = "temp"



@dataclass
class Doc:
    """
    :ivar temp:
    """
    class Meta:
        name = "doc"

    temp: List[Temp] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
