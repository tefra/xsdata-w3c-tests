from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


class ActuateType(Enum):
    """
    :cvar NONE_VALUE:
    :cvar ON_LOAD:
    :cvar ON_REQUEST:
    :cvar OTHER:
    """
    NONE_VALUE = "none"
    ON_LOAD = "onLoad"
    ON_REQUEST = "onRequest"
    OTHER = "other"


class ShowType(Enum):
    """
    :cvar EMBED:
    :cvar NEW:
    :cvar NONE_VALUE:
    :cvar OTHER:
    :cvar REPLACE:
    """
    EMBED = "embed"
    NEW = "new"
    NONE_VALUE = "none"
    OTHER = "other"
    REPLACE = "replace"


class TypeType(Enum):
    """
    :cvar ARC:
    :cvar EXTENDED:
    :cvar LOCATOR:
    :cvar RESOURCE:
    :cvar SIMPLE:
    :cvar TITLE:
    """
    ARC = "arc"
    EXTENDED = "extended"
    LOCATOR = "locator"
    RESOURCE = "resource"
    SIMPLE = "simple"
    TITLE = "title"


@dataclass
class ArcType:
    """
    :ivar www_w3_org_1999_xlink_title:
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

    www_w3_org_1999_xlink_title: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="title",
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: TypeType = field(
        init=False,
        default="arc",
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
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
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
    show: Optional[ShowType] = field(
        default=None,
        metadata=dict(
            name="show",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    actuate: Optional[ActuateType] = field(
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

    :ivar www_w3_org_1999_xlink_title:
    :ivar resource:
    :ivar locator:
    :ivar arc:
    :ivar type:
    :ivar role:
    :ivar title:
    """
    class Meta:
        name = "extended"

    www_w3_org_1999_xlink_title: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="title",
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    resource: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="resource",
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    locator: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="locator",
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    arc: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="arc",
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: TypeType = field(
        init=False,
        default="extended",
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
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
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
    :ivar www_w3_org_1999_xlink_title:
    :ivar type:
    :ivar href:
    :ivar role:
    :ivar title:
    :ivar label: label is not required, but locators have no particular
         XLink function if they are not labeled.
    """
    class Meta:
        name = "locatorType"

    www_w3_org_1999_xlink_title: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="title",
            type="Element",
            namespace="http://www.w3.org/1999/xlink",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: TypeType = field(
        init=False,
        default="locator",
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
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
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
        default="resource",
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
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
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
        default="simple",
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
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
        )
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata=dict(
            name="arcrole",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink",
            min_length=1.0
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
    show: Optional[ShowType] = field(
        default=None,
        metadata=dict(
            name="show",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    actuate: Optional[ActuateType] = field(
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
        default="title",
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
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
