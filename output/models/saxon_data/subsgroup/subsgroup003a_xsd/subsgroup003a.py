from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.myexample.com/command"


@dataclass
class ActionType:
    result: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Command:
    class Meta:
        namespace = "http://www.myexample.com/command"
