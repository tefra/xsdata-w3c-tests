from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_2_4"


@dataclass
class C1:
    """
    :ivar default_attr:
    :ivar element1:
    :ivar element2:
    :ivar element_added:
    """
    class Meta:
        name = "c1"

    default_attr: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="defaultAttr",
            type="Attribute",
            namespace="http://xstest-tns/schema11_S3_4_2_4",
            required=True
        )
    )
    element1: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xstest-tns/schema11_S3_4_2_4",
            required=True
        )
    )
    element2: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://xstest-tns/schema11_S3_4_2_4",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    element_added: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://xstest-tns/schema11_S3_4_2_4",
            required=True
        )
    )
