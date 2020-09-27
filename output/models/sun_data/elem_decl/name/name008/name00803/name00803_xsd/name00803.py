from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Aa111A2Aa:
    """
    :ivar value:
    """
    class Meta:
        name = "aa111a2Aa"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Aa22B3C:
    """
    :ivar value:
    """
    class Meta:
        name = "aa22B3c"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Aa34:
    """
    :ivar value:
    """
    class Meta:
        name = "aa3-4_"
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
    :ivar aa111a2_aa:
    :ivar aa22_b3c:
    :ivar aa3_4:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    aa111a2_aa: Optional[Aa111A2Aa] = field(
        default=None,
        metadata=dict(
            name="aa111a2Aa",
            type="Element",
            required=True
        )
    )
    aa22_b3c: Optional[Aa22B3C] = field(
        default=None,
        metadata=dict(
            name="aa22B3c",
            type="Element",
            required=True
        )
    )
    aa3_4: Optional[Aa34] = field(
        default=None,
        metadata=dict(
            name="aa3-4_",
            type="Element",
            required=True
        )
    )
