from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Event:
    """
    :ivar when:
    :ivar type:
    """
    class Meta:
        name = "event"

    when: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class When:
    """
    :ivar value:
    """
    class Meta:
        name = "when"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
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
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
