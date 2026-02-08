from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/name"


@dataclass(kw_only=True)
class A1234561:
    class Meta:
        name = "a-1.2_3·4·5۝6۞"
        namespace = "ElemDecl/name"

    value: int = field()


@dataclass(kw_only=True)
class A1234562:
    class Meta:
        name = "a123456"
        namespace = "ElemDecl/name"

    value: int = field()


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    a_1_2_3_4_5_6: A1234561 = field(
        metadata={
            "name": "a-1.2_3·4·5۝6۞",
            "type": "Element",
        }
    )
    elem_decl_name_a123456: A1234562 = field(
        metadata={
            "name": "a123456",
            "type": "Element",
        }
    )
