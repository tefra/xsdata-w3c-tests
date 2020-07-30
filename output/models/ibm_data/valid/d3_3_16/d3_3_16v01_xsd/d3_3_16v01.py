from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11"


@dataclass
class Root:
    """
    :ivar ele:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11"

    ele: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            max_length=4
        )
    )
