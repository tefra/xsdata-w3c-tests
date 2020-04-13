import pytest

from tests.utils import assert_bindings


@pytest.mark.schema11
def test_introspection_introspect_test_set_introspection_1(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="common/introspection.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_nist2004_01_14_2(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="nistMeta/NISTXMLSchemaDatatypes.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_suntest_3(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/suntest.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_agroup_def_4(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/AGroupDef.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_attr_decl_5(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/AttrDecl.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_attr_use_6(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/AttrUse.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ctype_7(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/CType.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_elem_decl_8(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/ElemDecl.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_id_constr_defs_9(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/IdConstrDefs.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_mgroup_10(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/MGroup.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_mgroup_def_11(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/MGroupDef.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_notation_12(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/Notation.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_stype_13(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/SType.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_schema_14(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/Schema.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_wildcard_15(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="sunMeta/Wildcard.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_additional2006_07_15_16(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/Additional_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_annotations2006_07_15_17(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/Annotations_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_attribute_group2006_07_15_18(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/AttributeGroup_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_attribute2006_07_15_19(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/Attribute_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_complex_type2006_07_15_20(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/ComplexType_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_data_types2006_07_15_21(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/DataTypes_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_element2006_07_15_22(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/Element_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_errata102006_07_15_23(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/Errata10_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_group2006_07_15_24(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/Group_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_identity_constraint2006_07_15_25(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/IdentityConstraint_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_model_groups2006_07_15_26(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/ModelGroups_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_notations2006_07_15_27(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/Notations_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_particles2006_07_15_28(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/Particles_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_regex2006_07_15_29(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/Regex_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_schema2006_07_15_30(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/Schema_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_simple_type2006_07_15_31(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/SimpleType_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_ms_wildcards2006_07_15_32(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="msMeta/Wildcards_w3c.xml",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_boeing_xsdtest_cases_33(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="boeingMeta/BoeingXSDTestSet.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_all_34(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/All.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_assert_35(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/Assert.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_complex_36(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/Complex.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_cta_37(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/CTA.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_id_38(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/Id.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_open_39(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/Open.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_override_40(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/Override.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_simple_41(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/Simple.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_subsgroup_42(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/Subsgroup.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_target_ns_43(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/TargetNS.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_vc_44(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/VC.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_wild_45(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/Wild.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_xml_versions_46(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/XmlVersions.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_zone_47(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="saxonMeta/Zone.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_zone_48(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="oracleMeta/Zone.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_substitution_groups_49(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="wgMeta/substitution-groups.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_all_group_50(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/allGroup.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_any_attribute_51(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/anyAttribute.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_assert_52(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/assert.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_assertion_53(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/assertion.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_conditional_inclusion_54(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/conditionalInclusion.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_constraints_on_attribute_55(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/constraintsOnAttribute.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_cyclic_dependencies_redefine_include_import_override_56(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/cyclicRedefineIncludeImportOverride.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_date_57(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/date.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_date_time_stamp_58(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/dateTimeStamp.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_day_time_duration_59(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/dayTimeDuration.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_default_attributes_apply_60(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/defaultAttributesApply.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_default_fixed_61(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/defaultFixed.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_double_62(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/double.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_edcwildcard_63(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/edcWildcard.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_explicit_timezone_64(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/explicitTimezone.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_float_65(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/float.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_g_year_month_66(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/gYearMonth.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_g_year_67(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/gYear.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_g_month_day_68(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/gMonthDay.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_g_day_69(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/gDay.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_g_month_70(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/gMonth.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_id_idref_71(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/idIDREF.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_identity_constraint_72(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/identityConstraint.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_list_73(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/list.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_popen_content_74(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/openContent.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_regular_expression_75(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/regularExpression.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_restriction_of_complex_types_76(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/restrictionOfComplexTypes.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_rf_white_space_77(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/rf_whiteSpace.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_substitution_group_78(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/substitutionGroup.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_target_ns_79(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/targetNamespace.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_time_80(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/time.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_type_alternative_tests_81(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/typeAlternatives.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_cta_82(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/typeAlternativesMixed.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_union_83(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/union.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_units_length_84(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/unitsLength.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_unsigned_integers_85(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/unsignedInteger.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_vc_86(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/vc.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_wildcard_87(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/wildcard.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_xml11_support_88(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/xml11Support.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_xpath_default_nson_key_key_ref_unique_89(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/xpathDefaultNSonKeyKeyRefUnique.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_xsimport_reference_90(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/xsImportReference.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_introspection_introspect_test_set_year_month_duration_91(save_xml):

    assert_bindings(
        schema="common/xsts.xsd",
        is_valid=True,
        instance="ibmMeta/yearMonthDuration.testSet",
        instance_is_valid=True,
        class_name="TestSet",
        version="1.1",
        save_xml=save_xml,
    )
