from dataclasses import dataclass, field
from typing import List, Union

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass
class TypeType:
    class Meta:
        name = "Type"


@dataclass
class Head(TypeType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class DerivedFromType(TypeType):
    class Meta:
        name = "derivedFromType"


@dataclass
class Member1(DerivedFromType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/disallowedSubst"

    member1_or_head: List[Union[Member1, Head]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Member1",
                    "type": Member1,
                },
                {
                    "name": "Head",
                    "type": Head,
                },
            ),
        },
    )
