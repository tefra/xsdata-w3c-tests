from tests.utils import assert_bindings


def test_ipo6_ipo_1(json_360, save_output):
    """
    International Purchase Order 6
    """
    assert_bindings(
        schema="boeingData/ipo6/ipo.xsd",
        instance="boeingData/ipo6/ipo_1.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ipo6_ipo_2(json_360, save_output):
    """
    International Purchase Order 6
    """
    assert_bindings(
        schema="boeingData/ipo6/ipo.xsd",
        instance="boeingData/ipo6/ipo_2.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ipo5_ipo_1(json_360, save_output):
    """
    International Purchase Order 5
    """
    assert_bindings(
        schema="boeingData/ipo5/ipo.xsd",
        instance="boeingData/ipo5/ipo_1.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ipo5_ipo_2(json_360, save_output):
    """
    International Purchase Order 5
    """
    assert_bindings(
        schema="boeingData/ipo5/ipo.xsd",
        instance="boeingData/ipo5/ipo_2.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ipo4_ipo_1(json_360, save_output):
    """
    International Purchase Order 4
    """
    assert_bindings(
        schema="boeingData/ipo4/ipo.xsd",
        instance="boeingData/ipo4/ipo_1.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ipo4_ipo_2(json_360, save_output):
    """
    International Purchase Order 4
    """
    assert_bindings(
        schema="boeingData/ipo4/ipo.xsd",
        instance="boeingData/ipo4/ipo_2.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ipo3_ipo_1(json_360, save_output):
    """
    International Purchase Order 3
    """
    assert_bindings(
        schema="boeingData/ipo3/ipo.xsd",
        instance="boeingData/ipo3/ipo_1.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ipo3_ipo_2(json_360, save_output):
    """
    International Purchase Order 3
    """
    assert_bindings(
        schema="boeingData/ipo3/ipo.xsd",
        instance="boeingData/ipo3/ipo_2.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ipo2_ipo_1(json_360, save_output):
    """
    International Purchase Order 2
    """
    assert_bindings(
        schema="boeingData/ipo2/ipo.xsd",
        instance="boeingData/ipo2/ipo_1.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ipo2_ipo_2(json_360, save_output):
    """
    International Purchase Order 2
    """
    assert_bindings(
        schema="boeingData/ipo2/ipo.xsd",
        instance="boeingData/ipo2/ipo_2.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ipo1_ipo_1(json_360, save_output):
    """
    International Purchase Order 1
    """
    assert_bindings(
        schema="boeingData/ipo1/ipo.xsd",
        instance="boeingData/ipo1/ipo_1.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ipo1_ipo_2(json_360, save_output):
    """
    International Purchase Order 1
    """
    assert_bindings(
        schema="boeingData/ipo1/ipo.xsd",
        instance="boeingData/ipo1/ipo_2.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )
