from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://xstest-tns"


@dataclass
class TitleType:
    """
    :ivar content:
    :ivar type:
    """
    class Meta:
        name = "titleType"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class IntegerTitleType(TitleType):
    """
    :ivar value:
    """
    class Meta:
        name = "integerTitleType"

    value: Optional[int] = field(
        default=None,
    )


@dataclass
class MixedTitleType(TitleType):
    """
    :ivar value:
    """
    class Meta:
        name = "mixedTitleType"

    value: Optional[Union[int, str]] = field(
        default=None,
    )


@dataclass
class StringTitleType(TitleType):
    """
    :ivar value:
    """
    class Meta:
        name = "stringTitleType"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class Root:
    """
    :ivar title:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    title: List[Union[IntegerTitleType, MixedTitleType, StringTitleType, TitleType]] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=5
        )
    )
