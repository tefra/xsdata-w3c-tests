from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/IBMd3_16v02"


@dataclass
class Root:
    """
    :ivar elflt_union_c:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/IBMd3_16v02"

    elflt_union_c: Optional[str] = field(
        default=None,
        metadata=dict(
            name="elfltUnionC",
            type="Element",
            namespace="",
            required=True,
            pattern=r"[0-9][0-9]"
        )
    )