from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class A123456:
    """
    :ivar value:
    """
    class Meta:
        name = "a-1.2_3·4·5۝6۞"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class A123456:
    """
    :ivar value:
    """
    class Meta:
        name = "a123456"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar a_1_2_3_4_5_6:
    :ivar a123456:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    a_1_2_3_4_5_6: Optional[A123456] = field(
        default=None,
        metadata=dict(
            name="a-1.2_3·4·5۝6۞",
            type="Element",
            required=True
        )
    )
    a123456: Optional[A123456] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
