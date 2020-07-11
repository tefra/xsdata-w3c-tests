from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    """
    :ivar local_target_namespace_foo_imported_xsd_bar_element:
    """
    local_target_namespace_foo_imported_xsd_bar_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##local ##targetNamespace foo http://importedXSD bar",
            min_occurs=1,
            max_occurs=4
        )
    )


@dataclass
class R(B):
    """
    :ivar e1:
    """
    e1: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=2,
            max_occurs=3
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[R] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
