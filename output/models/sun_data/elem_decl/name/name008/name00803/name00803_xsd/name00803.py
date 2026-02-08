from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/name"


@dataclass(kw_only=True)
class Aa111A2Aa:
    class Meta:
        name = "aa111a2Aa"
        namespace = "ElemDecl/name"

    value: int = field()


@dataclass(kw_only=True)
class Aa22B3C:
    class Meta:
        name = "aa22B3c"
        namespace = "ElemDecl/name"

    value: int = field()


@dataclass(kw_only=True)
class Aa34:
    class Meta:
        name = "aa3-4_"
        namespace = "ElemDecl/name"

    value: int = field()


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    aa111a2_aa: Aa111A2Aa = field(
        metadata={
            "name": "aa111a2Aa",
            "type": "Element",
        }
    )
    aa22_b3c: Aa22B3C = field(
        metadata={
            "name": "aa22B3c",
            "type": "Element",
        }
    )
    aa3_4: Aa34 = field(
        metadata={
            "name": "aa3-4_",
            "type": "Element",
        }
    )
