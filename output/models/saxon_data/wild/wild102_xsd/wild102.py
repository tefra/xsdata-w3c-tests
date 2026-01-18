from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://example.com/sample"


@dataclass(kw_only=True)
class P:
    class Meta:
        name = "p"
        namespace = "http://example.com/sample"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Wrapper:
    class Meta:
        name = "wrapper"
        namespace = "http://example.com/sample"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Note:
    class Meta:
        name = "note"
        namespace = "http://example.com/sample"

    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://example.com/sample"

    note_or_wrapper: list[Note | Wrapper] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "note",
                    "type": Note,
                },
                {
                    "name": "wrapper",
                    "type": Wrapper,
                },
            ),
        },
    )
