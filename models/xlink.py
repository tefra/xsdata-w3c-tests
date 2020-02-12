from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional


class Actuate(Enum):
    """
    :cvar ON_LOAD:
    :cvar ON_REQUEST:
    :cvar OTHER:
    :cvar NONE_VALUE:
    """
    ON_LOAD = "onLoad"
    ON_REQUEST = "onRequest"
    OTHER = "other"
    NONE_VALUE = "none"


class ActuateType(Enum):
    """
    :cvar ON_LOAD:
    :cvar ON_REQUEST:
    :cvar OTHER:
    :cvar NONE_VALUE:
    """
    ON_LOAD = "onLoad"
    ON_REQUEST = "onRequest"
    OTHER = "other"
    NONE_VALUE = "none"


@dataclass
class ArcType:
    """
    :ivar title:
    :ivar type:
    :ivar arcrole:
    :ivar title:
    :ivar show:
    :ivar actuate:
    :ivar from_value:
    :ivar to: from and to have default behavior when values are missing
    """
    class Meta:
        name = "arcType"

    title: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="title",
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata=dict(
            name="arcrole",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="title",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    show: Optional[str] = field(
        default=None,
        metadata=dict(
            name="show",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    actuate: Optional[str] = field(
        default=None,
        metadata=dict(
            name="actuate",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    from_value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="from",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    to: Optional[str] = field(
        default=None,
        metadata=dict(
            name="to",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )


@dataclass
class Extended:
    """Intended for use as the type of user-declared elements to make them extended
    links. Note that the elements referenced in the content model are all abstract.
    The intention is that by simply declaring elements with these as their
    substitutionGroup, all the right things will happen.

    :ivar title:
    :ivar resource:
    :ivar locator:
    :ivar arc:
    :ivar type:
    :ivar role:
    :ivar title:
    """
    class Meta:
        name = "extended"

    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="title",
            type="Element",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    resource: Optional[str] = field(
        default=None,
        metadata=dict(
            name="resource",
            type="Element",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    locator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="locator",
            type="Element",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    arc: Optional[str] = field(
        default=None,
        metadata=dict(
            name="arc",
            type="Element",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    role: Optional[str] = field(
        default=None,
        metadata=dict(
            name="role",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="title",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )


@dataclass
class LocatorType:
    """
    :ivar title:
    :ivar type:
    :ivar href:
    :ivar role:
    :ivar title:
    :ivar label: label is not required, but locators have no particular
         XLink function if they are not labeled.
    """
    class Meta:
        name = "locatorType"

    title: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="title",
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    href: Optional[str] = field(
        default=None,
        metadata=dict(
            name="href",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    role: Optional[str] = field(
        default=None,
        metadata=dict(
            name="role",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="title",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    label: Optional[str] = field(
        default=None,
        metadata=dict(
            name="label",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )


@dataclass
class ResourceType:
    """
    :ivar elements:
    :ivar type:
    :ivar role:
    :ivar title:
    :ivar label:
    """
    class Meta:
        name = "resourceType"
        mixed = True

    elements: List[object] = field(
        default_factory=list,
        metadata=dict(
            name="elements",
            type="Any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    role: Optional[str] = field(
        default=None,
        metadata=dict(
            name="role",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="title",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    label: Optional[str] = field(
        default=None,
        metadata=dict(
            name="label",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )


class Show(Enum):
    """
    :cvar NEW:
    :cvar REPLACE:
    :cvar EMBED:
    :cvar OTHER:
    :cvar NONE_VALUE:
    """
    NEW = "new"
    REPLACE = "replace"
    EMBED = "embed"
    OTHER = "other"
    NONE_VALUE = "none"


class ShowType(Enum):
    """
    :cvar NEW:
    :cvar REPLACE:
    :cvar EMBED:
    :cvar OTHER:
    :cvar NONE_VALUE:
    """
    NEW = "new"
    REPLACE = "replace"
    EMBED = "embed"
    OTHER = "other"
    NONE_VALUE = "none"


@dataclass
class Simple:
    """Intended for use as the type of user-declared elements to make them simple
    links.

    :ivar elements:
    :ivar type:
    :ivar href:
    :ivar role:
    :ivar arcrole:
    :ivar title:
    :ivar show:
    :ivar actuate:
    """
    class Meta:
        name = "simple"
        mixed = True

    elements: List[object] = field(
        default_factory=list,
        metadata=dict(
            name="elements",
            type="Any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    href: Optional[str] = field(
        default=None,
        metadata=dict(
            name="href",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    role: Optional[str] = field(
        default=None,
        metadata=dict(
            name="role",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata=dict(
            name="arcrole",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="title",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    show: Optional[str] = field(
        default=None,
        metadata=dict(
            name="show",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    actuate: Optional[str] = field(
        default=None,
        metadata=dict(
            name="actuate",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )


@dataclass
class TitleEltType:
    """
    :ivar elements:
    :ivar type:
    :ivar lang: xml:lang is not required, but provides much of the
         motivation for title elements in addition to attributes, and so
         is provided here for convenience.
    """
    class Meta:
        name = "titleEltType"
        mixed = True

    elements: List[object] = field(
        default_factory=list,
        metadata=dict(
            name="elements",
            type="Any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lang",
            type="Attribute"
        )
    )


class Type(Enum):
    """
    :cvar SIMPLE:
    :cvar EXTENDED:
    :cvar TITLE:
    :cvar RESOURCE:
    :cvar LOCATOR:
    :cvar ARC:
    """
    SIMPLE = "simple"
    EXTENDED = "extended"
    TITLE = "title"
    RESOURCE = "resource"
    LOCATOR = "locator"
    ARC = "arc"


class TypeType(Enum):
    """
    :cvar SIMPLE:
    :cvar EXTENDED:
    :cvar TITLE:
    :cvar RESOURCE:
    :cvar LOCATOR:
    :cvar ARC:
    """
    SIMPLE = "simple"
    EXTENDED = "extended"
    TITLE = "title"
    RESOURCE = "resource"
    LOCATOR = "locator"
    ARC = "arc"
