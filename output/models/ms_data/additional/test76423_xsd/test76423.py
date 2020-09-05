from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class ScopeType(Enum):
    """
    :cvar CLASS_VALUE:
    :cvar INSTANCE:
    """
    CLASS_VALUE = "class"
    INSTANCE = "instance"


class YesNoType(Enum):
    """
    :cvar YES:
    :cvar NO:
    """
    YES = "yes"
    NO = "no"


@dataclass
class EventType:
    """
    :ivar desc:
    :ivar name:
    :ivar scope:
    """
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    scope: Optional[ScopeType] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class PropertyType:
    """
    :ivar desc:
    :ivar name:
    :ivar scope:
    :ivar type:
    """
    desc: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    scope: Optional[ScopeType] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class EventsType:
    """
    :ivar event:
    """
    event: List[EventType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class ClassType:
    """
    :ivar events:
    :ivar property:
    :ivar name:
    :ivar inherits:
    """
    events: Optional[EventsType] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
    property: List[PropertyType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    inherits: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class JsmlDocumentType:
    """
    :ivar class_value:
    """
    class_value: List[ClassType] = field(
        default_factory=list,
        metadata=dict(
            name="class",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Jsml(JsmlDocumentType):
    class Meta:
        name = "jsml"
