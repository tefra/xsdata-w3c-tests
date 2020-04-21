from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class When:
    """
    :ivar value:
    """
    class Meta:
        name = "when"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Event:
    """
    :ivar when:
    :ivar type:
    """
    class Meta:
        name = "event"

    when: Optional[When] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Doc:
    """
    :ivar event:
    :ivar type:
    """
    class Meta:
        name = "doc"

    event: List[Event] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
