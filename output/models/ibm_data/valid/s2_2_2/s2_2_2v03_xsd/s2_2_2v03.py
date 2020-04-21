from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/ibms3_3_6_v01"


@dataclass
class Elem1:
    """
    :ivar value:
    """
    class Meta:
        name = "elem1"
        namespace = "http://xstest-tns/ibms3_3_6_v01"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Elem2:
    """
    :ivar value:
    """
    class Meta:
        name = "elem2"
        namespace = "http://xstest-tns/ibms3_3_6_v01"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class RootType:
    """
    :ivar elem2:
    :ivar elem1:
    """
    class Meta:
        name = "rootType"

    elem2: Optional[Elem2] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xstest-tns/ibms3_3_6_v01",
            required=True
        )
    )
    elem1: Optional[Elem1] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xstest-tns/ibms3_3_6_v01",
            required=True
        )
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/ibms3_3_6_v01"
