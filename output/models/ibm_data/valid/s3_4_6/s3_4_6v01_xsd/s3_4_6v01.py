from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_6"


@dataclass
class C:
    """
    :ivar a:
    :ivar any_element:
    """
    class Meta:
        name = "c"

    a: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=1,
            max_occurs=3
        )
    )


@dataclass
class Root(C):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_6"
