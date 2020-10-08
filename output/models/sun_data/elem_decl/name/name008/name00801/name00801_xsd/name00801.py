from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class AA:
    """
    :ivar value:
    """
    class Meta:
        name = "a--a"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class BB:
    """
    :ivar value:
    """
    class Meta:
        name = "b..b"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class CC:
    """
    :ivar value:
    """
    class Meta:
        name = "c__c"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class DD:
    """
    :ivar value:
    """
    class Meta:
        name = "d··d"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class EE:
    """
    :ivar value:
    """
    class Meta:
        name = "e··e"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class FF:
    """
    :ivar value:
    """
    class Meta:
        name = "f۝۝f"
        namespace = "ElemDecl/name"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class GG:
    """
    :ivar value:
    """
    class Meta:
        name = "g۞۞g"
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
    :ivar a_a:
    :ivar b_b:
    :ivar c_c:
    :ivar d_d:
    :ivar e_e:
    :ivar f_f:
    :ivar g_g:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    a_a: Optional[int] = field(
        default=None,
        metadata=dict(
            name="a--a",
            type="Element",
            required=True
        )
    )
    b_b: Optional[int] = field(
        default=None,
        metadata=dict(
            name="b..b",
            type="Element",
            required=True
        )
    )
    c_c: Optional[int] = field(
        default=None,
        metadata=dict(
            name="c__c",
            type="Element",
            required=True
        )
    )
    d_d: Optional[int] = field(
        default=None,
        metadata=dict(
            name="d··d",
            type="Element",
            required=True
        )
    )
    e_e: Optional[int] = field(
        default=None,
        metadata=dict(
            name="e··e",
            type="Element",
            required=True
        )
    )
    f_f: Optional[int] = field(
        default=None,
        metadata=dict(
            name="f۝۝f",
            type="Element",
            required=True
        )
    )
    g_g: Optional[int] = field(
        default=None,
        metadata=dict(
            name="g۞۞g",
            type="Element",
            required=True
        )
    )
