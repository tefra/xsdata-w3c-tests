from dataclasses import dataclass, field
from typing import Optional
from output.models.ibm_data.mixed.target_namespace.tns4_xsd.tns4_imp import Y

__NAMESPACE__ = "http://test1"


@dataclass
class X:
    """
    :ivar y:
    """
    class Meta:
        name = "x"
        namespace = "http://test1"

    y: Optional[Y] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://test2",
            required=True
        )
    )
