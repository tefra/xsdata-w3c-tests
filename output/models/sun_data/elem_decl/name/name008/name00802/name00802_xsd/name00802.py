from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class A1234561:
    class Meta:
        name = "a-1.2_3·4·5۝6۞"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class A1234562:
    class Meta:
        name = "a123456"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    a_1_2_3_4_5_6: Optional[int] = field(
        default=None,
        metadata={
            "name": "a-1.2_3·4·5۝6۞",
            "type": "Element",
        }
    )
    elem_decl_name_a123456: Optional[int] = field(
        default=None,
        metadata={
            "name": "a123456",
            "type": "Element",
        }
    )
