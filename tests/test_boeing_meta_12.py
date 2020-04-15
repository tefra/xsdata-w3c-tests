import pytest

from tests.utils import assert_bindings


@pytest.mark.schema11
def test_ipo6_ipo_1(save_xml):
    """
    International Purchase Order 6
    """
    assert_bindings(
        schema="boeingData/ipo6/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo6/ipo_1.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ipo6_ipo_2(save_xml):
    """
    International Purchase Order 6
    """
    assert_bindings(
        schema="boeingData/ipo6/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo6/ipo_2.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ipo5_ipo_1(save_xml):
    """
    International Purchase Order 5
    """
    assert_bindings(
        schema="boeingData/ipo5/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo5/ipo_1.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ipo5_ipo_2(save_xml):
    """
    International Purchase Order 5
    """
    assert_bindings(
        schema="boeingData/ipo5/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo5/ipo_2.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ipo4_ipo_1(save_xml):
    """
    International Purchase Order 4
    """
    assert_bindings(
        schema="boeingData/ipo4/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo4/ipo_1.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ipo4_ipo_2(save_xml):
    """
    International Purchase Order 4
    """
    assert_bindings(
        schema="boeingData/ipo4/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo4/ipo_2.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ipo3_ipo_1(save_xml):
    """
    International Purchase Order 3
    """
    assert_bindings(
        schema="boeingData/ipo3/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo3/ipo_1.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ipo3_ipo_2(save_xml):
    """
    International Purchase Order 3
    """
    assert_bindings(
        schema="boeingData/ipo3/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo3/ipo_2.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ipo2_ipo_1(save_xml):
    """
    International Purchase Order 2
    """
    assert_bindings(
        schema="boeingData/ipo2/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo2/ipo_1.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ipo2_ipo_2(save_xml):
    """
    International Purchase Order 2
    """
    assert_bindings(
        schema="boeingData/ipo2/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo2/ipo_2.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ipo1_ipo_1(save_xml):
    """
    International Purchase Order 1
    """
    assert_bindings(
        schema="boeingData/ipo1/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo1/ipo_1.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ipo1_ipo_2(save_xml):
    """
    International Purchase Order 1
    """
    assert_bindings(
        schema="boeingData/ipo1/ipo.xsd",
        is_valid=True,
        instance="boeingData/ipo1/ipo_2.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.1",
        save_xml=save_xml,
    )
