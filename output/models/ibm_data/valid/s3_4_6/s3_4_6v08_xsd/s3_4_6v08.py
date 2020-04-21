from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_6"


@dataclass
class CmplxBase:
    """
    :ivar element1:
    :ivar element2:
    :ivar element3:
    :ivar element4:
    """
    class Meta:
        name = "cmplxBase"

    element1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    element2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    element3: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    element4: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Derived:
    """
    :ivar element4:
    :ivar element3:
    :ivar element2:
    :ivar element1:
    """
    class Meta:
        name = "derived"

    element4: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    element3: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    element2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    element1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Root(Derived):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_6"
