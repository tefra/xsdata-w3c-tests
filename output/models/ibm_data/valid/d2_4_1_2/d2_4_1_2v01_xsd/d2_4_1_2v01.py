from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D2_4_1_2"


@dataclass
class Root:
    """
    :ivar list_value:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D2_4_1_2"

    list_value: List[List[str]] = field(
        default_factory=list,
        metadata=dict(
            name="List",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            min_length=2,
            max_length=6,
            pattern=r"123 (\d+\s)*456",
            tokens=True
        )
    )
