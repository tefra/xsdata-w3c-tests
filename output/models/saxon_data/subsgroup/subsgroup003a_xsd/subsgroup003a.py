from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.myexample.com/command"


@dataclass(kw_only=True)
class ActionType:
    result: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Command:
    class Meta:
        namespace = "http://www.myexample.com/command"


@dataclass(kw_only=True)
class Action(ActionType):
    class Meta:
        namespace = "http://www.myexample.com/command"
