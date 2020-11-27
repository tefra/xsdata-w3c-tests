from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://foo.com"


class SimpleType(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class ComplexType:
    class Meta:
        name = "complexType"

    root: Optional["Root"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://foo.com",
        }
    )
    att: Optional[SimpleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://foo.com",
        }
    )


@dataclass
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "http://foo.com"
