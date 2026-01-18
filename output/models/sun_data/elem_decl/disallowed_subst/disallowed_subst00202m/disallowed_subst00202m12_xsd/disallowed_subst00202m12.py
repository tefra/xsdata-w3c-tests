from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class HeadType:
    ear: None | object = field(
        default=None,
        metadata={
            "name": "Ear",
            "type": "Element",
            "namespace": "ElemDecl/disallowedSubst",
        },
    )
    eye: None | object = field(
        default=None,
        metadata={
            "name": "Eye",
            "type": "Element",
            "namespace": "ElemDecl/disallowedSubst",
        },
    )


@dataclass(kw_only=True)
class Element0(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Element1(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Element10(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Element2(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Element3(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Element4(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Element5(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Element6(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Element7(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Element8(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Element9(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
class Head(HeadType):
    class Meta:
        namespace = "ElemDecl/disallowedSubst"


@dataclass(kw_only=True)
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
