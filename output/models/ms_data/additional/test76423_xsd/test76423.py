from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class ScopeType(Enum):
    CLASS = "class"
    INSTANCE = "instance"


@dataclass(kw_only=True)
class EventType:
    desc: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    scope: ScopeType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PropertyType:
    desc: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    scope: ScopeType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class EventsType:
    event: list[EventType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ClassType:
    events: None | EventsType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    property: list[PropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    inherits: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class JsmlDocumentType:
    class_value: list[ClassType] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Jsml(JsmlDocumentType):
    class Meta:
        name = "jsml"
