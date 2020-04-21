from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class D:
    """
    :ivar d:
    """
    class Meta:
        name = "d"

    d: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class DatedEvent:
    """
    :ivar event:
    """
    class Meta:
        name = "datedEvent"

    event: Optional[D] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Temp:
    """
    :ivar event:
    """
    class Meta:
        name = "temp"

    event: Optional[D] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


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
