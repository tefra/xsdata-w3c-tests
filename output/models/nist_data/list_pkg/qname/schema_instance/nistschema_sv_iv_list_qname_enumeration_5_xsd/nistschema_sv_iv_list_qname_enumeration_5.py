from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"


class NistschemaSvIvListQnameEnumeration5Type(Enum):
    """
    :cvar VALUE_BACK_PARTICIPATING_FACT_FACT_THE_USED_RECENT_OFFER_ONLY_I_M_XPARTNE_XBOTH_WILL_INCLUDED_OF_NEW_CONSORTIUM_THE_RESOURCES_HELP_ARE_FOR_LTO_AND_EACH_DEFINING_ABOUT_OF_T_FLEADERSHIP_COMPUTING_WHO_CROSS_REFERENCE:
    :cvar VALUE_CONFORMANC_SSPECIFICATIONS_WHICH_OF_INDUSTRY_FROM_THE_BE_TLIBRARY_FILTER_INCLUDE_FOR_CAN_TECHNOLOGY_ALSO_REF_JFIVE_BY_IS_VIA_ARE_CONSORTIUM_AND_DEVELOPERS_PROTOTYPE_SIMULAT_WCONTAINS_DAT_PAND_SERVICE_ALL_AND_TECH_FAND_A_UCOMPUTER_TO_MU_DOF_INVESTIGATION_PERVASIVE_HARDWARE_THE_OBJECTS:
    :cvar VALUE_ORGANIZATIONS_AND_WEB_AND_WILL_DOCUMENTS_MANIPULATE_FINE_CAN_U_OAND_CPARTICIPATE_QBOTH_THE_AND_PARTICIPATING_AREAS_FILES_PARTNERSH_JTHE_ST_NAND_REL_TREGISTRY_C:
    :cvar VALUE_TEST_ANY_AND_THE_TO_COMPUTING_THOSE_DOCUMENTS_THE_ME_YMETHODS_LOCATION_TO_LED_USER_NUMBER_THIS_AS_RE_JDIVISIONS_ITS_IN_FOR_SUCH_AND_TOOLS_ICOMMUN_KRESULT_AND_NEXT_WITH_BUILD_VIA_CON_KAND_EMERGING_THIS_FILE_OF_W_HLOCALIZED_KTHE_DOCUM_CTHE_ESTABLISH_WILL_AND_SUPPLY_USED_RBE_SPECIFIC_WSIGNATURES_EACH_ADDITIONALLY_CAN_BETWEEN_GTHESE_USING_2000_INDUSTRY_MANUFACTURERS:
    :cvar AE_SOF_DISC_ATO_THE_PARTNERSHIPS_THE_RESPECT_AND_KEY_FOR_OF_BE_PWAS_PROFILES_DEV_AAPPL_BBECOM_HPROVIDE_VE_OANY_CONSTITUENT_THE_LANGUAGE_DI_FAS_ORGANIZATIONS_ALLOW_ABILITY_LOW_COST_INTEROPER_LAPPLICATIONS_RECOGNITION_TE:
    :cvar DOF_INVESTIGATION_PERVASIVE_HARDWARE_THE_OBJECTS_UREVIEWED_THE_BACK_RESOURCE_A_PERFORMANCE_USE_RESOU_ISET_SOFTWARE_STAKEHOLDERS_CO_N20_INCLUDING_F_WDEVELOPMENT_AND_WITH_MANIPULATION_THESE_TH_RIC_BEN_ORGANIZATIONS_AND_WEB_AND_WILL_DOCUMENTS_MANIPULATE_FINE_CAN_U:
    :cvar FLEADERSHIP_COMPUTING_WHO_CROSS_REFERENCE_WTHE_ARE_THESE_KNOWN_TO_ABILITY_AND_OF_DEVICES_USE_TTOOLS_TO_FROM_ADDRESSING_I_AND_THE_TEST_ANY_AND_THE_TO_COMPUTING_THOSE_DOCUMENTS_THE_ME:
    :cvar GTHESE_USING_2000_INDUSTRY_MANUFACTURERS_AORGANI_PMANY_PROMINENT_THESE_U_REVOLUTION_DWITH_IN_NEW_TO_OF_AND_IS_AREAS_HAS_PAGES_DOCUMENTS_FROM_DEPL_NTECHNI_QAPPLICATIONS_COMPETENCE_FILE_DISCUSSIONS_TSET_TO_BE_THE_FOR_SU_VOF_ETC_ARE_COMPLEX_SECURITY_AN_NLI:
    :cvar LAPPLICATIONS_RECOGNITION_TE_XHIGHLY_AMONG_COMMERCE_DESIGNED_TECHNOLOG_TTHE_OAS_LACKI_QTHAT_IN_WIRELESS_TRANSACT_AND_AS_SET_LACKING_HARDWARE_B_YFILES_THAT_IS_HIGH_SUPPORT_WAYS_COLLABORATE_INFORMATION_CONFORMANC_SSPECIFICATIONS_WHICH_OF_INDUSTRY_FROM_THE_BE:
    :cvar TREGISTRY_C_EOF_IMAGES_AND_SIGNATURES_WAS_WHICH_FO_ATRANS_JTHE_RE_XCERT_CGROUPS_ALSO_US_IN_RSEMA_SWITH_BETWEEN_INDUSTRIES_SIGNIFICANT_LANGUAGE_COST_OBTAIN_ETIME_PRINT_HAS_B_XGROUPS_TOOL_ENSURE_N_EEXCHANGE_WHICH_COMPUTER_AND_BUSINESS_FURTHE_ODONATE_MANAGE_FINE_THE_DEFINING_STANDAR_BACK_PARTICIPATING_FACT_FACT_THE_USED_RECENT_OFFER_ONLY_I:
    """
    VALUE_BACK_PARTICIPATING_FACT_FACT_THE_USED_RECENT_OFFER_ONLY_I_M_XPARTNE_XBOTH_WILL_INCLUDED_OF_NEW_CONSORTIUM_THE_RESOURCES_HELP_ARE_FOR_LTO_AND_EACH_DEFINING_ABOUT_OF_T_FLEADERSHIP_COMPUTING_WHO_CROSS_REFERENCE = "_back.participating.fact_fact_the_used-recent.offer-only_i m:xpartne xboth _will.included_of_new.consortium.the-resources-help.are.for_ lto.and_each.defining_about.of_t fleadership.computing_who-cross-reference"
    VALUE_CONFORMANC_SSPECIFICATIONS_WHICH_OF_INDUSTRY_FROM_THE_BE_TLIBRARY_FILTER_INCLUDE_FOR_CAN_TECHNOLOGY_ALSO_REF_JFIVE_BY_IS_VIA_ARE_CONSORTIUM_AND_DEVELOPERS_PROTOTYPE_SIMULAT_WCONTAINS_DAT_PAND_SERVICE_ALL_AND_TECH_FAND_A_UCOMPUTER_TO_MU_DOF_INVESTIGATION_PERVASIVE_HARDWARE_THE_OBJECTS = "_conformanc:sspecifications_which.of_industry_from.the-be tlibrary.filter_include-for_can.technology_also_ref jfive_by.is.via_are_consortium_and_developers_prototype- _simulat wcontains.dat:pand-service.all.and.tech fand_a:ucomputer-to-mu dof_investigation_pervasive_hardware.the_objects"
    VALUE_ORGANIZATIONS_AND_WEB_AND_WILL_DOCUMENTS_MANIPULATE_FINE_CAN_U_OAND_CPARTICIPATE_QBOTH_THE_AND_PARTICIPATING_AREAS_FILES_PARTNERSH_JTHE_ST_NAND_REL_TREGISTRY_C = "_organizations-and-web.and-will.documents-manipulate.fine-can-u oand cparticipate_ qboth.the-and-participating_areas_files.partnersh jthe_st:nand.rel tregistry_c"
    VALUE_TEST_ANY_AND_THE_TO_COMPUTING_THOSE_DOCUMENTS_THE_ME_YMETHODS_LOCATION_TO_LED_USER_NUMBER_THIS_AS_RE_JDIVISIONS_ITS_IN_FOR_SUCH_AND_TOOLS_ICOMMUN_KRESULT_AND_NEXT_WITH_BUILD_VIA_CON_KAND_EMERGING_THIS_FILE_OF_W_HLOCALIZED_KTHE_DOCUM_CTHE_ESTABLISH_WILL_AND_SUPPLY_USED_RBE_SPECIFIC_WSIGNATURES_EACH_ADDITIONALLY_CAN_BETWEEN_GTHESE_USING_2000_INDUSTRY_MANUFACTURERS = "_test_any-and-the_to_computing_those.documents_the.me ymethods-location-to.led-user-number.this-as_re jdivisions_its_in.for_such-and-tools- icommun:kresult.and_next-with_build-via.con kand-emerging-this_file_of.w hlocalized kthe.docum:cthe_establish.will.and_supply_used rbe.specific:wsignatures.each_additionally-can-between- gthese_using-2000-industry.manufacturers."
    AE_SOF_DISC_ATO_THE_PARTNERSHIPS_THE_RESPECT_AND_KEY_FOR_OF_BE_PWAS_PROFILES_DEV_AAPPL_BBECOM_HPROVIDE_VE_OANY_CONSTITUENT_THE_LANGUAGE_DI_FAS_ORGANIZATIONS_ALLOW_ABILITY_LOW_COST_INTEROPER_LAPPLICATIONS_RECOGNITION_TE = "ae.:_sof _disc:ato-the.partnerships-the.respect-and.key_for.of-be pwas-profiles-dev aappl:bbecom hprovide-ve:oany.constituent_the _language.di:fas_organizations-allow-ability_low-cost.interoper lapplications.recognition.te"
    DOF_INVESTIGATION_PERVASIVE_HARDWARE_THE_OBJECTS_UREVIEWED_THE_BACK_RESOURCE_A_PERFORMANCE_USE_RESOU_ISET_SOFTWARE_STAKEHOLDERS_CO_N20_INCLUDING_F_WDEVELOPMENT_AND_WITH_MANIPULATION_THESE_TH_RIC_BEN_ORGANIZATIONS_AND_WEB_AND_WILL_DOCUMENTS_MANIPULATE_FINE_CAN_U = "dof_investigation_pervasive_hardware.the_objects ureviewed-the.back-resource.a.performance.use_resou iset.software_stakeholders_co n20-including_f wdevelopment_and-with_manipulation.these.th _ric:ben _organizations-and-web.and-will.documents-manipulate.fine-can-u"
    FLEADERSHIP_COMPUTING_WHO_CROSS_REFERENCE_WTHE_ARE_THESE_KNOWN_TO_ABILITY_AND_OF_DEVICES_USE_TTOOLS_TO_FROM_ADDRESSING_I_AND_THE_TEST_ANY_AND_THE_TO_COMPUTING_THOSE_DOCUMENTS_THE_ME = "fleadership.computing_who-cross-reference wthe_are_these.known-to-ability_ _and-of-devices_use-:ttools-to.from.addressing_i _and.the _test_any-and-the_to_computing_those.documents_the.me"
    GTHESE_USING_2000_INDUSTRY_MANUFACTURERS_AORGANI_PMANY_PROMINENT_THESE_U_REVOLUTION_DWITH_IN_NEW_TO_OF_AND_IS_AREAS_HAS_PAGES_DOCUMENTS_FROM_DEPL_NTECHNI_QAPPLICATIONS_COMPETENCE_FILE_DISCUSSIONS_TSET_TO_BE_THE_FOR_SU_VOF_ETC_ARE_COMPLEX_SECURITY_AN_NLI = "gthese_using-2000-industry.manufacturers. aorgani:pmany_prominent_these_u _revolution dwith-in.new_to-of_and_is.areas-has.pages-documents-from_depl ntechni:qapplications.competence-file-discussions tset_to-be-the_for.su:vof_etc.are.complex_security_an nli"
    LAPPLICATIONS_RECOGNITION_TE_XHIGHLY_AMONG_COMMERCE_DESIGNED_TECHNOLOG_TTHE_OAS_LACKI_QTHAT_IN_WIRELESS_TRANSACT_AND_AS_SET_LACKING_HARDWARE_B_YFILES_THAT_IS_HIGH_SUPPORT_WAYS_COLLABORATE_INFORMATION_CONFORMANC_SSPECIFICATIONS_WHICH_OF_INDUSTRY_FROM_THE_BE = "lapplications.recognition.te xhighly-among.commerce-designed-technolog tthe oas-lacki qthat_in-wireless-transact-and-as-set-lacking.hardware-b yfiles:_that-is-high.support-ways.collaborate_information- _conformanc:sspecifications_which.of_industry_from.the-be"
    TREGISTRY_C_EOF_IMAGES_AND_SIGNATURES_WAS_WHICH_FO_ATRANS_JTHE_RE_XCERT_CGROUPS_ALSO_US_IN_RSEMA_SWITH_BETWEEN_INDUSTRIES_SIGNIFICANT_LANGUAGE_COST_OBTAIN_ETIME_PRINT_HAS_B_XGROUPS_TOOL_ENSURE_N_EEXCHANGE_WHICH_COMPUTER_AND_BUSINESS_FURTHE_ODONATE_MANAGE_FINE_THE_DEFINING_STANDAR_BACK_PARTICIPATING_FACT_FACT_THE_USED_RECENT_OFFER_ONLY_I = "tregistry_c eof.images.and-signatures_was-which.fo atrans:jthe-re xcert:cgroups-also-us _in:rsema swith.between-industries.significant-language_cost-obtain etime-print.has.b:xgroups.tool_ensure-n eexchange_which_computer-and.business_furthe odonate-manage_fine_the_defining_standar _back.participating.fact_fact_the_used-recent.offer-only_i"


@dataclass
class TypeAndThe:
    """
    :ivar value:
    """
    class Meta:
        name = "_and.the"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeBackParticipatingFactFactTheUsedRecentOfferOnlyI:
    """
    :ivar value:
    """
    class Meta:
        name = "_back.participating.fact_fact_the_used-recent.offer-only_i"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeOrganizationsAndWebAndWillDocumentsManipulateFineCanU:
    """
    :ivar value:
    """
    class Meta:
        name = "_organizations-and-web.and-will.documents-manipulate.fine-can-u"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeRevolution:
    """
    :ivar value:
    """
    class Meta:
        name = "_revolution"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeSimulat:
    """
    :ivar value:
    """
    class Meta:
        name = "_simulat"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeTestAnyAndTheToComputingThoseDocumentsTheMe:
    """
    :ivar value:
    """
    class Meta:
        name = "_test_any-and-the_to_computing_those.documents_the.me"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TypeWillIncludedOfNewConsortiumTheResourcesHelpAreFor:
    """
    :ivar value:
    """
    class Meta:
        name = "_will.included_of_new.consortium.the-resources-help.are.for_"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Cparticipate:
    """
    :ivar value:
    """
    class Meta:
        name = "cparticipate_"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class DofInvestigationPervasiveHardwareTheObjects:
    """
    :ivar value:
    """
    class Meta:
        name = "dof_investigation_pervasive_hardware.the_objects"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class DwithInNewToOfAndIsAreasHasPagesDocumentsFromDepl:
    """
    :ivar value:
    """
    class Meta:
        name = "dwith-in.new_to-of_and_is.areas-has.pages-documents-from_depl"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class EexchangeWhichComputerAndBusinessFurthe:
    """
    :ivar value:
    """
    class Meta:
        name = "eexchange_which_computer-and.business_furthe"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class EofImagesAndSignaturesWasWhichFo:
    """
    :ivar value:
    """
    class Meta:
        name = "eof.images.and-signatures_was-which.fo"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class FleadershipComputingWhoCrossReference:
    """
    :ivar value:
    """
    class Meta:
        name = "fleadership.computing_who-cross-reference"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class GtheseUsing2000IndustryManufacturers:
    """
    :ivar value:
    """
    class Meta:
        name = "gthese_using-2000-industry.manufacturers."
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Hlocalized:
    """
    :ivar value:
    """
    class Meta:
        name = "hlocalized"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class IsetSoftwareStakeholdersCo:
    """
    :ivar value:
    """
    class Meta:
        name = "iset.software_stakeholders_co"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class JdivisionsItsInForSuchAndTools:
    """
    :ivar value:
    """
    class Meta:
        name = "jdivisions_its_in.for_such-and-tools-"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class JfiveByIsViaAreConsortiumAndDevelopersPrototype:
    """
    :ivar value:
    """
    class Meta:
        name = "jfive_by.is.via_are_consortium_and_developers_prototype-"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class KandEmergingThisFileOfW:
    """
    :ivar value:
    """
    class Meta:
        name = "kand-emerging-this_file_of.w"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class LapplicationsRecognitionTe:
    """
    :ivar value:
    """
    class Meta:
        name = "lapplications.recognition.te"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class LtoAndEachDefiningAboutOfT:
    """
    :ivar value:
    """
    class Meta:
        name = "lto.and_each.defining_about.of_t"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class N20IncludingF:
    """
    :ivar value:
    """
    class Meta:
        name = "n20-including_f"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Nli:
    """
    :ivar value:
    """
    class Meta:
        name = "nli"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Oand:
    """
    :ivar value:
    """
    class Meta:
        name = "oand"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class OasLacki:
    """
    :ivar value:
    """
    class Meta:
        name = "oas-lacki"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class OdonateManageFineTheDefiningStandar:
    """
    :ivar value:
    """
    class Meta:
        name = "odonate-manage_fine_the_defining_standar"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class PwasProfilesDev:
    """
    :ivar value:
    """
    class Meta:
        name = "pwas-profiles-dev"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class QbothTheAndParticipatingAreasFilesPartnersh:
    """
    :ivar value:
    """
    class Meta:
        name = "qboth.the-and-participating_areas_files.partnersh"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class QthatInWirelessTransactAndAsSetLackingHardwareB:
    """
    :ivar value:
    """
    class Meta:
        name = "qthat_in-wireless-transact-and-as-set-lacking.hardware-b"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class SwithBetweenIndustriesSignificantLanguageCostObtain:
    """
    :ivar value:
    """
    class Meta:
        name = "swith.between-industries.significant-language_cost-obtain"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TlibraryFilterIncludeForCanTechnologyAlsoRef:
    """
    :ivar value:
    """
    class Meta:
        name = "tlibrary.filter_include-for_can.technology_also_ref"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TregistryC:
    """
    :ivar value:
    """
    class Meta:
        name = "tregistry_c"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Tthe:
    """
    :ivar value:
    """
    class Meta:
        name = "tthe"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class UreviewedTheBackResourceAPerformanceUseResou:
    """
    :ivar value:
    """
    class Meta:
        name = "ureviewed-the.back-resource.a.performance.use_resou"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class WdevelopmentAndWithManipulationTheseTh:
    """
    :ivar value:
    """
    class Meta:
        name = "wdevelopment_and-with_manipulation.these.th"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class WtheAreTheseKnownToAbility:
    """
    :ivar value:
    """
    class Meta:
        name = "wthe_are_these.known-to-ability_"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Xboth:
    """
    :ivar value:
    """
    class Meta:
        name = "xboth"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class XhighlyAmongCommerceDesignedTechnolog:
    """
    :ivar value:
    """
    class Meta:
        name = "xhighly-among.commerce-designed-technolog"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class YmethodsLocationToLedUserNumberThisAsRe:
    """
    :ivar value:
    """
    class Meta:
        name = "ymethods-location-to.led-user-number.this-as_re"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class NistschemaSvIvListQnameEnumeration5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-QName-enumeration-5"
        namespace = "NISTSchema-SV-IV-list-QName-enumeration-5-NS"

    value: Optional[NistschemaSvIvListQnameEnumeration5Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
