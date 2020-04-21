from dataclasses import dataclass, field
from typing import List, Union

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v03"


@dataclass
class Root:
    """
    :ivar ely_mdunion_a:
    :ivar ely_mdunion_b:
    :ivar ely_mdunion_c:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v03"

    ely_mdunion_a: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="elyMDUnionA",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    ely_mdunion_b: List[Union[str, int]] = field(
        default_factory=list,
        metadata=dict(
            name="elyMDUnionB",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    ely_mdunion_c: List[Union[str, int]] = field(
        default_factory=list,
        metadata=dict(
            name="elyMDUnionC",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
