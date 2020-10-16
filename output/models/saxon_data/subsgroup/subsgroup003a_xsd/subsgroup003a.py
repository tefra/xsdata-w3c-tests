from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.myexample.com/command"


@dataclass
class ActionType:
    """
    :ivar result:
    """
    result: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Action(ActionType):
    class Meta:
        namespace = "http://www.myexample.com/command"


@dataclass
class Command:
    """
    :ivar action:
    """
    class Meta:
        namespace = "http://www.myexample.com/command"

    action: List[Action] = field(
        default_factory=list,
        metadata={
            "name": "Action",
            "type": "Element",
            "min_occurs": 1,
        }
    )
