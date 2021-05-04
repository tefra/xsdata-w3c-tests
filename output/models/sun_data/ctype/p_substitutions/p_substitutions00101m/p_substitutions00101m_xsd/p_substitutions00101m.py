from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "pSubstitutions"


@dataclass
class A:
    c: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )


@dataclass
class B(A):
    d: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class C(A):
    pass


@dataclass
class E(A):
    class Meta:
        name = "e"
        namespace = "pSubstitutions"
