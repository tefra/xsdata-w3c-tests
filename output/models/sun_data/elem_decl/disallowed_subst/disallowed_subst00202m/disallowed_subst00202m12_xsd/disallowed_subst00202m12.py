from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass
class HeadType:
    ear: Optional[object] = field(
        default=None,
        metadata={
            "name": "Ear",
            "type": "Element",
            "namespace": "ElemDecl/disallowedSubst",
        },
    )
    eye: Optional[object] = field(
        default=None,
        metadata={
            "name": "Eye",
            "type": "Element",
            "namespace": "ElemDecl/disallowedSubst",
        },
    )


@dataclass
class Element0(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Element1(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Element10(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Element2(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Element3(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Element4(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Element5(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Element6(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Element7(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Element8(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Element9(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Head(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/disallowedSubst"

    head: list[Head] = field(
        default_factory=list,
        metadata={
            "name": "Head",
            "type": "Element",
            "min_occurs": 1,
        },
    )
