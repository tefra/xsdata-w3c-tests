from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict

__NAMESPACE__ = "http://foobar"


@dataclass
class Foo:
    """
    :ivar foobar_attributes:
    """
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    foobar_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local http://foobar"
        )
    )
