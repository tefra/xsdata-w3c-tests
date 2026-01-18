from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Base2:
    class Meta:
        name = "base2"

    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class Base3:
    class Meta:
        name = "base3"

    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class Base4:
    class Meta:
        name = "base4"

    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class Intersection1:
    class Meta:
        name = "intersection1"

    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    local_b_c_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local b c",
        },
    )


@dataclass(kw_only=True)
class Intersection2:
    class Meta:
        name = "intersection2"

    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class Derived2(Base2):
    class Meta:
        name = "derived2"

    b_c_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "b c",
        },
    )


@dataclass(kw_only=True)
class Derived3(Base3):
    class Meta:
        name = "derived3"

    target_namespace_local_b_c_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##targetNamespace ##local b c",
        },
    )


@dataclass(kw_only=True)
class Derived4(Base4):
    class Meta:
        name = "derived4"

    local_b_c_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local b c",
        },
    )


@dataclass(kw_only=True)
class Derived5(Base4):
    class Meta:
        name = "derived5"

    b_c_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "b c",
        },
    )


@dataclass(kw_only=True)
class Sub5(Intersection1):
    class Meta:
        name = "sub5"
        namespace = "a"


@dataclass(kw_only=True)
class Sub6(Intersection2):
    class Meta:
        name = "sub6"
        namespace = "a"


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    sub: None | Derived2 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        },
    )
    sub2: None | Derived3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        },
    )
    sub3: None | Derived4 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        },
    )
    sub4: None | Derived5 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        },
    )
    sub5: None | Intersection1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        },
    )
    sub6: None | Intersection2 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass(kw_only=True)
class Sub(Derived2):
    class Meta:
        name = "sub"
        namespace = "a"


@dataclass(kw_only=True)
class Sub2(Derived3):
    class Meta:
        name = "sub2"
        namespace = "a"


@dataclass(kw_only=True)
class Sub3(Derived4):
    class Meta:
        name = "sub3"
        namespace = "a"


@dataclass(kw_only=True)
class Sub4(Derived5):
    class Meta:
        name = "sub4"
        namespace = "a"


@dataclass(kw_only=True)
class Derived(Base):
    class Meta:
        name = "derived"

    target_namespace_b_c_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##targetNamespace b c",
        },
    )


@dataclass(kw_only=True)
class Doc(Derived):
    class Meta:
        name = "doc"
        namespace = "a"
