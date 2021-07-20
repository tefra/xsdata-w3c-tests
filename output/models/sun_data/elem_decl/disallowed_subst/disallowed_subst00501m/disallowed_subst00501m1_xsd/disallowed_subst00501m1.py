from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass
class Head:
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Member1:
    class Meta:
        namespace = "ElemDecl/disallowedSubst"

    value: Optional[str] = field(
        default=None
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/disallowedSubst"

    member1: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Member1",
            "type": "Element",
        }
    )
    head: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Head",
            "type": "Element",
        }
    )
