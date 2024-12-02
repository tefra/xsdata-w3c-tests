from dataclasses import dataclass, field
from typing import Union

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
class Container1:
    class Meta:
        name = "CONTAINER"

    choice: list[Union[G, F, E, D, C, B, A]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "g",
                    "type": G,
                    "namespace": "http://www.microsoft.com/schema/1",
                },
                {
                    "name": "f",
                    "type": F,
                    "namespace": "http://www.microsoft.com/schema/1",
                },
                {
                    "name": "e",
                    "type": E,
                    "namespace": "http://www.microsoft.com/schema/1",
                },
                {
                    "name": "d",
                    "type": D,
                    "namespace": "http://www.microsoft.com/schema/1",
                },
                {
                    "name": "c",
                    "type": C,
                    "namespace": "http://www.microsoft.com/schema/1",
                },
                {
                    "name": "b",
                    "type": B,
                    "namespace": "http://www.microsoft.com/schema/1",
                },
                {
                    "name": "a",
                    "type": A,
                    "namespace": "http://www.microsoft.com/schema/1",
                },
            ),
        },
    )


@dataclass
class Container(Container1):
    class Meta:
        name = "container"
        namespace = "http://www.microsoft.com/schema/1"
