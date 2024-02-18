from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Aa111A2Aa:
    class Meta:
        name = "aa111a2Aa"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Aa22B3C:
    class Meta:
        name = "aa22B3c"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Aa34:
    class Meta:
        name = "aa3-4_"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    aa111a2_aa: Optional[Aa111A2Aa] = field(
        default=None,
        metadata={
            "name": "aa111a2Aa",
            "type": "Element",
            "required": True,
        },
    )
    aa22_b3c: Optional[Aa22B3C] = field(
        default=None,
        metadata={
            "name": "aa22B3c",
            "type": "Element",
            "required": True,
        },
    )
    aa3_4: Optional[Aa34] = field(
        default=None,
        metadata={
            "name": "aa3-4_",
            "type": "Element",
            "required": True,
        },
    )
