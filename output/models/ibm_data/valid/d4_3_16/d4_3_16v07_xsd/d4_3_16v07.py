from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v07"


@dataclass
class Root:
    """
    :ivar eld_time_etzone_optional_fderived_optional:
    :ivar eld_time_etzone_optional_fderived_required:
    :ivar eld_time_etzone_optional_fderived_prohibited:
    :ivar eld_time_etzone_optional_tderived_optional:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v07"

    eld_time_etzone_optional_fderived_optional: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeETzoneOptionalFDerivedOptional",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            explicit_timezone="optional"
        )
    )
    eld_time_etzone_optional_fderived_required: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeETzoneOptionalFDerivedRequired",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            explicit_timezone="required"
        )
    )
    eld_time_etzone_optional_fderived_prohibited: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeETzoneOptionalFDerivedProhibited",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            explicit_timezone="prohibited"
        )
    )
    eld_time_etzone_optional_tderived_optional: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeETzoneOptionalTDerivedOptional",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            explicit_timezone="optional"
        )
    )