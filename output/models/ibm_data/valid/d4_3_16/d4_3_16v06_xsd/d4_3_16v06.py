from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v06"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v06"

    eld_time_pattern: list[str] = field(
        default_factory=list,
        metadata={
            "name": "eldTimePattern",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        },
    )
    eld_time_etrequired: list[str] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeETRequired",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            "explicit_timezone": "required",
        },
    )
    eld_time_etoptional: list[str] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeETOptional",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            "explicit_timezone": "optional",
        },
    )
    eld_time_etprohibited: list[str] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeETProhibited",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            "explicit_timezone": "prohibited",
        },
    )
    d_time_etoptional_der_req: list[str] = field(
        default_factory=list,
        metadata={
            "name": "dTimeETOptionalDerReq",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            "explicit_timezone": "required",
        },
    )
    d_time_etoptional_der_pro: list[str] = field(
        default_factory=list,
        metadata={
            "name": "dTimeETOptionalDerPro",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            "explicit_timezone": "prohibited",
        },
    )
