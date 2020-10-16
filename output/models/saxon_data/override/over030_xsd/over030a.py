from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://example.org/ns/document"


@dataclass
class InlineType:
    """
    :ivar content:
    :ivar phrase:
    :ivar superscript:
    :ivar subscript:
    :ivar abbrev:
    :ivar emphasis:
    :ivar property:
    :ivar role:
    :ivar id:
    :ivar base:
    """
    class Meta:
        name = "inline.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    phrase: Optional["Phrase"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    superscript: Optional["Superscript"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    subscript: Optional["Subscript"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    abbrev: Optional["Abbrev"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    emphasis: Optional["Emphasis"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    property: Optional["Property"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Xsdextra:
    """
    :ivar any_element:
    """
    class Meta:
        name = "xsdextra"
        namespace = "http://example.org/ns/document"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Abbrev(InlineType):
    class Meta:
        name = "abbrev"
        namespace = "http://example.org/ns/document"


@dataclass
class Emphasis(InlineType):
    class Meta:
        name = "emphasis"
        namespace = "http://example.org/ns/document"


@dataclass
class Phrase(InlineType):
    class Meta:
        name = "phrase"
        namespace = "http://example.org/ns/document"


@dataclass
class Property(InlineType):
    class Meta:
        name = "property"
        namespace = "http://example.org/ns/document"


@dataclass
class Subscript(InlineType):
    class Meta:
        name = "subscript"
        namespace = "http://example.org/ns/document"


@dataclass
class Superscript(InlineType):
    class Meta:
        name = "superscript"
        namespace = "http://example.org/ns/document"


@dataclass
class Title(InlineType):
    class Meta:
        name = "title"
        namespace = "http://example.org/ns/document"


@dataclass
class Blockquote:
    """
    :ivar title:
    :ivar p:
    :ivar role:
    :ivar id:
    :ivar base:
    """
    class Meta:
        name = "blockquote"
        namespace = "http://example.org/ns/document"

    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    p: Optional["P"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class ParaType:
    """
    :ivar content:
    :ivar phrase:
    :ivar superscript:
    :ivar subscript:
    :ivar abbrev:
    :ivar emphasis:
    :ivar property:
    :ivar blockquote:
    :ivar role:
    :ivar id:
    :ivar base:
    """
    class Meta:
        name = "para.type"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    phrase: Optional[Phrase] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    superscript: Optional[Superscript] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    subscript: Optional[Subscript] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    abbrev: Optional[Abbrev] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    emphasis: Optional[Emphasis] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    property: Optional[Property] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    blockquote: Optional[Blockquote] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://example.org/ns/document",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class P(ParaType):
    class Meta:
        name = "p"
        namespace = "http://example.org/ns/document"


@dataclass
class Doc:
    """
    :ivar title:
    :ivar xsdextra:
    :ivar p:
    :ivar blockquote:
    :ivar role:
    :ivar id:
    :ivar base:
    """
    class Meta:
        name = "doc"
        namespace = "http://example.org/ns/document"

    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    xsdextra: Optional[Xsdextra] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    p: List[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    blockquote: List[Blockquote] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
