from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


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


@dataclass
class ArcType:
    """
    :ivar title:
    :ivar type:
    :ivar arcrole:
    :ivar title_attribute:
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
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: TypeType = field(
        init=False,
        default=TypeType.ARC,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
        )
    )
    title_attribute: Optional[str] = field(
        default=None,
        metadata=dict(
            name="title",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata=dict(
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
    :ivar title_attribute:
    """
    class Meta:
        name = "extended"

    title: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    resource: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    locator: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    arc: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: TypeType = field(
        init=False,
        default=TypeType.EXTENDED,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    role: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
        )
    )
    title_attribute: Optional[str] = field(
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
    :ivar title_attribute:
    :ivar label: label is not required, but locators have no particular
         XLink function if they are not labeled.
    """
    class Meta:
        name = "locatorType"

    title: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: TypeType = field(
        init=False,
        default=TypeType.LOCATOR,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    href: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    role: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
        )
    )
    title_attribute: Optional[str] = field(
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
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )


@dataclass
class ResourceType:
    """
    :ivar any_element:
    :ivar type:
    :ivar role:
    :ivar title:
    :ivar label:
    """
    class Meta:
        name = "resourceType"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: TypeType = field(
        init=False,
        default=TypeType.RESOURCE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    role: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    label: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )


@dataclass
class Simple:
    """Intended for use as the type of user-declared elements to make them simple
    links.

    :ivar any_element:
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

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    href: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    role: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
        )
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )


@dataclass
class TitleEltType:
    """
    :ivar any_element:
    :ivar type:
    :ivar lang: xml:lang is not required, but provides much of the
         motivation for title elements in addition to attributes, and so
         is provided here for convenience.
    """
    class Meta:
        name = "titleEltType"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: TypeType = field(
        init=False,
        default=TypeType.TITLE,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            required=True
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
