from dataclasses import dataclass, field
from typing import Union

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass
class Type:
    pass


@dataclass
class Head(Type):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class DerivedFromType(Type):
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

    member1_or_head: list[Union[Member1, Head]] = field(
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
