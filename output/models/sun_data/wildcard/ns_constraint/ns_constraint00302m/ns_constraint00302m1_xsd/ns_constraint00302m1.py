from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict

__NAMESPACE__ = "nsConstraint"


@dataclass
class A:
    """
    :ivar ns_test1_ns_test2_attributes:
    """
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    ns_test1_ns_test2_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="ns_test1 ns_test2"
        )
    )
