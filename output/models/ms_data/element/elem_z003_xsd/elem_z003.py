from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.microsoft.com/schema/1"


@dataclass
class AType:
    class Meta:
        name = "A_TYPE"


@dataclass
class BType(AType):
    class Meta:
        name = "B_TYPE"


@dataclass
class A(AType):
    class Meta:
        name = "a"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass
class CType(BType):
    class Meta:
        name = "C_TYPE"


@dataclass
class B(BType):
    class Meta:
        name = "b"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass
class DType(CType):
    class Meta:
        name = "D_TYPE"


@dataclass
class C(CType):
    class Meta:
        name = "c"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass
class EType(DType):
    class Meta:
        name = "E_TYPE"


@dataclass
class D(DType):
    class Meta:
        name = "d"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass
class FType(EType):
    class Meta:
        name = "F_TYPE"


@dataclass
class E(EType):
    class Meta:
        name = "e"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass
class GType(FType):
    class Meta:
        name = "G_TYPE"


@dataclass
class F(FType):
    class Meta:
        name = "f"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass
class G(FType):
    class Meta:
        name = "g"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass
class Container:
    """
    :ivar g:
    :ivar f:
    :ivar e:
    :ivar d:
    :ivar c:
    :ivar b:
    :ivar a:
    """
    class Meta:
        name = "CONTAINER"

    g: List[G] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.microsoft.com/schema/1",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    f: List[F] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.microsoft.com/schema/1",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e: List[E] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.microsoft.com/schema/1",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    d: List[D] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.microsoft.com/schema/1",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    c: List[C] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.microsoft.com/schema/1",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    b: List[B] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.microsoft.com/schema/1",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    a: List[A] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.microsoft.com/schema/1",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Container(Container):
    class Meta:
        name = "container"
        namespace = "http://www.microsoft.com/schema/1"
