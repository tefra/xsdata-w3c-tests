from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://example.org/ns/document"


@dataclass(kw_only=True)
class InlineType:
    class Meta:
        name = "inline.type"

    role: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    base: None | str = field(
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


@dataclass(kw_only=True)
class Xsdextra:
    class Meta:
        name = "xsdextra"
        namespace = "http://example.org/ns/document"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Abbrev(InlineType):
    class Meta:
        name = "abbrev"
        namespace = "http://example.org/ns/document"


@dataclass(kw_only=True)
class Emphasis(InlineType):
    class Meta:
        name = "emphasis"
        namespace = "http://example.org/ns/document"


@dataclass(kw_only=True)
class Phrase(InlineType):
    class Meta:
        name = "phrase"
        namespace = "http://example.org/ns/document"


@dataclass(kw_only=True)
class Property(InlineType):
    class Meta:
        name = "property"
        namespace = "http://example.org/ns/document"


@dataclass(kw_only=True)
class Subscript(InlineType):
    class Meta:
        name = "subscript"
        namespace = "http://example.org/ns/document"


@dataclass(kw_only=True)
class Superscript(InlineType):
    class Meta:
        name = "superscript"
        namespace = "http://example.org/ns/document"


@dataclass(kw_only=True)
class Title(InlineType):
    class Meta:
        name = "title"
        namespace = "http://example.org/ns/document"


@dataclass(kw_only=True)
class ParaType:
    class Meta:
        name = "para.type"

    role: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    base: None | str = field(
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


@dataclass(kw_only=True)
class P(ParaType):
    class Meta:
        name = "p"
        namespace = "http://example.org/ns/document"


@dataclass(kw_only=True)
class Blockquote:
    class Meta:
        name = "blockquote"
        namespace = "http://example.org/ns/document"

    title: None | Title = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p: P = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    role: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://example.org/ns/document"

    title: Title = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    xsdextra: None | Xsdextra = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    p_or_blockquote: list[P | Blockquote] = field(
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
    role: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
