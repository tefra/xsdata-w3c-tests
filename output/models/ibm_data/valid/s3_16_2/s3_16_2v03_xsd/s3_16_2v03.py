from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/IBMd3_16v03"


@dataclass
class Root:
    """
    :ivar union_element:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/IBMd3_16v03"

    union_element: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[1-9][1-9]"
        )
    )
