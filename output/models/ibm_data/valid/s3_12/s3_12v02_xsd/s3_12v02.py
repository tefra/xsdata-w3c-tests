from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://xstest-tns"


@dataclass
class TitleType:
    class Meta:
        name = "titleType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MixedTitleType(TitleType):
    class Meta:
        name = "mixedTitleType"

    value: Optional[Union[int, str]] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    title: List[Union[TitleType, MixedTitleType, "Root.TypeText", "Root.TypeNumber"]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )

    @dataclass
    class TypeText(TitleType):
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            }
        )

    @dataclass
    class TypeNumber(TitleType):
        value: Optional[int] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
