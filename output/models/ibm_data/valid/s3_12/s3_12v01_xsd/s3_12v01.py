from dataclasses import dataclass, field
from typing import Any, Optional, Union

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
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class IntegerTitleType(TitleType):
    class Meta:
        name = "integerTitleType"

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: Optional[int] = field(default=None)


@dataclass
class MixedTitleType(TitleType):
    class Meta:
        name = "mixedTitleType"

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: Union[int, str] = field(default="")


@dataclass
class StringTitleType(TitleType):
    class Meta:
        name = "stringTitleType"

    content: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value: str = field(default="")


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    title: list[
        Union[TitleType, StringTitleType, IntegerTitleType, MixedTitleType]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )
