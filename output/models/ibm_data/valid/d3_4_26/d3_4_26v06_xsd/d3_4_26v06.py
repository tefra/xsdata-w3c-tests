from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_26_v06"


@dataclass
class Root:
    """
    :ivar el_duration:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_26_v06"

    el_duration: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elDuration",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )