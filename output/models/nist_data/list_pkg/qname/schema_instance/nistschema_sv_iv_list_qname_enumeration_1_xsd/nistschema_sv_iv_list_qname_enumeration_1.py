from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"


class NistschemaSvIvListQnameEnumeration1Type(Enum):
    """
    :cvar VALUE_USED_F_EPROCESS_THE_NEWCOMER_Q_ITO_THESE_BEEN_UTILITIES_MODELS_DATA_BOTTLENECKS_TO_INFOR_GTO_MORE_YIS_NOT_MULT_AOF_R_KHAS_VIRTUALLY_ACCESSIBLE_INCLUDING_ALLOWS_SU:
    :cvar VALUE_WILL_FOUR_T_OHAS_A_BACK_IDENTIFY_VINFL_YFOR_THE_A_INFORMATION_AND_A_WVIRTUALLY_DEVICES_CONTRIBUTE_FOR_PARTNERSHIPS_ENSURE_ENSU_VBUSINESS_AND_FOR_CREATION_AND_INFORMATION_AI_IS_ALLOW_FOUR_AS_TO_IMP_MISSUES_E_INDUSTRY_FROM_DEF_QTO_RE:
    :cvar AAPPROACH_INFORMATION_FOR_METROLOGY_JOINT_FILE_THESE_I_SCOMMERCE_THROUGH_DEFINE_MANIPULATION_GROUPS_OF_D_PAND_WTO_APPROACH_UTILIZE_AND_DEVELOP_IMATCH_CONTRIBUTE_D_MMORE_PERVASIVE_THE_NECESSARY_AND_DTHE_OF_METHODS_A_GCONSTITUENT_HAS_HAS_AUTOMATING_SOFTWARE_TECHNOLOGIES_WILL_AN_YIN_BASE_OF_IFILE_CAN_FOR_XCONFORMANCE:
    :cvar AOF_R_KHAS_VIRTUALLY_ACCESSIBLE_INCLUDING_ALLOWS_SU_NFOR_AS_YTHEN_SPECIFICATIONS_PROVIDED_WIT_JINTERNATIONAL_INFORMATION_T_THE_SHIFT_AND_O_IIS_AND_OF_AND_SPECIFICATIONS_OUR_GIMPACT_LA_WITH_FOR_REPOSITORY_CREATE_BY_APPROPRIATE_WILL_FOUR_T_OHAS_A_BACK_IDENTIFY:
    :cvar AUSERS_GSPECIFICATION_HIGH_TO_TOOLS_SERVICE_DONAT_EBOTH_MANUAL_XREGISTRY_TO_COMPUTER_THE_SUBJECT_BACK_AND_THESE_TOPERATING_T_TAUTOMATE_AN_BAND_AND_YEARS_20_AND_AND_HAVI_H_O_GAND_OPERATING_COM_FAND_DISCUSS_YEARS_A_LENFORCEMENT_SERVICES_LACKIN_DWITH_VWITH_OB:
    :cvar DWITH_VWITH_OB_ASOLUTIONS_EHAVING_SAME_VCAN_MECHANISM_MTH_NOF_AND_THE_KNOWN_BY_DEVELOPERS_AND_AAS_THE_INFORMATION_RETRIEVAL_ONLY_IMPLEMENTATION_TECH_DWILL_IF_OF_TO_THE_USED_WITH_LOOKING_T:
    :cvar QTO_RE_KFROM_FOR_HTHAT_AND_MANIPULATE_ORGANIZATIONS_HETEROGENEOUS_Q_THAT_FOR_BUSINES_ECAN_INTEROPERABILIT_UREGI_USED_THE_BE_THE_SOF_SYSTEM_BANDWIDTH_ULTIM_TWILL_TWO_AND_YOBJECT_INCORPORATED_A_AND_MU_AUSERS_GSPECIFICATION_HIGH_TO_TOOLS_SERVICE_DONAT:
    :cvar XCONFORMANCE_ANEW_SPECIFICA_UHELP_CROSS_OVER_THE_IS_PERVASIVE_SUPPLY_DE_HDISCUSS_FO_WDEBUG_A_MUST_XWHICH_IS_DOCUM_FAS_USES_SOFTWARE_D_FROM_AN_RE_HOBJECT_20_QSUCCESS_AND_NATURE_FULL_ON_USED_F:
    """
    VALUE_USED_F_EPROCESS_THE_NEWCOMER_Q_ITO_THESE_BEEN_UTILITIES_MODELS_DATA_BOTTLENECKS_TO_INFOR_GTO_MORE_YIS_NOT_MULT_AOF_R_KHAS_VIRTUALLY_ACCESSIBLE_INCLUDING_ALLOWS_SU = "_used.f eprocess_the-newcomer q ito.these-been.utilities.models-data-bottlenecks_to_infor gto_more:yis.not_mult aof_r:khas_virtually-accessible-including.allows_su"
    VALUE_WILL_FOUR_T_OHAS_A_BACK_IDENTIFY_VINFL_YFOR_THE_A_INFORMATION_AND_A_WVIRTUALLY_DEVICES_CONTRIBUTE_FOR_PARTNERSHIPS_ENSURE_ENSU_VBUSINESS_AND_FOR_CREATION_AND_INFORMATION_AI_IS_ALLOW_FOUR_AS_TO_IMP_MISSUES_E_INDUSTRY_FROM_DEF_QTO_RE = "_will_four_t:ohas_a-back-identify vinfl:yfor-the.a-information.and_a wvirtually_devices-contribute_for_partnerships-ensure.ensu vbusiness.and_for.creation_and_information-ai _is-allow.four-as_to-imp missues_e_industry-from_def qto.:_re"
    AAPPROACH_INFORMATION_FOR_METROLOGY_JOINT_FILE_THESE_I_SCOMMERCE_THROUGH_DEFINE_MANIPULATION_GROUPS_OF_D_PAND_WTO_APPROACH_UTILIZE_AND_DEVELOP_IMATCH_CONTRIBUTE_D_MMORE_PERVASIVE_THE_NECESSARY_AND_DTHE_OF_METHODS_A_GCONSTITUENT_HAS_HAS_AUTOMATING_SOFTWARE_TECHNOLOGIES_WILL_AN_YIN_BASE_OF_IFILE_CAN_FOR_XCONFORMANCE = "aapproach_information_for-metrology-joint.file-these_i scommerce_through.define.manipulation.groups.of.d pand:wto-approach.utilize.and-develop imatch.contribute_d:mmore-pervasive-the.necessary.and- dthe.of_methods.a gconstituent.has_has.automating.software-technologies-will-an yin.base.of.:ifile-can.for_ xconformance"
    AOF_R_KHAS_VIRTUALLY_ACCESSIBLE_INCLUDING_ALLOWS_SU_NFOR_AS_YTHEN_SPECIFICATIONS_PROVIDED_WIT_JINTERNATIONAL_INFORMATION_T_THE_SHIFT_AND_O_IIS_AND_OF_AND_SPECIFICATIONS_OUR_GIMPACT_LA_WITH_FOR_REPOSITORY_CREATE_BY_APPROPRIATE_WILL_FOUR_T_OHAS_A_BACK_IDENTIFY = "aof_r:khas_virtually-accessible-including.allows_su nfor.as:ythen_specifications_provided.wit jinternational.information-t _the.shift-and-o:iis-and.of-and_specifications-our gimpact:la.with_for-repository-create.by-appropriate. _will_four_t:ohas_a-back-identify"
    AUSERS_GSPECIFICATION_HIGH_TO_TOOLS_SERVICE_DONAT_EBOTH_MANUAL_XREGISTRY_TO_COMPUTER_THE_SUBJECT_BACK_AND_THESE_TOPERATING_T_TAUTOMATE_AN_BAND_AND_YEARS_20_AND_AND_HAVI_H_O_GAND_OPERATING_COM_FAND_DISCUSS_YEARS_A_LENFORCEMENT_SERVICES_LACKIN_DWITH_VWITH_OB = "ausers:gspecification_high_to.tools.service-donat eboth.manual xregistry-to.computer.the_subject-back_and-these_ toperating-t:tautomate-an band-and-years-20_and.and.havi h:o gand-operating-com:fand-discuss-years-a lenforcement_services-lackin dwith.:vwith-ob"
    DWITH_VWITH_OB_ASOLUTIONS_EHAVING_SAME_VCAN_MECHANISM_MTH_NOF_AND_THE_KNOWN_BY_DEVELOPERS_AND_AAS_THE_INFORMATION_RETRIEVAL_ONLY_IMPLEMENTATION_TECH_DWILL_IF_OF_TO_THE_USED_WITH_LOOKING_T = "dwith.:vwith-ob asolutions_ ehaving.same_:vcan_mechanism mth:nof_and-the_known-by-developers_and aas.the.information.retrieval_only-implementation-tech dwill.if_of.to.the-used.with.looking_t"
    QTO_RE_KFROM_FOR_HTHAT_AND_MANIPULATE_ORGANIZATIONS_HETEROGENEOUS_Q_THAT_FOR_BUSINES_ECAN_INTEROPERABILIT_UREGI_USED_THE_BE_THE_SOF_SYSTEM_BANDWIDTH_ULTIM_TWILL_TWO_AND_YOBJECT_INCORPORATED_A_AND_MU_AUSERS_GSPECIFICATION_HIGH_TO_TOOLS_SERVICE_DONAT = "qto.:_re kfrom_for_:hthat.and_manipulate_organizations_heterogeneous q:_that_for-busines ecan_interoperabilit uregi _used.the-be_the-:sof_system-bandwidth-ultim twill_two-and.:yobject-incorporated.a-and-mu ausers:gspecification_high_to.tools.service-donat"
    XCONFORMANCE_ANEW_SPECIFICA_UHELP_CROSS_OVER_THE_IS_PERVASIVE_SUPPLY_DE_HDISCUSS_FO_WDEBUG_A_MUST_XWHICH_IS_DOCUM_FAS_USES_SOFTWARE_D_FROM_AN_RE_HOBJECT_20_QSUCCESS_AND_NATURE_FULL_ON_USED_F = "xconformance anew_specifica:uhelp-cross-over-the.is-pervasive-supply_de hdiscuss-fo:wdebug_a-must_ xwhich-is-docum fas-uses-:_software.d _from-an.re hobject-20:qsuccess_and.nature-full-on. _used.f"


@dataclass
class TypeFromAnRe:
    """
    :ivar value:
    """
    class Meta:
        name = "_from-an.re"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeIsAllowFourAsToImp:
    """
    :ivar value:
    """
    class Meta:
        name = "_is-allow.four-as_to-imp"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeUsedF:
    """
    :ivar value:
    """
    class Meta:
        name = "_used.f"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class AapproachInformationForMetrologyJointFileTheseI:
    """
    :ivar value:
    """
    class Meta:
        name = "aapproach_information_for-metrology-joint.file-these_i"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class AasTheInformationRetrievalOnlyImplementationTech:
    """
    :ivar value:
    """
    class Meta:
        name = "aas.the.information.retrieval_only-implementation-tech"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Asolutions:
    """
    :ivar value:
    """
    class Meta:
        name = "asolutions_"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class BandAndYears20AndAndHavi:
    """
    :ivar value:
    """
    class Meta:
        name = "band-and-years-20_and.and.havi"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class DtheOfMethodsA:
    """
    :ivar value:
    """
    class Meta:
        name = "dthe.of_methods.a"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class DwillIfOfToTheUsedWithLookingT:
    """
    :ivar value:
    """
    class Meta:
        name = "dwill.if_of.to.the-used.with.looking_t"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class EbothManual:
    """
    :ivar value:
    """
    class Meta:
        name = "eboth.manual"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class EcanInteroperabilit:
    """
    :ivar value:
    """
    class Meta:
        name = "ecan_interoperabilit"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class EprocessTheNewcomer:
    """
    :ivar value:
    """
    class Meta:
        name = "eprocess_the-newcomer"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class GconstituentHasHasAutomatingSoftwareTechnologiesWillAn:
    """
    :ivar value:
    """
    class Meta:
        name = "gconstituent.has_has.automating.software-technologies-will-an"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ItoTheseBeenUtilitiesModelsDataBottlenecksToInfor:
    """
    :ivar value:
    """
    class Meta:
        name = "ito.these-been.utilities.models-data-bottlenecks_to_infor"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class JinternationalInformationT:
    """
    :ivar value:
    """
    class Meta:
        name = "jinternational.information-t"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class LenforcementServicesLackin:
    """
    :ivar value:
    """
    class Meta:
        name = "lenforcement_services-lackin"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class MissuesEIndustryFromDef:
    """
    :ivar value:
    """
    class Meta:
        name = "missues_e_industry-from_def"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Q:
    """
    :ivar value:
    """
    class Meta:
        name = "q"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ScommerceThroughDefineManipulationGroupsOfD:
    """
    :ivar value:
    """
    class Meta:
        name = "scommerce_through.define.manipulation.groups.of.d"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Uregi:
    """
    :ivar value:
    """
    class Meta:
        name = "uregi"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class VbusinessAndForCreationAndInformationAi:
    """
    :ivar value:
    """
    class Meta:
        name = "vbusiness.and_for.creation_and_information-ai"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class WvirtuallyDevicesContributeForPartnershipsEnsureEnsu:
    """
    :ivar value:
    """
    class Meta:
        name = "wvirtually_devices-contribute_for_partnerships-ensure.ensu"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Xconformance:
    """
    :ivar value:
    """
    class Meta:
        name = "xconformance"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class XregistryToComputerTheSubjectBackAndThese:
    """
    :ivar value:
    """
    class Meta:
        name = "xregistry-to.computer.the_subject-back_and-these_"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class XwhichIsDocum:
    """
    :ivar value:
    """
    class Meta:
        name = "xwhich-is-docum"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class NistschemaSvIvListQnameEnumeration1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-enumeration-1"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-1-NS"

    value: Optional[NistschemaSvIvListQnameEnumeration1Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
