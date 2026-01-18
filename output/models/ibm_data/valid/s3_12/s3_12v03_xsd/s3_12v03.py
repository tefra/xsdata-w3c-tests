from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns"


@dataclass(kw_only=True)
class TitleType:
    class Meta:
        name = "titleType"

    type_value: None | object = field(
        default=None,
        metadata={
            "name": "type",
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
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    title: list[Root.TypeText | Root.TypeNumber | TitleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )

    @dataclass(kw_only=True)
    class TypeText(TitleType):
        type_value: None | str = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class TypeNumber(TitleType):
        type_value: None | str = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Attribute",
            },
        )
