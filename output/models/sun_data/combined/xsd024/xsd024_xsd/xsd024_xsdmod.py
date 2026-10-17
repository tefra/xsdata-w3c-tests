from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

__NAMESPACE__ = "http://foo.com"


class SimpleType(StrEnum):
    YES = "yes"
    NO = "no"


@dataclass(kw_only=True)
class ComplexType:
    class Meta:
        name = "complexType"

    root: None | Root = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://foo.com",
        },
    )
    att: None | SimpleType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://foo.com",
        },
    )


@dataclass(kw_only=True)
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "http://foo.com"
