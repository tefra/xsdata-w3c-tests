from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.microsoft.com/schema/1"


@dataclass(kw_only=True)
class AType:
    class Meta:
        name = "A_TYPE"


@dataclass(kw_only=True)
class BType(AType):
    class Meta:
        name = "B_TYPE"


@dataclass(kw_only=True)
class A(AType):
    class Meta:
        name = "a"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass(kw_only=True)
class CType(BType):
    class Meta:
        name = "C_TYPE"


@dataclass(kw_only=True)
class B(BType):
    class Meta:
        name = "b"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass(kw_only=True)
class DType(CType):
    class Meta:
        name = "D_TYPE"


@dataclass(kw_only=True)
class C(CType):
    class Meta:
        name = "c"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass(kw_only=True)
class EType(DType):
    class Meta:
        name = "E_TYPE"


@dataclass(kw_only=True)
class D(DType):
    class Meta:
        name = "d"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass(kw_only=True)
class FType(EType):
    class Meta:
        name = "F_TYPE"


@dataclass(kw_only=True)
class E(EType):
    class Meta:
        name = "e"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass(kw_only=True)
class GType(FType):
    class Meta:
        name = "G_TYPE"


@dataclass(kw_only=True)
class F(FType):
    class Meta:
        name = "f"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass(kw_only=True)
class G(FType):
    class Meta:
        name = "g"
        namespace = "http://www.microsoft.com/schema/1"


@dataclass(kw_only=True)
class Container1:
    class Meta:
        name = "CONTAINER"

    choice: list[G | F | E | D | C | B | A] = field(
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


@dataclass(kw_only=True)
class Container(Container1):
    class Meta:
        name = "container"
        namespace = "http://www.microsoft.com/schema/1"
