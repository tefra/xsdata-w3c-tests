from dataclasses import dataclass, field
from typing import Dict

__NAMESPACE__ = "urn:foo"


@dataclass
class Base:
    """
    :ivar a_b_attributes:
    """
    class Meta:
        name = "base"

    a_b_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "urn:a urn:b",
        }
    )


@dataclass
class Alias(Base):
    class Meta:
        name = "alias"
        namespace = "urn:foo"


@dataclass
class Extension(Base):
    """
    :ivar c_attributes:
    """
    class Meta:
        name = "extension"
        namespace = "urn:foo"

    c_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "urn:c",
        }
    )


@dataclass
class Restriction(Base):
    """
    :ivar a_attributes:
    """
    class Meta:
        name = "restriction"
        namespace = "urn:foo"

    a_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "urn:a",
        }
    )
