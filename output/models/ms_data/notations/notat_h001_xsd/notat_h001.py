from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class Foo:
    """
    :ivar foo_attributes:
    """
    class Meta:
        name = "foo"

    foo_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://foo"
        )
    )
