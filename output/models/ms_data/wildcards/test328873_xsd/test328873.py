from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "a"


@dataclass
class Base2:
    """
    :ivar other_attributes:
    """
    class Meta:
        name = "base2"

    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Base3:
    """
    :ivar other_attributes:
    """
    class Meta:
        name = "base3"

    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Base4:
    """
    :ivar other_attributes:
    """
    class Meta:
        name = "base4"

    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Intersection1:
    """
    :ivar other_attributes:
    :ivar local_b_c_attributes:
    """
    class Meta:
        name = "intersection1"

    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    local_b_c_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local b c",
        }
    )


@dataclass
class Intersection2:
    """
    :ivar other_attributes:
    """
    class Meta:
        name = "intersection2"

    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Derived2(Base2):
    """
    :ivar b_c_attributes:
    """
    class Meta:
        name = "derived2"

    b_c_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "b c",
        }
    )


@dataclass
class Derived3(Base3):
    """
    :ivar target_namespace_local_b_c_attributes:
    """
    class Meta:
        name = "derived3"

    target_namespace_local_b_c_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##targetNamespace ##local b c",
        }
    )


@dataclass
class Derived4(Base4):
    """
    :ivar local_b_c_attributes:
    """
    class Meta:
        name = "derived4"

    local_b_c_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local b c",
        }
    )


@dataclass
class Derived5(Base4):
    """
    :ivar b_c_attributes:
    """
    class Meta:
        name = "derived5"

    b_c_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "b c",
        }
    )


@dataclass
class Sub5(Intersection1):
    class Meta:
        name = "sub5"
        namespace = "a"


@dataclass
class Sub6(Intersection2):
    class Meta:
        name = "sub6"
        namespace = "a"


@dataclass
class Base:
    """
    :ivar sub:
    :ivar sub2:
    :ivar sub3:
    :ivar sub4:
    :ivar sub5:
    :ivar sub6:
    :ivar other_attributes:
    """
    class Meta:
        name = "base"

    sub: Optional[Derived2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        }
    )
    sub2: Optional[Derived3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        }
    )
    sub3: Optional[Derived4] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        }
    )
    sub4: Optional[Derived5] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        }
    )
    sub5: Optional[Intersection1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        }
    )
    sub6: Optional[Intersection2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Sub(Derived2):
    class Meta:
        name = "sub"
        namespace = "a"


@dataclass
class Sub2(Derived3):
    class Meta:
        name = "sub2"
        namespace = "a"


@dataclass
class Sub3(Derived4):
    class Meta:
        name = "sub3"
        namespace = "a"


@dataclass
class Sub4(Derived5):
    class Meta:
        name = "sub4"
        namespace = "a"


@dataclass
class Derived(Base):
    """
    :ivar target_namespace_b_c_attributes:
    """
    class Meta:
        name = "derived"

    target_namespace_b_c_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##targetNamespace b c",
        }
    )


@dataclass
class Doc(Derived):
    class Meta:
        name = "doc"
        namespace = "a"
