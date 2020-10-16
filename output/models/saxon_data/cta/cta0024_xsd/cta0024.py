from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://cta023.com/ns"


@dataclass
class Event:
    """
    :ivar when:
    :ivar type:
    """
    class Meta:
        name = "event"
        namespace = "http://cta023.com/ns"

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
        namespace = "http://cta023.com/ns"

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
        namespace = "http://cta023.com/ns"

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
