from dataclasses import dataclass, field

__NAMESPACE__ = "http://xstest-tns/schema11_F4_3_16_v07"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_F4_3_16_v07"

    eld_time_etzone_optional_fderived_optional: list[str] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeETzoneOptionalFDerivedOptional",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            "explicit_timezone": "optional",
        },
    )
    eld_time_etzone_optional_fderived_required: list[str] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeETzoneOptionalFDerivedRequired",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            "explicit_timezone": "required",
        },
    )
    eld_time_etzone_optional_fderived_prohibited: list[str] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeETzoneOptionalFDerivedProhibited",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            "explicit_timezone": "prohibited",
        },
    )
    eld_time_etzone_optional_tderived_optional: list[str] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeETzoneOptionalTDerivedOptional",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
            "explicit_timezone": "optional",
        },
    )
