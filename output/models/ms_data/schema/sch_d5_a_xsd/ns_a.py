from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns-a"


@dataclass
class CtA:
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "ct-A"

    a1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a",
            required=True
        )
    )
    a2: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a",
            required=True
        )
    )


@dataclass
class CtB:
    """
    :ivar b1:
    :ivar b2:
    """
    class Meta:
        name = "ct-B"

    b1: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a",
            required=True
        )
    )
    b2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="ns-a",
            required=True
        )
    )


@dataclass
class CtC:
    """
    :ivar c1:
    :ivar c2:
    """
    class Meta:
        name = "ct-C"

    c1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    c2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class AE2(CtB):
    class Meta:
        name = "a-e2"
        namespace = "ns-a"


@dataclass
class AE3(CtC):
    class Meta:
        name = "a-e3"
        namespace = "ns-a"


@dataclass
class BE1(CtA):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"


@dataclass
class BE3(CtC):
    class Meta:
        name = "b-e3"
        namespace = "ns-a"


@dataclass
class CE1(CtA):
    class Meta:
        name = "c-e1"
        namespace = "ns-a"


@dataclass
class CE2(CtB):
    class Meta:
        name = "c-e2"
        namespace = "ns-a"


@dataclass
class E1(CtA):
    class Meta:
        name = "e1"
        namespace = "ns-a"


@dataclass
class E2(CtB):
    class Meta:
        name = "e2"
        namespace = "ns-a"


@dataclass
class E3(CtC):
    class Meta:
        name = "e3"
        namespace = "ns-a"
