from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.myexample.com/command"


@dataclass
class Action:
    """
    :ivar result:
    """
    class Meta:
        namespace = "http://www.myexample.com/command"

    result: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class Command:
    """
    :ivar action:
    """
    class Meta:
        namespace = "http://www.myexample.com/command"

    action: List[Action] = field(
        default_factory=list,
        metadata=dict(
            name="Action",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
