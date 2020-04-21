from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict

__NAMESPACE__ = "urn:foo"


@dataclass
class Emptywc:
    """
    :ivar a_attributes:
    :ivar b_attributes:
    """
    class Meta:
        name = "emptywc"
        namespace = "urn:foo"

    a_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="urn:a"
        )
    )
    b_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="urn:b"
        )
    )


@dataclass
class JustA:
    """
    :ivar a_attributes:
    :ivar b_urn_c_attributes:
    """
    class Meta:
        name = "justA"
        namespace = "urn:foo"

    a_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="urn:a"
        )
    )
    b_urn_c_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="urn:a urn:b urn:c"
        )
    )
