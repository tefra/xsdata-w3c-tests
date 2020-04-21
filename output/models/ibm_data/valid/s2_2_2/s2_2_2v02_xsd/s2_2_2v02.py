from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xstest-tns/ibms3_3_6_v02"


@dataclass
class Elem0:
    """
    :ivar value:
    """
    class Meta:
        name = "elem0"
        namespace = "http://xstest-tns/ibms3_3_6_v02"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Elem1:
    """
    :ivar value:
    """
    class Meta:
        name = "elem1"
        namespace = "http://xstest-tns/ibms3_3_6_v02"

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
        namespace = "http://xstest-tns/ibms3_3_6_v02"

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
    :ivar elem0:
    :ivar elem1:
    """
    class Meta:
        name = "rootType"

    elem2: List[Elem2] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://xstest-tns/ibms3_3_6_v02",
            min_occurs=1,
            max_occurs=2
        )
    )
    elem0: Optional[Elem0] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xstest-tns/ibms3_3_6_v02",
            required=True
        )
    )
    elem1: Optional[Elem1] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xstest-tns/ibms3_3_6_v02",
            required=True
        )
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/ibms3_3_6_v02"
