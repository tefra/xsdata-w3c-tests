from dataclasses import dataclass, field
from typing import List, Optional, Type

__NAMESPACE__ = "http://example.org/ns/document"


@dataclass
class InlineType:
    """
    :ivar content:
    :ivar choice:
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
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "phrase",
                    "type": Type["Phrase"],
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "superscript",
                    "type": Type["Superscript"],
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "subscript",
                    "type": Type["Subscript"],
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "abbrev",
                    "type": Type["Abbrev"],
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "emphasis",
                    "type": Type["Emphasis"],
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "property",
                    "type": Type["Property"],
                    "namespace": "http://example.org/ns/document",
                },
            ),
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
    :ivar choice:
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
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "phrase",
                    "type": Phrase,
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "superscript",
                    "type": Superscript,
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "subscript",
                    "type": Subscript,
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "abbrev",
                    "type": Abbrev,
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "emphasis",
                    "type": Emphasis,
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "property",
                    "type": Property,
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                    "namespace": "http://example.org/ns/document",
                },
            ),
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
    :ivar p_or_blockquote:
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
    p_or_blockquote: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "p",
                    "type": P,
                },
                {
                    "name": "blockquote",
                    "type": Blockquote,
                },
            ),
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
