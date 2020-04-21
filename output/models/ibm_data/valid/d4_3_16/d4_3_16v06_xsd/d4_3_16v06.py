from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v06"


@dataclass
class Root:
    """
    :ivar eld_time_pattern:
    :ivar eld_time_etrequired:
    :ivar eld_time_etoptional:
    :ivar eld_time_etprohibited:
    :ivar d_time_etoptional_der_req:
    :ivar d_time_etoptional_der_pro:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v06"

    eld_time_pattern: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimePattern",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*"
        )
    )
    eld_time_etrequired: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeETRequired",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            explicit_timezone="required"
        )
    )
    eld_time_etoptional: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeETOptional",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            explicit_timezone="optional"
        )
    )
    eld_time_etprohibited: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeETProhibited",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            explicit_timezone="prohibited"
        )
    )
    d_time_etoptional_der_req: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="dTimeETOptionalDerReq",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            explicit_timezone="required"
        )
    )
    d_time_etoptional_der_pro: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="dTimeETOptionalDerPro",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            explicit_timezone="prohibited"
        )
    )
