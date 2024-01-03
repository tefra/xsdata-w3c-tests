from dataclasses import dataclass, field
from typing import List, Optional, Union, Any

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
class MixedTitleType(TitleType):
    class Meta:
        name = "mixedTitleType"

    content: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    value: Union[int, str] = field(default="")


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    title: List[
        Union[TitleType, MixedTitleType, "Root.TypeText", "Root.TypeNumber"]
    ] = field(
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
        content: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        value: str = field(default="")

    @dataclass
    class TypeNumber(TitleType):
        content: Any = field(
            init=False,
            metadata={
                "type": "Ignore",
            },
        )
        value: Optional[int] = field(default=None)
