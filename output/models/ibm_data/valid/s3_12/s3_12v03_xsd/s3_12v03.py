from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://xstest-tns"


@dataclass
class TitleType:
    class Meta:
        name = "titleType"

    type_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    title: List[Union["Root.TypeText", "Root.TypeNumber", TitleType]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )

    @dataclass
    class TypeText(TitleType):
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Attribute",
            },
        )

    @dataclass
    class TypeNumber(TitleType):
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Attribute",
            },
        )
