from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "http://example.org/ns/document"


@dataclass
class InlineType:
    class Meta:
        name = "inline.type"

    role: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "phrase",
                    "type": ForwardRef("Phrase"),
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "superscript",
                    "type": ForwardRef("Superscript"),
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "subscript",
                    "type": ForwardRef("Subscript"),
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "abbrev",
                    "type": ForwardRef("Abbrev"),
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "emphasis",
                    "type": ForwardRef("Emphasis"),
                    "namespace": "http://example.org/ns/document",
                },
                {
                    "name": "property",
                    "type": ForwardRef("Property"),
                    "namespace": "http://example.org/ns/document",
                },
            ),
        },
    )


@dataclass
class Xsdextra:
    class Meta:
        name = "xsdextra"
        namespace = "http://example.org/ns/document"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
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
class ParaType:
    class Meta:
        name = "para.type"

    role: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
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
                    "type": ForwardRef("Blockquote"),
                    "namespace": "http://example.org/ns/document",
                },
            ),
        },
    )


@dataclass
class P(ParaType):
    class Meta:
        name = "p"
        namespace = "http://example.org/ns/document"


@dataclass
class Blockquote:
    class Meta:
        name = "blockquote"
        namespace = "http://example.org/ns/document"

    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p: Optional[P] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    role: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://example.org/ns/document"

    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    xsdextra: Optional[Xsdextra] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p_or_blockquote: list[Union[P, Blockquote]] = field(
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
        },
    )
    role: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
