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
class IntegerTitleType(TitleType):
    class Meta:
        name = "integerTitleType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
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
class StringTitleType(TitleType):
    class Meta:
        name = "stringTitleType"

    value: Optional[str] = field(
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

    title: List[Union[TitleType, StringTitleType, IntegerTitleType, MixedTitleType]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
