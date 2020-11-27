from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class ScopeType(Enum):
    CLASS_VALUE = "class"
    INSTANCE = "instance"


class YesNoType(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class EventType:
    desc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    scope: Optional[ScopeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PropertyType:
    desc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    scope: Optional[ScopeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class EventsType:
    event: List[EventType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ClassType:
    events: Optional[EventsType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    property: List[PropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    inherits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class JsmlDocumentType:
    class_value: List[ClassType] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Jsml(JsmlDocumentType):
    class Meta:
        name = "jsml"
