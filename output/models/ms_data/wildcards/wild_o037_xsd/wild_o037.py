from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict

__NAMESPACE__ = "http://foobar"


@dataclass
class Foo:
    """
    :ivar www_w3_org_1999_xhtml_attributes:
    """
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    www_w3_org_1999_xhtml_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##local http://www.w3.org/1999/xhtml"
        )
    )
