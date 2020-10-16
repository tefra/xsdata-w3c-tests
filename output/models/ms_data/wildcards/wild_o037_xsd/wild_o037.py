from dataclasses import dataclass, field
from typing import Dict

__NAMESPACE__ = "http://foobar"


@dataclass
class Foo:
    """
    :ivar local_w3_org_1999_xhtml_attributes:
    """
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    local_w3_org_1999_xhtml_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local http://www.w3.org/1999/xhtml",
        }
    )
