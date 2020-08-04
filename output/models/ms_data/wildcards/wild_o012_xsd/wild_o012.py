from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "http://foobar"


@dataclass
class Foo:
    """
    :ivar value:
    :ivar target_namespace_w3_org_1999_xhtml_attributes:
    """
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    value: Optional[str] = field(
        default=None,
    )
    target_namespace_w3_org_1999_xhtml_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##targetNamespace http://www.w3.org/1999/xhtml"
        )
    )
