from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_2_4"


@dataclass
class Root:
    """
    :ivar e1:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_2_4"

    e1: Optional["Root.E1"] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )

    @dataclass
    class E1:
        pass
