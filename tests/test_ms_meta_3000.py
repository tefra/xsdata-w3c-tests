import pytest

from tests.utils import assert_bindings


def test_group_n005v_group_n005v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=1, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupN005.xsd",
        is_valid=True,
        instance="msData/group/groupN005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_n004v_group_n004v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=0, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupN004.xsd",
        is_valid=True,
        instance="msData/group/groupN004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_n003v_group_n003v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=2, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupN003.xsd",
        is_valid=True,
        instance="msData/group/groupN003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_n002v_group_n002v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=1, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupN002.xsd",
        is_valid=True,
        instance="msData/group/groupN002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_n001v_group_n001v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=0, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupN001.xsd",
        is_valid=True,
        instance="msData/group/groupN001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_m005v_group_m005v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: check that
    maxOccurs default is 1, elements in instant XML = 2, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupM005.xsd",
        is_valid=True,
        instance="msData/group/groupM005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_m004v_group_m004v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: check that
    minOccurs default is 1, elements in instant XML = 1, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupM004.xsd",
        is_valid=True,
        instance="msData/group/groupM004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_m003v_group_m003v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: check that
    minOccurs default is 1, elements in instant XML = 0, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupM003.xsd",
        is_valid=True,
        instance="msData/group/groupM003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_l021v_group_l021v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=3, maxOccurs=unbounded
    """
    assert_bindings(
        schema="msData/group/groupL021.xsd",
        is_valid=True,
        instance="msData/group/groupL021.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_l019v_group_l019v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=3, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupL019.xsd",
        is_valid=True,
        instance="msData/group/groupL019.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_l018v_group_l018v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=2, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupL018.xsd",
        is_valid=True,
        instance="msData/group/groupL018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_l017v_group_l017v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=1, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupL017.xsd",
        is_valid=True,
        instance="msData/group/groupL017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_l016v_group_l016v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=0, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupL016.xsd",
        is_valid=True,
        instance="msData/group/groupL016.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_l015v_group_l015v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=2, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupL015.xsd",
        is_valid=True,
        instance="msData/group/groupL015.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_l014v_group_l014v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=1, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupL014.xsd",
        is_valid=True,
        instance="msData/group/groupL014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_l013v_group_l013v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=0, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupL013.xsd",
        is_valid=True,
        instance="msData/group/groupL013.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_l012v_group_l012v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=2, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupL012.xsd",
        is_valid=True,
        instance="msData/group/groupL012.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_l011v_group_l011v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=1, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupL011.xsd",
        is_valid=True,
        instance="msData/group/groupL011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_l010v_group_l010v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=0, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupL010.xsd",
        is_valid=True,
        instance="msData/group/groupL010.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_l009v_group_l009v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=0, minOccurs=0, maxOccurs=999999999
    """
    assert_bindings(
        schema="msData/group/groupL009.xsd",
        is_valid=True,
        instance="msData/group/groupL009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_l008v_group_l008v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=1, minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/group/groupL008.xsd",
        is_valid=True,
        instance="msData/group/groupL008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_l007_group_l007_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=0, minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/group/groupL007.xsd",
        is_valid=True,
        instance="msData/group/groupL007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_l006v_group_l006v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=2, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupL006.xsd",
        is_valid=True,
        instance="msData/group/groupL006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_l005v_group_l005v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=1, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupL005.xsd",
        is_valid=True,
        instance="msData/group/groupL005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_l004v_group_l004v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=0, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupL004.xsd",
        is_valid=True,
        instance="msData/group/groupL004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_l003v_group_l003v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=2, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupL003.xsd",
        is_valid=True,
        instance="msData/group/groupL003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_l002v_group_l002v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=1, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupL002.xsd",
        is_valid=True,
        instance="msData/group/groupL002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_l001v_group_l001v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: elements in
    instant XML=0, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupL001.xsd",
        is_valid=True,
        instance="msData/group/groupL001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_k005v_group_k005v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: check that
    maxOccurs default is 1, elements in instant XML = 2, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupK005.xsd",
        is_valid=True,
        instance="msData/group/groupK005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_k004v_group_k004v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: check that
    minOccurs default is 1, elements in instant XML = 1, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupK004.xsd",
        is_valid=True,
        instance="msData/group/groupK004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_k003v_group_k003v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is choice: check that
    minOccurs default is 1, elements in instant XML = 0, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupK003.xsd",
        is_valid=True,
        instance="msData/group/groupK003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_j021v_group_j021v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=3, maxOccurs=unbounded
    """
    assert_bindings(
        schema="msData/group/groupJ021.xsd",
        is_valid=True,
        instance="msData/group/groupJ021.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_j019v_group_j019v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=3, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupJ019.xsd",
        is_valid=True,
        instance="msData/group/groupJ019.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_j018v_group_j018v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=2, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupJ018.xsd",
        is_valid=True,
        instance="msData/group/groupJ018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_j017v_group_j017v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=1, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupJ017.xsd",
        is_valid=True,
        instance="msData/group/groupJ017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_j016v_group_j016v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=0, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupJ016.xsd",
        is_valid=True,
        instance="msData/group/groupJ016.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_j015v_group_j015v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=2, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupJ015.xsd",
        is_valid=True,
        instance="msData/group/groupJ015.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_j014v_group_j014v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=1, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupJ014.xsd",
        is_valid=True,
        instance="msData/group/groupJ014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_j013v_group_j013v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=0, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupJ013.xsd",
        is_valid=True,
        instance="msData/group/groupJ013.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_j012v_group_j012v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=2, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupJ012.xsd",
        is_valid=True,
        instance="msData/group/groupJ012.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_j011v_group_j011v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=1, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupJ011.xsd",
        is_valid=True,
        instance="msData/group/groupJ011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_j010v_group_j010v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=0, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupJ010.xsd",
        is_valid=True,
        instance="msData/group/groupJ010.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_j009v_group_j009v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=0, minOccurs=0, maxOccurs=99999999999
    """
    assert_bindings(
        schema="msData/group/groupJ009.xsd",
        is_valid=True,
        instance="msData/group/groupJ009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_j008v_group_j008v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=1, minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/group/groupJ008.xsd",
        is_valid=True,
        instance="msData/group/groupJ008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_j007v_group_j007v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=0, minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/group/groupJ007.xsd",
        is_valid=True,
        instance="msData/group/groupJ007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_j006v_group_j006v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=2, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupJ006.xsd",
        is_valid=True,
        instance="msData/group/groupJ006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_j005v_group_j005v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=1, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupJ005.xsd",
        is_valid=True,
        instance="msData/group/groupJ005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_j004v_group_j004v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=0, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupJ004.xsd",
        is_valid=True,
        instance="msData/group/groupJ004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_j003v_group_j003v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=2, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupJ003.xsd",
        is_valid=True,
        instance="msData/group/groupJ003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_j002v_group_j002v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=1, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupJ002.xsd",
        is_valid=True,
        instance="msData/group/groupJ002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_j001v_group_j001v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: elements in
    instant XML=0, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupJ001.xsd",
        is_valid=True,
        instance="msData/group/groupJ001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_i005v_group_i005v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: check that
    maxOccurs default is 1, elements in instant XML = 2, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupI005.xsd",
        is_valid=True,
        instance="msData/group/groupI005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_group_i004v_group_i004v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: check that
    minOccurs default is 1, elements in instant XML = 1, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupI004.xsd",
        is_valid=True,
        instance="msData/group/groupI004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_i003v_group_i003v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is sequence: check that
    minOccurs default is 1, elements in instant XML = 0, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupI003.xsd",
        is_valid=True,
        instance="msData/group/groupI003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_h019v_group_h019v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=3, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupH019.xsd",
        is_valid=True,
        instance="msData/group/groupH019.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_group_h018v_group_h018v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=2, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupH018.xsd",
        is_valid=True,
        instance="msData/group/groupH018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_group_h017v_group_h017v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=1, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupH017.xsd",
        is_valid=True,
        instance="msData/group/groupH017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_h016v_group_h016v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=0, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupH016.xsd",
        is_valid=True,
        instance="msData/group/groupH016.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_h015v_group_h015v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=2, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupH015.xsd",
        is_valid=True,
        instance="msData/group/groupH015.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_group_h014v_group_h014v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=1, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupH014.xsd",
        is_valid=True,
        instance="msData/group/groupH014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_h013v_group_h013v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=0, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupH013.xsd",
        is_valid=True,
        instance="msData/group/groupH013.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_h012v_group_h012v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=2, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupH012.xsd",
        is_valid=True,
        instance="msData/group/groupH012.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_h011v_group_h011v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=1, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupH011.xsd",
        is_valid=True,
        instance="msData/group/groupH011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_h010v_group_h010v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=0, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupH010.xsd",
        is_valid=True,
        instance="msData/group/groupH010.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_h009v_group_h009v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=0, minOccurs=0, maxOccurs=999999999999999
    """
    assert_bindings(
        schema="msData/group/groupH009.xsd",
        is_valid=True,
        instance="msData/group/groupH009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_h008v_group_h008v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=1, minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/group/groupH008.xsd",
        is_valid=True,
        instance="msData/group/groupH008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_h006v_group_h006v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=2, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupH006.xsd",
        is_valid=True,
        instance="msData/group/groupH006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_h005v_group_h005v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=1, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupH005.xsd",
        is_valid=True,
        instance="msData/group/groupH005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_h004v_group_h004v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=0, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupH004.xsd",
        is_valid=True,
        instance="msData/group/groupH004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_h003v_group_h003v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=2, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupH003.xsd",
        is_valid=True,
        instance="msData/group/groupH003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_h002v_group_h002v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=1, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupH002.xsd",
        is_valid=True,
        instance="msData/group/groupH002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_h001v_group_h001v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: elements in
    instant XML=0, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupH001.xsd",
        is_valid=True,
        instance="msData/group/groupH001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_g005v_group_g005v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: check that
    maxOccurs default is 1, elements in instant XML = 2, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupG005.xsd",
        is_valid=True,
        instance="msData/group/groupG005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_g004v_group_g004v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: check that
    minOccurs default is 1, elements in instant XML = 1, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupG004.xsd",
        is_valid=True,
        instance="msData/group/groupG004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_g003v_group_g003v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is restriction: check that
    minOccurs default is 1, elements in instant XML = 0, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupG003.xsd",
        is_valid=True,
        instance="msData/group/groupG003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_group_f021v_group_f021v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=3, maxOccurs=unbounded
    """
    assert_bindings(
        schema="msData/group/groupF021.xsd",
        is_valid=True,
        instance="msData/group/groupF021.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_f019v_group_f019v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=3, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupF019.xsd",
        is_valid=True,
        instance="msData/group/groupF019.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_f018v_group_f018v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=2, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupF018.xsd",
        is_valid=True,
        instance="msData/group/groupF018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_f017v_group_f017v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=1, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupF017.xsd",
        is_valid=True,
        instance="msData/group/groupF017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_f016v_group_f016v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=0, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupF016.xsd",
        is_valid=True,
        instance="msData/group/groupF016.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_f015v_group_f015v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=2, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupF015.xsd",
        is_valid=True,
        instance="msData/group/groupF015.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_f014v_group_f014v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=1, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupF014.xsd",
        is_valid=True,
        instance="msData/group/groupF014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_f013v_group_f013v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=0, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupF013.xsd",
        is_valid=True,
        instance="msData/group/groupF013.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_f012v_group_f012v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=2, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupF012.xsd",
        is_valid=True,
        instance="msData/group/groupF012.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_f011v_group_f011v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=1, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupF011.xsd",
        is_valid=True,
        instance="msData/group/groupF011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_f010v_group_f010v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=0, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupF010.xsd",
        is_valid=True,
        instance="msData/group/groupF010.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_f009v_group_f009v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=0, minOccurs=0, maxOccurs=999999999999999999999
    """
    assert_bindings(
        schema="msData/group/groupF009.xsd",
        is_valid=True,
        instance="msData/group/groupF009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_f008v_group_f008v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=1, minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/group/groupF008.xsd",
        is_valid=True,
        instance="msData/group/groupF008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_f007v_group_f007v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=0, minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/group/groupF007.xsd",
        is_valid=True,
        instance="msData/group/groupF007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_f006v_group_f006v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=2, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupF006.xsd",
        is_valid=True,
        instance="msData/group/groupF006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_f005v_group_f005v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=1, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupF005.xsd",
        is_valid=True,
        instance="msData/group/groupF005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_f004v_group_f004v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=0, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupF004.xsd",
        is_valid=True,
        instance="msData/group/groupF004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_f003v_group_f003v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=2, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupF003.xsd",
        is_valid=True,
        instance="msData/group/groupF003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_f002v_group_f002v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=1, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupF002.xsd",
        is_valid=True,
        instance="msData/group/groupF002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_f001v_group_f001v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: elements in
    instant XML=0, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupF001.xsd",
        is_valid=True,
        instance="msData/group/groupF001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_e005v_group_e005v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: check that
    maxOccurs default is 1, elements in instant XML = 2, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupE005.xsd",
        is_valid=True,
        instance="msData/group/groupE005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_e004v_group_e004v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: check that
    minOccurs default is 1, elements in instant XML = 1, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupE004.xsd",
        is_valid=True,
        instance="msData/group/groupE004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_e003v_group_e003v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is extension: check that
    minOccurs default is 1, elements in instant XML = 0, minOccurs=absent,
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupE003.xsd",
        is_valid=True,
        instance="msData/group/groupE003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_b010v_group_b010v_v():
    """
    TEST :Syntax Checking (id, ref) : Test ref:, parent is extension,
    ref='global group from included xsd"
    """
    assert_bindings(
        schema="msData/group/groupB010.xsd",
        is_valid=True,
        instance="msData/group/groupB010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_b009v_group_b009v_v():
    """
    TEST :Syntax Checking (id, ref) : Test ref:, parent is extension,
    ref='global group from imported xsd"
    """
    assert_bindings(
        schema="msData/group/groupB009.xsd",
        is_valid=True,
        instance="msData/group/groupB009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_b006v_group_b006v_v():
    """
    TEST :Syntax Checking (id, ref) : Test ref:, parent is complexType,
    ref='global group'
    """
    assert_bindings(
        schema="msData/group/groupB006.xsd",
        is_valid=True,
        instance="msData/group/groupB006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_group_b005v_group_b005v_v():
    """
    TEST :Syntax Checking (id, ref) : Test ref:, parent is choice,
    ref='global group'
    """
    assert_bindings(
        schema="msData/group/groupB005.xsd",
        is_valid=True,
        instance="msData/group/groupB005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_b004v_group_b004v_v():
    """
    TEST :Syntax Checking (id, ref) : Test ref:, parent is sequence,
    ref='global group'
    """
    assert_bindings(
        schema="msData/group/groupB004.xsd",
        is_valid=True,
        instance="msData/group/groupB004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_b003v_group_b003v_v():
    """
    TEST :Syntax Checking (id, ref) : Test ref:, parent is restriction,
    ref='global group'
    """
    assert_bindings(
        schema="msData/group/groupB003.xsd",
        is_valid=True,
        instance="msData/group/groupB003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_b002v_group_b002v_v():
    """
    TEST :Syntax Checking (id, ref) : Test ref:, parent is extension,
    ref='global group'
    """
    assert_bindings(
        schema="msData/group/groupB002.xsd",
        is_valid=True,
        instance="msData/group/groupB002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_id_z015_id_z015_i():
    """
    TEST :Identity-constraint Definition Schema Component : XSD: test
    Identity constraint field: evaluate to anyAttribute with lax or skip
    TSTF concludes after some deliberation that for 1.0 this is indeed
    invalid:  see bugzilla for detailed discussion
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ015.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ015.xml",
        instance_is_valid=False,
        class_name="Foo",
        version="1.0",
    )


def test_id_z012_id_z012_i():
    """
    TEST :Identity-constraint Definition Schema Component : processing
    default/fixed xsd attributes typed IDREF/IDREFS in the instance
    document.
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ012.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ012.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_z011_a_id_z011_a_i():
    """
    TEST :Identity-constraint Definition Schema Component : xsd: multiple
    instance of an element with attribute having xs:unique which has a
    default or fixed value set, should error.
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ011_a.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ011_a.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_z011_id_z011_i():
    """
    TEST :Identity-constraint Definition Schema Component : xsd: multiple
    instance of an element with attribute typed as xsd:ID and has a
    default or fixed value set, should error. TSTF says 'fixed' ID attr in
    schema is invalid, instance testing disabled Allowed in XSD 1.1 - MHK
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ011.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ011.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


def test_id_z010_id_z010_i():
    """
    TEST :Identity-constraint Definition Schema Component : xsd idendity
    constraint key/keyref is not resolving correctly, wrong namespace is
    applied to keyref declaration.
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ010.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ010.xml",
        instance_is_valid=False,
        class_name="Root1",
        version="1.0",
    )


def test_id_z008_id_z008_i():
    """
    TEST :Identity-constraint Definition Schema Component : xsd: test
    keyref with value that does not have a relative key defined.
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ008.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ008.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_z007_id_z007_v():
    """
    TEST :Identity-constraint Definition Schema Component : Values of
    simple types derived from built-in types should always be comparable
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ007.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ007.xml",
        instance_is_valid=True,
        class_name="NewDataSet",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_z006_id_z006_v():
    """
    TEST :Identity-constraint Definition Schema Component : test
    Validation of keys when more than one key is defined
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ006.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ006.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_z005_id_z005_v():
    """
    TEST :Identity-constraint Definition Schema Component : test
    Validation of keys when more than one key is defined
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ005.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ005.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_z004_id_z004_i():
    """
    TEST :Identity-constraint Definition Schema Component : 71477 - XSD
    IdentityConstraint: placing IC on undeclared element in instance
    document
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ004.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ004.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_z002_id_z002_i():
    """
    TEST :Identity-constraint Definition Schema Component : 70981 -
    invalid line numbers in XPath validation errors
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ002.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ002.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_z001_id_z001_i():
    """
    TEST :Identity-constraint Definition Schema Component : 70955 -
    identityConstraint : key attempting to validate missing element
    """
    assert_bindings(
        schema="msData/identityConstraint/idZ001.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idZ001.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l103_id_l103_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='@ncname:*' , selector contains qname |
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL103.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL103.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_l102_id_l102_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='@ncname:*' , selector contains qname |
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL102.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL102.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l101_id_l101_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='@*' , selector contains qname | qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL101.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL101.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l100_id_l100_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='@*' , selector contains qname | qname1
    TSTF decided test was coherent but polarity should be reversed
    """
    assert_bindings(
        schema="msData/identityConstraint/idL100.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL100.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l099_id_l099_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='@qname' , selector contains qname |
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL099.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL099.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_l098_id_l098_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='@qname' , selector contains qname |
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL098.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL098.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l097_id_l097_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='ncname:*' , selector contains qname |
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL097.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL097.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l096_id_l096_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='ncname:*' , selector contains qname |
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL096.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL096.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l095_id_l095_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='*' , selector contains qname | qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL095.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL095.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l094_id_l094_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='*' , selector contains qname | qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL094.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL094.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l093_id_l093_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='qname' , selector contains qname |
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL093.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL093.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l092_id_l092_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='qname' , selector contains qname |
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL092.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL092.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l091_id_l091_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='.' , selector contains qname | qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL091.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL091.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l090_id_l090_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test for path
    | path of selector field xpath='.' , selector contains qname | qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL090.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL090.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l089_id_l089_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='@ncname:* ;qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL089.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL089.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l088_id_l088_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='@ncname:* ; qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL088.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL088.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l087_id_l087_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='@* ; qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL087.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL087.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l086_id_l086_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='@* ; qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL086.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL086.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l085_id_l085_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='@qname ; qname1' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL085.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL085.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l084_id_l084_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='@qname ; qname1' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL084.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL084.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l083_id_l083_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='ncname:* ; qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL083.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL083.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l082_id_l082_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='ncname:* ; qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL082.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL082.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l081_id_l081_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='* ; qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL081.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL081.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l080_id_l080_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='* ; qname' , selector contains *, keyref
    with field="*". Should fail because it allow only single node.
    """
    assert_bindings(
        schema="msData/identityConstraint/idL080.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL080.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l079_id_l079_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='qname ; qname1' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL079.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL079.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l078_id_l078_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='qname ; qname1' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL078.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL078.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l077a_id_l077_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='. ; qname' , selector contains *
    Resolution pending decision about issue 5780 against the 1.0 spec.
    """
    assert_bindings(
        schema="msData/identityConstraint/idL077.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL077.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l077_id_l077_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='. ; qname' , selector contains *
    Resolution pending decision about issue 5780 against the 1.0 spec.
    """
    assert_bindings(
        schema="msData/identityConstraint/idL077.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL077.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l076a_id_l076_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='. ; qname' , selector contains *
    Resolution pending decision about issue 5780 against the 1.0 spec.
    """
    assert_bindings(
        schema="msData/identityConstraint/idL076.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL076.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l076_id_l076_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test multiple
    field statements field xpath='. ; qname' , selector contains *
    Resolution pending decision about issue 5780 against the 1.0 spec.
    """
    assert_bindings(
        schema="msData/identityConstraint/idL076.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL076.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l075_id_l075_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for keyref definition, field xpath='@ncname:*' , selector contains
    *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL075.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL075.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l074_id_l074_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='attribute::ncname:*' , selector
    contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL074.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL074.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l073_id_l073_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='@ncname:*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL073.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL073.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l072_id_l072_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for keyref definition, field xpath='@*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL072.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL072.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l071_id_l071_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='attribute::*' , selector contains
    *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL071.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL071.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l070_id_l070_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='@*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL070.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL070.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l069_id_l069_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for keyref definition, field xpath='@qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL069.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL069.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l068_id_l068_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='attribute::qname' , selector
    contains .//qname1/qname2
    """
    assert_bindings(
        schema="msData/identityConstraint/idL068.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL068.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l067_id_l067_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='attribute::qname' , selector
    contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL067.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL067.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l066_id_l066_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='@qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL066.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL066.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l065_id_l065_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for keyref definition, field xpath='ncname:*' , selector contains
    *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL065.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL065.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l064_id_l064_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='child::ncname:*' , selector
    contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL064.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL064.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l063_id_l063_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='ncname:*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL063.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL063.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l062_id_l062_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for keyref definition, field xpath='*' , selector contains
    .//qname
    """
    assert_bindings(
        schema="msData/identityConstraint/idL062.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL062.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l061_id_l061_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for keyref definition, field xpath='*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL061.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL061.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l060_id_l060_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='child::*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL060.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL060.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l059_id_l059_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='*' , selector contains .//qname
    """
    assert_bindings(
        schema="msData/identityConstraint/idL059.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL059.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l058_id_l058_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL058.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL058.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l057_id_l057_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for keyref definition, field xpath='.//qname' , selector contains
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL057.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL057.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l056_id_l056_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for keyref definition, field xpath='qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL056.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL056.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l055_id_l055_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='.//qname' , selector contains
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL055.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL055.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l054_id_l054_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='child::qname' , selector contains
    *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL054.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL054.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l053_id_l053_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL053.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL053.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l052_id_l052_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for keyref definition, field xpath='.' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL052.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL052.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l051_id_l051_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for keyref definition, field xpath='.' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL051.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL051.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l050_id_l050_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for key definition, field xpath='@ncname:*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL050.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL050.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l049_id_l049_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='attribute::ncname:*' , selector
    contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL049.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL049.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l048_id_l048_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='@ncname:*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL048.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL048.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l047_id_l047_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for key definition, field xpath='@*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL047.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL047.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l046_id_l046_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='attribute::*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL046.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL046.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l045_id_l045_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='@*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL045.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL045.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l044_id_l044_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for key definition, field xpath='@qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL044.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL044.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l043_id_l043_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='attribute::qname' , selector contains
    .//qname1/qname2
    """
    assert_bindings(
        schema="msData/identityConstraint/idL043.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL043.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l042_id_l042_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='attribute::qname' , selector contains
    *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL042.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL042.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l041_id_l041_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='@qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL041.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL041.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l040_id_l040_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for key definition, field xpath='ncname:*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL040.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL040.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l039_id_l039_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='child::ncname:*' , selector contains
    *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL039.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL039.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l038_id_l038_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='ncname:*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL038.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL038.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l037_id_l037_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for key definition, field xpath='*' , selector contains .//qname
    """
    assert_bindings(
        schema="msData/identityConstraint/idL037.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL037.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l036_id_l036_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for key definition, field xpath='*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL036.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL036.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l035_id_l035_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='child::*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL035.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL035.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l034_id_l034_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='*' , selector contains .//qname
    """
    assert_bindings(
        schema="msData/identityConstraint/idL034.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL034.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l033_id_l033_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL033.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL033.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l032_id_l032_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for key definition, field xpath='.//qname' , selector contains
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL032.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL032.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l031_id_l031_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for key definition, field xpath='qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL031.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL031.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l030_id_l030_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='.//qname' , selector contains qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL030.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL030.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l029_id_l029_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='child::qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL029.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL029.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l028_id_l028_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL028.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL028.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l027_id_l027_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for key definition, field xpath='.' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL027.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL027.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l026_id_l026_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for key definition, field xpath='.' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL026.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL026.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l025_id_l025_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for unique definition, field xpath='@ncname:*' , selector contains
    *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL025.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL025.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l024_id_l024_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='attribute::ncname:*' , selector
    contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL024.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL024.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l023_id_l023_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='@ncname:*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL023.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL023.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l022_id_l022_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for unique definition, field xpath='@*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL022.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL022.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l021_id_l021_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='attribute::*' , selector contains
    *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL021.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL021.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l020_id_l020_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='@*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL020.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL020.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l019_id_l019_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for unique definition, field xpath='@qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL019.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL019.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l018_id_l018_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='attribute::qname' , selector
    contains .//qname1/qname2
    """
    assert_bindings(
        schema="msData/identityConstraint/idL018.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL018.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l017_id_l017_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='attribute::qname' , selector
    contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL017.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL017.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l016_id_l016_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='@qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL016.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL016.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l015_id_l015_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for unique definition, field xpath='ncname:*' , selector contains
    *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL015.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL015.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l014_id_l014_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='child::ncname:*' , selector
    contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL014.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL014.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l013_id_l013_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='ncname:*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL013.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL013.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l012_id_l012_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for unique definition, field xpath='*' , selector contains
    .//qname
    """
    assert_bindings(
        schema="msData/identityConstraint/idL012.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL012.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l011_id_l011_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for unique definition, field xpath='*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL011.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL011.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l010_id_l010_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='child::*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL010.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL010.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l009_id_l009_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='*' , selector contains .//qname
    """
    assert_bindings(
        schema="msData/identityConstraint/idL009.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL009.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l008_id_l008_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='*' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL008.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL008.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l007_id_l007_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for unique definition, field xpath='.//qname' , selector contains
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL007.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL007.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l006_id_l006_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for unique definition, field xpath='qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL006.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL006.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l005_id_l005_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='.//qname' , selector contains
    qname1
    """
    assert_bindings(
        schema="msData/identityConstraint/idL005.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL005.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l004_id_l004_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='child::qname' , selector contains
    *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL004.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l003_id_l003_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='qname' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL003.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL003.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_l002_id_l002_i():
    """
    TEST :Identity-constraint Definition Schema Component : Test invalid
    XML for unique definition, field xpath='.' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL002.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL002.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_l001_id_l001_v():
    """
    TEST :Identity-constraint Definition Schema Component : Test valid XML
    for unique definition, field xpath='.' , selector contains *
    """
    assert_bindings(
        schema="msData/identityConstraint/idL001.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idL001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k017_id_k017_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref defined
    locally within key scope
    """
    assert_bindings(
        schema="msData/identityConstraint/idK017.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK017.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k015_id_k015_v():
    """
    TEST :Identity-constraint Definition Schema Component : constraint
    locating an element that is of simpleType/union
    """
    assert_bindings(
        schema="msData/identityConstraint/idK015.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK015.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k014_id_k014_v():
    """
    TEST :Identity-constraint Definition Schema Component : constraint
    locating an element that is of simpleType/list
    """
    assert_bindings(
        schema="msData/identityConstraint/idK014.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK014.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k013_id_k013_v():
    """
    TEST :Identity-constraint Definition Schema Component : constraint
    locating an element that is of simpleType/restriction
    """
    assert_bindings(
        schema="msData/identityConstraint/idK013.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK013.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_k012_id_k012_i():
    """
    TEST :Identity-constraint Definition Schema Component : constraint
    locating an element that is of complexType/complexContent
    """
    assert_bindings(
        schema="msData/identityConstraint/idK012.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK012.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_k011a_id_k011_v():
    """
    TEST :Identity-constraint Definition Schema Component : constraint
    locating an element that is of complexType/simpleContent Resolution
    pending decision about issue 5780 against the 1.0 spec.
    """
    assert_bindings(
        schema="msData/identityConstraint/idK011.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK011.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k011_id_k011_v():
    """
    TEST :Identity-constraint Definition Schema Component : constraint
    locating an element that is of complexType/simpleContent Resolution
    pending decision about issue 5780 against the 1.0 spec.
    """
    assert_bindings(
        schema="msData/identityConstraint/idK011.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK011.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k010_id_k010_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref fields
    locating an element refers to a unique locating an element
    """
    assert_bindings(
        schema="msData/identityConstraint/idK010.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK010.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k009_id_k009_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref fields
    locating an element refers to a key locating an element
    """
    assert_bindings(
        schema="msData/identityConstraint/idK009.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK009.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k008_id_k008_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref fields
    locating an attribute refers to a unique locating an attribute
    """
    assert_bindings(
        schema="msData/identityConstraint/idK008.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK008.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k007_id_k007_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref fields
    locating an attribute refers to a key locating an attribute
    """
    assert_bindings(
        schema="msData/identityConstraint/idK007.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK007.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k006_id_k006_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref fields
    locating an element refers to a unique locating an attribute
    """
    assert_bindings(
        schema="msData/identityConstraint/idK006.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK006.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k005_id_k005_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref fields
    locating an element refers to a key locating an attribute
    """
    assert_bindings(
        schema="msData/identityConstraint/idK005.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK005.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k004_id_k004_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref fields
    locating an attribute subject to normalization refers to a key
    locating an element that is not normalized , postnormalization values
    are the same
    """
    assert_bindings(
        schema="msData/identityConstraint/idK004.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k003_id_k003_i():
    """
    TEST :Identity-constraint Definition Schema Component : keyref fields
    locating an attribute subject to normalization refers to a key
    locating an element that is not normalized , prenormalization values
    are the same
    """
    assert_bindings(
        schema="msData/identityConstraint/idK003.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK003.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_k002_id_k002_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref fields
    locating an attribute refers to a unique locating an element
    """
    assert_bindings(
        schema="msData/identityConstraint/idK002.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK002.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_k001_id_k001_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref fields
    locating an attribute refers to a key locating an element
    """
    assert_bindings(
        schema="msData/identityConstraint/idK001.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idK001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h034_id_h034_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field points to attribute used only within xsi:type
    substitution
    """
    assert_bindings(
        schema="msData/identityConstraint/idH034.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH034.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h032_id_h032_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field points to attribute from redefined schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idH032.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH032.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h031a_id_h031_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field points to attribute from imported schema Resolution
    pending decision about issue 5780 against the 1.0 spec.
    """
    assert_bindings(
        schema="msData/identityConstraint/idH031.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH031.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h031_id_h031_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field points to attribute from imported schema Resolution
    pending decision about issue 5780 against the 1.0 spec.
    """
    assert_bindings(
        schema="msData/identityConstraint/idH031.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH031.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h030_id_h030_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field points to attribute within targetNamespace
    """
    assert_bindings(
        schema="msData/identityConstraint/idH030.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH030.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h029_id_h029_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field points to element redefined by use of
    substitutionGroup
    """
    assert_bindings(
        schema="msData/identityConstraint/idH029.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH029.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h028_id_h028_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field points to element from redefined schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idH028.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH028.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h027_id_h027_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field points to element from imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idH027.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH027.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h026_id_h026_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field points to element outside targetNamespace in non-
    imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idH026.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH026.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h025_id_h025_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field points to element within targetNamespace
    """
    assert_bindings(
        schema="msData/identityConstraint/idH025.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH025.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h024_id_h024_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, selector points to element redefined by use of
    substitutionGroup
    """
    assert_bindings(
        schema="msData/identityConstraint/idH024.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH024.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h023_id_h023_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, selector points to element from redefined schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idH023.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH023.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h022_id_h022_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, selector points to element from imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idH022.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH022.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h021_id_h021_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, selector points to element outside of targetNamespace in a
    non-imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idH021.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH021.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_h020_id_h020_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, selector points to element within targetNamespace
    """
    assert_bindings(
        schema="msData/identityConstraint/idH020.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH020.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h019_id_h019_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, qualified node set defined with the use of multiple field
    schema elements pointing to a mix of elements and attributes
    """
    assert_bindings(
        schema="msData/identityConstraint/idH019.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH019.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h018_id_h018_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, qualified node set defined with the use of multiple field
    schema elements pointing to only attributes
    """
    assert_bindings(
        schema="msData/identityConstraint/idH018.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH018.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h017_id_h017_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, qualified node set defined with the use of multiple field
    schema elements pointing to only elements
    """
    assert_bindings(
        schema="msData/identityConstraint/idH017.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH017.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h016_id_h016_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, instance member (a)=test, string; instance member (b)='',
    string defined using fixed='test'
    """
    assert_bindings(
        schema="msData/identityConstraint/idH016.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH016.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h015_id_h015_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, instance member (a)=test, string; instance member (b)='',
    string defined using default='test'
    """
    assert_bindings(
        schema="msData/identityConstraint/idH015.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH015.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h012_id_h012_i():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, keyref fields are defined in a different order than referred
    key fields
    """
    assert_bindings(
        schema="msData/identityConstraint/idH012.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH012.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_h010_id_h010_i():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, keyref refers to unique element whose value is nil
    """
    assert_bindings(
        schema="msData/identityConstraint/idH010.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH010.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_h009_id_h009_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, keyref refers to unique element
    """
    assert_bindings(
        schema="msData/identityConstraint/idH009.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH009.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h008_id_h008_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, keyref refers to existing key element defined post to keyref
    """
    assert_bindings(
        schema="msData/identityConstraint/idH008.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH008.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h007_id_h007_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, keyref refers to existing key element defined prior to
    keyref
    """
    assert_bindings(
        schema="msData/identityConstraint/idH007.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH007.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h006_id_h006_i():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field element evaluates to a node-set with a member that is
    not a simple type
    """
    assert_bindings(
        schema="msData/identityConstraint/idH006.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH006.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_h005_id_h005_i():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field element evaluates to a node-set with more than one
    member
    """
    assert_bindings(
        schema="msData/identityConstraint/idH005.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH005.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_h004_id_h004_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field element evaluates to a node-set with only one member
    """
    assert_bindings(
        schema="msData/identityConstraint/idH004.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h003_id_h003_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, field element evaluates to an empty-node set
    """
    assert_bindings(
        schema="msData/identityConstraint/idH003.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH003.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_h001_id_h001_v():
    """
    TEST :Identity-constraint Definition Schema Component : keyref
    category, selector element evaluates to a node-set
    """
    assert_bindings(
        schema="msData/identityConstraint/idH001.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idH001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_g030_id_g030_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field points to attribute used only within xsi:type substitution
    """
    assert_bindings(
        schema="msData/identityConstraint/idG030.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG030.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_g029_id_g029_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field points to attribute outside targetNamespace in non-imported
    schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idG029.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG029.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_g028_id_g028_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field points to attribute from redefined schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idG028.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG028.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g027_id_g027_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field points to attribute from imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idG027.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG027.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g026_id_g026_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field points to attribute within targetNamespace
    """
    assert_bindings(
        schema="msData/identityConstraint/idG026.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG026.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g025_id_g025_i():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field points to element redefined by use of substitutionGroup
    """
    assert_bindings(
        schema="msData/identityConstraint/idG025.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG025.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_g024_id_g024_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field points to element from redefined schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idG024.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG024.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g023_id_g023_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field points to element from imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idG023.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG023.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_g022_id_g022_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field points to element outside targetNamespace in non-imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idG022.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG022.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g021_id_g021_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field points to element within targetNamespace
    """
    assert_bindings(
        schema="msData/identityConstraint/idG021.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG021.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g020_id_g020_i():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    selector points to element redefined by use of substitutionGroup
    """
    assert_bindings(
        schema="msData/identityConstraint/idG020.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG020.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_g019_id_g019_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    selector points to element from redefined schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idG019.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG019.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g018_id_g018_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    selector points to element from imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idG018.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG018.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_g017_id_g017_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    selector points to element outside of targetNamespace in a non-
    imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idG017.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG017.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_g016_id_g016_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    selector points to element within targetNamespace
    """
    assert_bindings(
        schema="msData/identityConstraint/idG016.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG016.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g015_id_g015_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    qualified node set defined with the use of multiple field schema
    elements pointing to a mix of elements and attributes
    """
    assert_bindings(
        schema="msData/identityConstraint/idG015.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG015.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g014_id_g014_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    qualified node set defined with the use of multiple field schema
    elements pointing to only attributes
    """
    assert_bindings(
        schema="msData/identityConstraint/idG014.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG014.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g013_id_g013_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    qualified node set defined with the use of multiple field schema
    elements pointing to only elements
    """
    assert_bindings(
        schema="msData/identityConstraint/idG013.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG013.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g012_id_g012_i():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    instance member (a)=test, string; instance member (b)='', string
    defined using fixed='test'
    """
    assert_bindings(
        schema="msData/identityConstraint/idG012.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG012.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_g011_id_g011_i():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    instance member (a)=test, string; instance member (b)='', string
    defined using default='test'
    """
    assert_bindings(
        schema="msData/identityConstraint/idG011.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG011.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_g010_id_g010_i():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    qualified node set contains members are that are not unique.
    """
    assert_bindings(
        schema="msData/identityConstraint/idG010.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG010.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_g009_id_g009_i():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    qualified node set contains members with an element declaration whose
    {nillable} is true.
    """
    assert_bindings(
        schema="msData/identityConstraint/idG009.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG009.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_g008_id_g008_i():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    some target node set members do not exist in qualified node set
    """
    assert_bindings(
        schema="msData/identityConstraint/idG008.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG008.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_g007_id_g007_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    all target node set members exist in qualified node set
    """
    assert_bindings(
        schema="msData/identityConstraint/idG007.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG007.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g006_id_g006_i():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field element evaluates to a node-set with a member that is not a
    simple type
    """
    assert_bindings(
        schema="msData/identityConstraint/idG006.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG006.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_g005_id_g005_i():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field element evaluates to a node-set with more than one member
    """
    assert_bindings(
        schema="msData/identityConstraint/idG005.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG005.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_g004_id_g004_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field element evaluates to a node-set with only one member
    """
    assert_bindings(
        schema="msData/identityConstraint/idG004.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_g003_id_g003_i():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    field element evaluates to an empty-node set
    """
    assert_bindings(
        schema="msData/identityConstraint/idG003.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG003.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_g001_id_g001_v():
    """
    TEST :Identity-constraint Definition Schema Component : key category,
    selector element evaluates to a node-set
    """
    assert_bindings(
        schema="msData/identityConstraint/idG001.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idG001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f036_id_f036_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field points to attribute used only within xsi:type
    substitution
    """
    assert_bindings(
        schema="msData/identityConstraint/idF036.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF036.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f035_id_f035_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field points to attribute outside targetNamespace in non-
    imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idF035.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF035.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f034_id_f034_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field points to attribute from redefined schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idF034.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF034.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f033_id_f033_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field points to attribute from imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idF033.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF033.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f032_id_f032_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field points to attribute within targetNamespace
    """
    assert_bindings(
        schema="msData/identityConstraint/idF032.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF032.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f031_id_f031_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field points to element redefined by use of
    substitutionGroup
    """
    assert_bindings(
        schema="msData/identityConstraint/idF031.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF031.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f030_id_f030_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field points to element from redefined schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idF030.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF030.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f029_id_f029_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field points to element from imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idF029.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF029.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f028_id_f028_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field points to element outside targetNamespace in non-
    imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idF028.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF028.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f027_id_f027_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field points to element within targetNamespace
    """
    assert_bindings(
        schema="msData/identityConstraint/idF027.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF027.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f026_id_f026_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, selector points to element redefined by use of
    substitutionGroup
    """
    assert_bindings(
        schema="msData/identityConstraint/idF026.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF026.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f025_id_f025_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, selector points to element from redefined schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idF025.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF025.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f024_id_f024_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, selector points to element from imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idF024.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF024.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f023_id_f023_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, selector points to element outside of targetNamespace in a
    non-imported schema
    """
    assert_bindings(
        schema="msData/identityConstraint/idF023.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF023.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f022_id_f022_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, selector points to element within targetNamespace
    """
    assert_bindings(
        schema="msData/identityConstraint/idF022.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF022.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f021_id_f021_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, qualified node set defined with the use of multiple field
    schema elements pointing to a mix of elements and attributes
    """
    assert_bindings(
        schema="msData/identityConstraint/idF021.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF021.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f020_id_f020_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, qualified node set defined with the use of multiple field
    schema elements pointing to only attributes
    """
    assert_bindings(
        schema="msData/identityConstraint/idF020.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF020.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f019_id_f019_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, qualified node set defined with the use of multiple field
    schema elements pointing to only elements
    """
    assert_bindings(
        schema="msData/identityConstraint/idF019.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF019.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f018_id_f018_i():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, instance member (a)=nil, string; instance member (b)=nil
    """
    assert_bindings(
        schema="msData/identityConstraint/idF018.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF018.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_f017_id_f017_i():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, instance member (a)=test, string; instance member (b)='',
    string defined using fixed='test'
    """
    assert_bindings(
        schema="msData/identityConstraint/idF017.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF017.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_f016_id_f016_i():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, instance member (a)=test, string; instance member (b)='',
    string defined using default='test'
    """
    assert_bindings(
        schema="msData/identityConstraint/idF016.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF016.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f015_id_f015_i():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, instance member (a)=1, decimal; instance member (b)=1,
    unsignedByte
    """
    assert_bindings(
        schema="msData/identityConstraint/idF015.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF015.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f014_id_f014_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, instance member (a)=1, float; instance member (b)=1,
    unsignedByte
    """
    assert_bindings(
        schema="msData/identityConstraint/idF014.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF014.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f013_id_f013_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, instance member (a)=1, float; instance member (b)=1, decimal
    """
    assert_bindings(
        schema="msData/identityConstraint/idF013.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF013.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_id_f012_id_f012_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, instance member (a)=1, boolean; instance member (b)=1,
    number
    """
    assert_bindings(
        schema="msData/identityConstraint/idF012.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF012.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f011_id_f011_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, instance member (a)=3.0, string; instance member (b)=3,
    string
    """
    assert_bindings(
        schema="msData/identityConstraint/idF011.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF011.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f010_id_f010_i():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, instance member (a)=3.0, number; instance member (b)=3,
    number
    """
    assert_bindings(
        schema="msData/identityConstraint/idF010.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF010.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_f009_id_f009_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, qualified node set contains members with an element
    declaration whose {nillable} is true.
    """
    assert_bindings(
        schema="msData/identityConstraint/idF009.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF009.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f008_id_f008_i():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, not all qualified node set members are unique
    """
    assert_bindings(
        schema="msData/identityConstraint/idF008.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF008.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_f007_id_f007_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, all qualified node set members are unique
    """
    assert_bindings(
        schema="msData/identityConstraint/idF007.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF007.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f006_id_f006_i():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field element evaluates to a node-set with a member that is
    not a simple type
    """
    assert_bindings(
        schema="msData/identityConstraint/idF006.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF006.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_f005_id_f005_i():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field element evaluates to a node-set with more than one
    member
    """
    assert_bindings(
        schema="msData/identityConstraint/idF005.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF005.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_id_f004_id_f004_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field element evaluates to a node-set with only one member
    """
    assert_bindings(
        schema="msData/identityConstraint/idF004.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f003_id_f003_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, field element evaluates to an empty-node set
    """
    assert_bindings(
        schema="msData/identityConstraint/idF003.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF003.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_id_f001_id_f001_v():
    """
    TEST :Identity-constraint Definition Schema Component : unique
    category, selector element evaluates to a node-set
    """
    assert_bindings(
        schema="msData/identityConstraint/idF001.xsd",
        is_valid=True,
        instance="msData/identityConstraint/idF001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_z004_mg_z004_v():
    """
    TEST :model groups (ALL) : test occurence range of xs:choice
    """
    assert_bindings(
        schema="msData/modelGroups/mgZ004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgZ004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_z003_mg_z003_v():
    """
    TEST :model groups (ALL) : test derivation by ext. with all with
    base=empty content
    """
    assert_bindings(
        schema="msData/modelGroups/mgZ003.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgZ003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_z001_mg_z001_i():
    """
    TEST :model groups (ALL) : XSD: handling of ALL schema element when
    ALL has minOccurs=0
    """
    assert_bindings(
        schema="msData/modelGroups/mgZ001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgZ001.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_mg_q020_mg_q020_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), one under 'choice', one under 'sequence'
    inside 'choice' of 'choice'
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ020.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ020.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_q019_mg_q019_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), one under 'choice', one under 'choice'
    inside 'sequence' of 'choice'
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ019.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ019.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_q018_mg_q018_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), one under 'choice', one under 'sequence'
    inside 'sequence' of 'choice'
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ018.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_q017_mg_q017_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), one under 'sequence', one under 'choice'
    inside 'choice' of 'sequence'
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ017.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_q016_mg_q016_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), one under 'sequence', one under 'sequence'
    inside 'choice' of 'sequence'
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ016.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_q015_mg_q015_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), one under 'sequence', one under 'choice'
    inside 'sequence' of 'sequence'
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ015.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_q014_mg_q014_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), one under 'sequence', one under 'sequence'
    inside 'sequence' of 'sequence'
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ014.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_q009_mg_q009_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), one under 'choice', one under 'sequence'
    inside 'choice'
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ009.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_q008_mg_q008_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), one under 'choice', one under 'choice'
    inside 'choice'
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ008.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_q007_mg_q007_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), one under 'sequence', one under 'sequence'
    inside 'sequence'
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ007.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_q006_mg_q006_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), one under 'sequence', one under 'choice'
    inside 'sequence'
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_q003_mg_q003_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), both under choice
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ003.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_q002_mg_q002_v():
    """
    TEST :model groups (ALL) : 2 particles with idendical element
    declarations (same type), both under sequence
    """
    assert_bindings(
        schema="msData/modelGroups/mgQ002.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgQ002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o038_mg_o038_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under 'choice'
    with maxOccurs=minOccurs=1 , which is part of a complexType
    """
    assert_bindings(
        schema="msData/modelGroups/mgO038.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO038.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o037_mg_o037_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under 'sequence'
    with maxOccurs=minOccurs=1, which is part of a complexType
    """
    assert_bindings(
        schema="msData/modelGroups/mgO037.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO037.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o036_mg_o036_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under
    'restriction', whiche is part of a complexType
    """
    assert_bindings(
        schema="msData/modelGroups/mgO036.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO036.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o034_mg_o034_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under 'redefine',
    which is part of a complexType
    """
    assert_bindings(
        schema="msData/modelGroups/mgO034.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO034.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o031_mg_o031_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under 'choice'
    with maxOccurs=minOccurs=1 , which is part of a complexType, and group
    ref has minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgO031.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO031.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o030_mg_o030_v():
    """
    TEST :model groups (ALL) : 'all', and has minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgO030.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO030.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o029_mg_o029_v():
    """
    TEST :model groups (ALL) : 'all', appear under 'restriction', which is
    part of a complexType, and has minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgO029.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO029.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o017_mg_o017_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under 'choice'
    with maxOccurs=minOccurs=1 , whiche is part of a complexType, and
    particles in all has maxOccurs=minOccurs (absent)
    """
    assert_bindings(
        schema="msData/modelGroups/mgO017.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o016_mg_o016_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under 'sequence'
    with maxOccurs=minOccurs=1, , whiche is part of a complexType, and
    particles in all has maxOccurs=minOccurs (absent)
    """
    assert_bindings(
        schema="msData/modelGroups/mgO016.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o015_mg_o015_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under
    'restriction', whiche is part of a complexType, and particles in all
    has maxOccurs=minOccurs (absent)
    """
    assert_bindings(
        schema="msData/modelGroups/mgO015.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o011_mg_o011_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under
    'complexType', whiche is part of a complexType, and particles in all
    has maxOccurs=minOccurs (absent)
    """
    assert_bindings(
        schema="msData/modelGroups/mgO011.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o010_mg_o010_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under 'choice'
    which is part of a complexType
    """
    assert_bindings(
        schema="msData/modelGroups/mgO010.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o009_mg_o009_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under 'sequence'
    which is part of a complexType
    """
    assert_bindings(
        schema="msData/modelGroups/mgO009.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o008_mg_o008_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under
    'restriction', which is part of a complexType
    """
    assert_bindings(
        schema="msData/modelGroups/mgO008.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_o006_mg_o006_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under 'redefine',
    which is part of a complexType
    """
    assert_bindings(
        schema="msData/modelGroups/mgO006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o005_mg_o005_v():
    """
    TEST :model groups (ALL) : group' with 'all', appear under 'schema',
    which is part of a complexType and has maxOccurs=minOccurs (0 | 1)
    """
    assert_bindings(
        schema="msData/modelGroups/mgO005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o004_mg_o004_v():
    """
    TEST :model groups (ALL) : all appear under 'complexType', which is
    part of a complexType, and particles in all has maxOccurs=minOccurs (0
    | 1)
    """
    assert_bindings(
        schema="msData/modelGroups/mgO004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_o002_mg_o002_v():
    """
    TEST :model groups (ALL) : all has particle with minOccurs=maxOccur =
    1
    """
    assert_bindings(
        schema="msData/modelGroups/mgO002.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgO002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n016_mg_n016_i():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence (E1, E2)
    (F1,F2), and 2 choice (C1 | C2) (D1 | D2), in the instant XML document
    ( no element )
    """
    assert_bindings(
        schema="msData/modelGroups/mgN016.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN016.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n015_mg_n015_i():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence (E1, E2)
    (F1,F2), and 2 choice (C1 | C2) (D1 | D2), in the instant XML document
    (D1)
    """
    assert_bindings(
        schema="msData/modelGroups/mgN015.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN015.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n014_mg_n014_i():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence (E1, E2)
    (F1,F2), and 2 choice (C1 | C2) (D1 | D2), in the instant XML document
    ( C1, F1, D1)
    """
    assert_bindings(
        schema="msData/modelGroups/mgN014.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN014.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n013_mg_n013_i():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence (E1, E2)
    (F1,F2), and 2 choice (C1 | C2) (D1 | D2), in the instant XML document
    ( C1, D1)
    """
    assert_bindings(
        schema="msData/modelGroups/mgN013.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN013.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n012_mg_n012_v():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence (E1, E2)
    (F1,F2), and 2 choice (C1 | C2) (D1 | D2), in the instant XML document
    ( E1, E2, F1, F2, C1, D1)
    """
    assert_bindings(
        schema="msData/modelGroups/mgN012.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n011_mg_n011_i():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence (E1, E2)
    (F1,F2), and 2 choice (C1 | C2) (C1 | C2), in the instant XML document
    ( E1, F2, C2, D2)
    """
    assert_bindings(
        schema="msData/modelGroups/mgN011.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN011.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n010_mg_n010_i():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence as child
    (E1,E2) (F1,F2), in the instant XML document, the sequence appear as
    (F1, E1, E2, F2)
    """
    assert_bindings(
        schema="msData/modelGroups/mgN010.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN010.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n009_mg_n009_i():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence as child
    (E1,E2) (F1,F2), in the instant XML document, the sequence appear as
    (F1, F2, E1, E2)
    """
    assert_bindings(
        schema="msData/modelGroups/mgN009.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN009.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n008_mg_n008_i():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence as child
    (E1,E2) (F1,F2), in the instant XML document, the sequence appear as
    (E1, F2, F1)
    """
    assert_bindings(
        schema="msData/modelGroups/mgN008.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n007_mg_n007_i():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence as child
    (E1,E2) (F1,F2), in the instant XML document, the sequence appear as
    (E1, F1, E2, F2)
    """
    assert_bindings(
        schema="msData/modelGroups/mgN007.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN007.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n006_mg_n006_i():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence as child
    (E1,E2) (F1,F2), in the instant XML document, the sequence appear as
    (E1)
    """
    assert_bindings(
        schema="msData/modelGroups/mgN006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n005_mg_n005_v():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence as child
    (E1,E2) (F1,F2), in the instant XML document, there is no element
    specified
    """
    assert_bindings(
        schema="msData/modelGroups/mgN005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n004_mg_n004_i():
    """
    TEST :model groups (ALL) : parent is sequence, has 2 sequence as child
    ( no elements ), in the instant XML document, the sequence appear as
    (F1, E1, E2, F2)
    """
    assert_bindings(
        schema="msData/modelGroups/mgN004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN004.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n003_mg_n003_i():
    """
    TEST :model groups (ALL) : parent is sequence, the instant XML has
    element that are of same local name but different namespace URI than
    in the element decl
    """
    assert_bindings(
        schema="msData/modelGroups/mgN003.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n002_mg_n002_i():
    """
    TEST :model groups (ALL) : parent is sequence, more than one child
    sequences, each of them again have more than one sequence child node,
    instant XML doesn't conform to the declaration
    """
    assert_bindings(
        schema="msData/modelGroups/mgN002.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN002.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_n001_mg_n001_v():
    """
    TEST :model groups (ALL) : parent is sequence, more than one child
    sequences, each of them again have more than one sequence child node,
    instant XML conform to the declaration
    """
    assert_bindings(
        schema="msData/modelGroups/mgN001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgN001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m014_mg_m014_i():
    """
    TEST :model groups (ALL) : all: with 2 elements instant doc has the
    same element twice.
    """
    assert_bindings(
        schema="msData/modelGroups/mgM014.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM014.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_m013_mg_m013_v():
    """
    TEST :model groups (ALL) : all: with 2 elements instant doc has a
    global element
    """
    assert_bindings(
        schema="msData/modelGroups/mgM013.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m012_mg_m012_i():
    """
    TEST :model groups (ALL) : all: with 2 elements instant doc has an
    element that is not local or global to the declaring element
    """
    assert_bindings(
        schema="msData/modelGroups/mgM012.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM012.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m011_mg_m011_v():
    """
    TEST :model groups (ALL) : all: with 5 elements instant doc has all
    the element in reverse order
    """
    assert_bindings(
        schema="msData/modelGroups/mgM011.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m010_mg_m010_i():
    """
    TEST :model groups (ALL) : all: with 2 elements instant doc has all
    the element plus some other element from other namespace
    """
    assert_bindings(
        schema="msData/modelGroups/mgM010.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM010.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m009_mg_m009_v():
    """
    TEST :model groups (ALL) : all: with 2 elements 2 element in different
    order is in the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgM009.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m008_mg_m008_v():
    """
    TEST :model groups (ALL) : all: with 2 elements 2 element is in the
    instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgM008.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m007_mg_m007_i():
    """
    TEST :model groups (ALL) : all: with 2 elements 1 element is in the
    instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgM007.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM007.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m006_mg_m006_i():
    """
    TEST :model groups (ALL) : all: with 2 elements 0 element is in the
    instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgM006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m005_mg_m005_i():
    """
    TEST :model groups (ALL) : all: with 1 elements 2 element is in the
    instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgM005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m004_mg_m004_v():
    """
    TEST :model groups (ALL) : all: with 1 elements 1 element is in the
    instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgM004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m003_mg_m003_i():
    """
    TEST :model groups (ALL) : all: with 1 elements 0 element is in the
    instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgM003.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_m002_mg_m002_i():
    """
    TEST :model groups (ALL) : all: with no elements 1 element is in the
    instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgM002.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgM002.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_l010_mg_l010_i():
    """
    TEST :model groups (ALL) : choice: with 5 elements, an undefined
    element in the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgL010.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgL010.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_l009_mg_l009_v():
    """
    TEST :model groups (ALL) : choice: with 5 elements, 1 element in the
    instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgL009.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgL009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_l008_mg_l008_v():
    """
    TEST :model groups (ALL) : choice: with 5 elements, 0 element in the
    instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgL008.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgL008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_l007_mg_l007_i():
    """
    TEST :model groups (ALL) : choice: with 2 elements, 2 element in the
    instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgL007.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgL007.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_l006_mg_l006_v():
    """
    TEST :model groups (ALL) : choice: with 2 elements, 1 element in the
    instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgL006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgL006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_l005_mg_l005_i():
    """
    TEST :model groups (ALL) : choice: with 1 elements, 2 element is in
    the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgL005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgL005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_l004_mg_l004_v():
    """
    TEST :model groups (ALL) : choice: with 1 elements, 1 element is in
    the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgL004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgL004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_l003_mg_l003_i():
    """
    TEST :model groups (ALL) : choice: with 1 elements, 0 element is in
    the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgL003.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgL003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_l002_mg_l002_i():
    """
    TEST :model groups (ALL) : choice: with NO elements, 1 element is in
    the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgL002.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgL002.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_l001_mg_l001_v():
    """
    TEST :model groups (ALL) : choice: with NO elements (max=min=absent),
    0 element is in the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgL001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgL001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_k010_mg_k010_i():
    """
    TEST :model groups (ALL) : sequence: with 5 elements, the last 2
    elements are not in the defined order
    """
    assert_bindings(
        schema="msData/modelGroups/mgK010.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgK010.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_k009_mg_k009_v():
    """
    TEST :model groups (ALL) : sequence: with 5 elements, all elements
    appeared and are in defined order
    """
    assert_bindings(
        schema="msData/modelGroups/mgK009.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgK009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_k008_mg_k008_i():
    """
    TEST :model groups (ALL) : sequence: with 2 elements, 3 elements is
    specified in the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgK008.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgK008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_k007_mg_k007_i():
    """
    TEST :model groups (ALL) : sequence: with 2 elements, the elements are
    not in the defined order
    """
    assert_bindings(
        schema="msData/modelGroups/mgK007.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgK007.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_k006_mg_k006_i():
    """
    TEST :model groups (ALL) : sequence: with 2 elements, only the 1st
    element is specified in the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgK006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgK006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_k005_mg_k005_i():
    """
    TEST :model groups (ALL) : sequence: with 1 elements, 2 element is in
    the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgK005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgK005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_k004_mg_k004_v():
    """
    TEST :model groups (ALL) : sequence: with 1 elements, 1 element is in
    the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgK004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgK004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_k003_mg_k003_i():
    """
    TEST :model groups (ALL) : sequence: with 1 elements, 0 element is in
    the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgK003.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgK003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_k002_mg_k002_i():
    """
    TEST :model groups (ALL) : sequence: with NO elements, 1 element is in
    the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgK002.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgK002.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_k001_mg_k001_v():
    """
    TEST :model groups (ALL) : sequence: with NO elements
    (max=min=absent), 0 element is in the instant XML doc
    """
    assert_bindings(
        schema="msData/modelGroups/mgK001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgK001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j026_mg_j026_v():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=3,
    maxOccurs=unbounded
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ026.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ026.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j024_mg_j024_i():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=3,
    minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ024.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ024.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j023_mg_j023_v():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=2,
    minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ023.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ023.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j022_mg_j022_v():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=1,
    minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ022.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ022.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j021_mg_j021_i():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=0,
    minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ021.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ021.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j020_mg_j020_i():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=2,
    minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ020.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ020.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j019_mg_j019_v():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=1,
    minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ019.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ019.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j018_mg_j018_i():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=0,
    minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ018.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ018.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j017_mg_j017_i():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=2,
    minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ017.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ017.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j016_mg_j016_v():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=1,
    minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ016.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j015_mg_j015_i():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=0,
    minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ015.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ015.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j014_mg_j014_v():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=0,
    minOccurs=0, maxOccurs=999999999
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ014.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j013_mg_j013_i():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=1,
    minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ013.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ013.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j012_mg_j012_v():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=0,
    minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ012.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j011_mg_j011_i():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=2,
    minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ011.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ011.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j010_mg_j010_v():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=1,
    minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ010.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j009_mg_j009_v():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=0,
    minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ009.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j008_mg_j008_i():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=2,
    minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ008.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j007_mg_j007_v():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=1,
    minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ007.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j006_mg_j006_v():
    """
    TEST :model groups (ALL) : choice: elements in instant XML=0,
    minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j005_mg_j005_i():
    """
    TEST :model groups (ALL) : choice: check that maxOccurs default is 1,
    elements in instant XML = 2, minOccurs=absent, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j004_mg_j004_v():
    """
    TEST :model groups (ALL) : choice: check that minOccurs default is 1,
    elements in instant XML = 1, minOccurs=absent, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_j003_mg_j003_i():
    """
    TEST :model groups (ALL) : choice: check that minOccurs default is 1,
    elements in instant XML = 0, minOccurs=absent, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgJ003.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgJ003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_i019_mg_i019_v():
    """
    TEST :model groups (ALL) : choice: with children 4 any, 4 elements
    """
    assert_bindings(
        schema="msData/modelGroups/mgI019.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI019.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_i018_mg_i018_v():
    """
    TEST :model groups (ALL) : choice: with children 4 sequence, 4 any
    """
    assert_bindings(
        schema="msData/modelGroups/mgI018.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_i017_mg_i017_v():
    """
    TEST :model groups (ALL) : choice: with children 4 choice, 4 sequence
    """
    assert_bindings(
        schema="msData/modelGroups/mgI017.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_i016_mg_i016_v():
    """
    TEST :model groups (ALL) : choice: with children 4 groups, 4 choice
    """
    assert_bindings(
        schema="msData/modelGroups/mgI016.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_i015_mg_i015_v():
    """
    TEST :model groups (ALL) : choice: with children 4 elements, 4 groups
    """
    assert_bindings(
        schema="msData/modelGroups/mgI015.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_i014_mg_i014_v():
    """
    TEST :model groups (ALL) : choice: with children any, sequence, group,
    element, choice
    """
    assert_bindings(
        schema="msData/modelGroups/mgI014.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_i013_mg_i013_v():
    """
    TEST :model groups (ALL) : choice: with children sequence, group,
    choice, element, any
    """
    assert_bindings(
        schema="msData/modelGroups/mgI013.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_i012_mg_i012_v():
    """
    TEST :model groups (ALL) : choice: with children choice, any, group,
    sequence, element
    """
    assert_bindings(
        schema="msData/modelGroups/mgI012.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_i011_mg_i011_v():
    """
    TEST :model groups (ALL) : choice: with children group, any, choice,
    element, sequence
    """
    assert_bindings(
        schema="msData/modelGroups/mgI011.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_i010_mg_i010_v():
    """
    TEST :model groups (ALL) : choice: with children element, any,
    sequence, choice, group
    """
    assert_bindings(
        schema="msData/modelGroups/mgI010.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_i009_mg_i009_v():
    """
    TEST :model groups (ALL) : choice: with children annotation, element,
    group, choice, sequence, any
    """
    assert_bindings(
        schema="msData/modelGroups/mgI009.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_i008_mg_i008_v():
    """
    TEST :model groups (ALL) : choice: with children annotation, any
    """
    assert_bindings(
        schema="msData/modelGroups/mgI008.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_i007_mg_i007_v():
    """
    TEST :model groups (ALL) : choice: with children annotation, sequence
    """
    assert_bindings(
        schema="msData/modelGroups/mgI007.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_i006_mg_i006_v():
    """
    TEST :model groups (ALL) : choice: with children annotation, choice
    """
    assert_bindings(
        schema="msData/modelGroups/mgI006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_i005_mg_i005_v():
    """
    TEST :model groups (ALL) : choice: with children annotation, group
    """
    assert_bindings(
        schema="msData/modelGroups/mgI005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_i004_mg_i004_v():
    """
    TEST :model groups (ALL) : choice: with children annotation, element
    """
    assert_bindings(
        schema="msData/modelGroups/mgI004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_i002_mg_i002_v():
    """
    TEST :model groups (ALL) : choice: with one annotation only
    """
    assert_bindings(
        schema="msData/modelGroups/mgI002.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI002.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_i001_mg_i001_v():
    """
    TEST :model groups (ALL) : choice: with no child node
    """
    assert_bindings(
        schema="msData/modelGroups/mgI001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgI001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_hb005_mg_hb005_v():
    """
    TEST :model groups (ALL) : choice: maxOccurs = 5
    """
    assert_bindings(
        schema="msData/modelGroups/mgHb005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgHb005.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_hb004_mg_hb004_v():
    """
    TEST :model groups (ALL) : choice: maxOccurs = unbounded
    """
    assert_bindings(
        schema="msData/modelGroups/mgHb004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgHb004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_h018_mg_h018_v():
    """
    TEST :model groups (ALL) : choice: with parent sequence
    """
    assert_bindings(
        schema="msData/modelGroups/mgH018.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgH018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_h017_mg_h017_v():
    """
    TEST :model groups (ALL) : choice: with parent choice
    """
    assert_bindings(
        schema="msData/modelGroups/mgH017.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgH017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_h016_mg_h016_v():
    """
    TEST :model groups (ALL) : choice: with parent group
    """
    assert_bindings(
        schema="msData/modelGroups/mgH016.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgH016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_h015_mg_h015_v():
    """
    TEST :model groups (ALL) : choice: with parent extension
    """
    assert_bindings(
        schema="msData/modelGroups/mgH015.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgH015.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_h014_mg_h014_v():
    """
    TEST :model groups (ALL) : choice: with parent restriction
    """
    assert_bindings(
        schema="msData/modelGroups/mgH014.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgH014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_h013_mg_h013_v():
    """
    TEST :model groups (ALL) : choice: with parent complexType
    """
    assert_bindings(
        schema="msData/modelGroups/mgH013.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgH013.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_h001_mg_h001_v():
    """
    TEST :model groups (ALL) : choice: id, id="foo"
    """
    assert_bindings(
        schema="msData/modelGroups/mgH001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgH001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g026_mg_g026_v():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=3,
    maxOccurs=unbounded
    """
    assert_bindings(
        schema="msData/modelGroups/mgG026.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG026.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g024_mg_g024_i():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=3,
    minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/modelGroups/mgG024.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG024.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g023_mg_g023_v():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=2,
    minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/modelGroups/mgG023.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG023.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g022_mg_g022_v():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=1,
    minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/modelGroups/mgG022.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG022.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g021_mg_g021_i():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=0,
    minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/modelGroups/mgG021.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG021.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g020_mg_g020_i():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=2,
    minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgG020.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG020.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g019_mg_g019_v():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=1,
    minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgG019.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG019.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g018_mg_g018_i():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=0,
    minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgG018.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG018.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g017_mg_g017_i():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=2,
    minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgG017.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG017.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g016_mg_g016_v():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=1,
    minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgG016.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g015_mg_g015_i():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=0,
    minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgG015.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG015.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g014_mg_g014_v():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=0,
    minOccurs=0, maxOccurs=999999999
    """
    assert_bindings(
        schema="msData/modelGroups/mgG014.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g013_mg_g013_i():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=1,
    minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/modelGroups/mgG013.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG013.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g012_mg_g012_v():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=0,
    minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/modelGroups/mgG012.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g011_mg_g011_i():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=2,
    minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgG011.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG011.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g010_mg_g010_v():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=1,
    minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgG010.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g009_mg_g009_v():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=0,
    minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgG009.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g008_mg_g008_i():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=2,
    minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgG008.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g007_mg_g007_v():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=1,
    minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgG007.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g006_mg_g006_v():
    """
    TEST :model groups (ALL) : sequence: elements in instant XML=0,
    minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgG006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g005_mg_g005_i():
    """
    TEST :model groups (ALL) : sequence: check that maxOccurs default is
    1, elements in instant XML = 2, minOccurs=absent, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgG005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g004_mg_g004_v():
    """
    TEST :model groups (ALL) : sequence: check that minOccurs default is
    1, elements in instant XML = 1, minOccurs=absent, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgG004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_g003_mg_g003_i():
    """
    TEST :model groups (ALL) : sequence: check that minOccurs default is
    1, elements in instant XML = 0, minOccurs=absent, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgG003.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgG003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_f019_mg_f019_v():
    """
    TEST :model groups (ALL) : sequence: with children 4 any, 4 elements
    """
    assert_bindings(
        schema="msData/modelGroups/mgF019.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF019.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_f018_mg_f018_v():
    """
    TEST :model groups (ALL) : sequence: with children 4 sequence, 4 any
    """
    assert_bindings(
        schema="msData/modelGroups/mgF018.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_f017_mg_f017_v():
    """
    TEST :model groups (ALL) : sequence: with children 4 choice, 4
    sequence
    """
    assert_bindings(
        schema="msData/modelGroups/mgF017.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_f016_mg_f016_v():
    """
    TEST :model groups (ALL) : sequence: with children 4 groups, 4 choice
    """
    assert_bindings(
        schema="msData/modelGroups/mgF016.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_f015_mg_f015_v():
    """
    TEST :model groups (ALL) : sequence: with children 4 elements, 4
    groups
    """
    assert_bindings(
        schema="msData/modelGroups/mgF015.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_f014_mg_f014_v():
    """
    TEST :model groups (ALL) : sequence: with children any, sequence,
    group, element, choice
    """
    assert_bindings(
        schema="msData/modelGroups/mgF014.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_f013_mg_f013_v():
    """
    TEST :model groups (ALL) : sequence: with children sequence, group,
    choice, element, any
    """
    assert_bindings(
        schema="msData/modelGroups/mgF013.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_f012_mg_f012_v():
    """
    TEST :model groups (ALL) : sequence: with children choice, any, group,
    sequence, element
    """
    assert_bindings(
        schema="msData/modelGroups/mgF012.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_f011_mg_f011_v():
    """
    TEST :model groups (ALL) : sequence: with children group, any, choice,
    element, sequence
    """
    assert_bindings(
        schema="msData/modelGroups/mgF011.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_f010_mg_f010_v():
    """
    TEST :model groups (ALL) : sequence: with children element, any,
    sequence, choice, group
    """
    assert_bindings(
        schema="msData/modelGroups/mgF010.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_f009_mg_f009_v():
    """
    TEST :model groups (ALL) : sequence: with children annotation,
    element, group, choice, sequence, any
    """
    assert_bindings(
        schema="msData/modelGroups/mgF009.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_f008_mg_f008_v():
    """
    TEST :model groups (ALL) : sequence: with children annotation, any
    """
    assert_bindings(
        schema="msData/modelGroups/mgF008.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_f007_mg_f007_v():
    """
    TEST :model groups (ALL) : sequence: with children annotation,
    sequence
    """
    assert_bindings(
        schema="msData/modelGroups/mgF007.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_f006_mg_f006_v():
    """
    TEST :model groups (ALL) : sequence: with children annotation, choice
    """
    assert_bindings(
        schema="msData/modelGroups/mgF006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_f005_mg_f005_v():
    """
    TEST :model groups (ALL) : sequence: with children annotation, group
    """
    assert_bindings(
        schema="msData/modelGroups/mgF005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_f004_mg_f004_v():
    """
    TEST :model groups (ALL) : sequence: with children annotation, element
    """
    assert_bindings(
        schema="msData/modelGroups/mgF004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_f002_mg_f002_v():
    """
    TEST :model groups (ALL) : sequence: with one annotation only
    """
    assert_bindings(
        schema="msData/modelGroups/mgF002.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_f001_mg_f001_v():
    """
    TEST :model groups (ALL) : sequence: with no child node
    """
    assert_bindings(
        schema="msData/modelGroups/mgF001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgF001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_eb005_mg_eb005_v():
    """
    TEST :model groups (ALL) : sequence: maxOccurs = 8
    """
    assert_bindings(
        schema="msData/modelGroups/mgEb005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgEb005.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_eb004_mg_eb004_v():
    """
    TEST :model groups (ALL) : sequence: maxOccurs = unbounded
    """
    assert_bindings(
        schema="msData/modelGroups/mgEb004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgEb004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_e018_mg_e018_v():
    """
    TEST :model groups (ALL) : sequence: with parent sequence
    """
    assert_bindings(
        schema="msData/modelGroups/mgE018.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgE018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_e017_mg_e017_v():
    """
    TEST :model groups (ALL) : sequence: with parent choice
    """
    assert_bindings(
        schema="msData/modelGroups/mgE017.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgE017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_e016_mg_e016_v():
    """
    TEST :model groups (ALL) : sequence: with parent group
    """
    assert_bindings(
        schema="msData/modelGroups/mgE016.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgE016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_e015_mg_e015_v():
    """
    TEST :model groups (ALL) : sequence: with parent extension
    """
    assert_bindings(
        schema="msData/modelGroups/mgE015.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgE015.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_e014_mg_e014_v():
    """
    TEST :model groups (ALL) : sequence: with parent restriction
    """
    assert_bindings(
        schema="msData/modelGroups/mgE014.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgE014.xml",
        instance_is_valid=True,
        class_name="Who",
        version="1.0",
    )


def test_mg_e013_mg_e013_v():
    """
    TEST :model groups (ALL) : sequence: with parent complexType
    """
    assert_bindings(
        schema="msData/modelGroups/mgE013.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgE013.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_e001_mg_e001_v():
    """
    TEST :model groups (ALL) : sequence: id, id="foo"
    """
    assert_bindings(
        schema="msData/modelGroups/mgE001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgE001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_d013_mg_d013_v():
    """
    TEST :model groups (ALL) : test using of minOccurs=0 and allowing
    elements to not exists
    """
    assert_bindings(
        schema="msData/modelGroups/mgD013.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgD013.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_d009_mg_d009_v():
    """
    TEST :model groups (ALL) : choice: with any attribute with no schema
    namespace
    """
    assert_bindings(
        schema="msData/modelGroups/mgD009.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgD009.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_d005_mg_d005_v():
    """
    TEST :model groups (ALL) : sequence: with any attribute with no schema
    namespace
    """
    assert_bindings(
        schema="msData/modelGroups/mgD005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgD005.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_d001_mg_d001_v():
    """
    TEST :model groups (ALL) : all: with any attribute with no schema
    namespace
    """
    assert_bindings(
        schema="msData/modelGroups/mgD001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgD001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_mg_c014_mg_c014_v():
    """
    TEST :model groups (ALL) : all with default minOccurs and maxOccurs
    with optional element children
    """
    assert_bindings(
        schema="msData/modelGroups/mgC014.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgC014.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_c012_mg_c012_i():
    """
    TEST :model groups (ALL) : all: elements in instant XML=2,
    minOccurs=absent, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgC012.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgC012.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_c011_mg_c011_v():
    """
    TEST :model groups (ALL) : all: elements in instant XML=1,
    minOccurs=absent, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgC011.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgC011.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_c010_mg_c010_i():
    """
    TEST :model groups (ALL) : all: elements in instant XML=0,
    minOccurs=absent, maxOccurs=1
    """
    assert_bindings(
        schema="msData/modelGroups/mgC010.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgC010.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_c007_mg_c007_i():
    """
    TEST :model groups (ALL) : all: elements in instant XML=2,
    minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgC007.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgC007.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_c006_mg_c006_v():
    """
    TEST :model groups (ALL) : all: elements in instant XML=1,
    minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgC006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgC006.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_c005_mg_c005_i():
    """
    TEST :model groups (ALL) : all: elements in instant XML=0,
    minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgC005.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgC005.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_mg_c004_mg_c004_v():
    """
    TEST :model groups (ALL) : all: minOccurs can have value of 0 or 1 max
    occurs can only have 1 as value, minOccurs=0, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgC004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgC004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_c003_mg_c003_i():
    """
    TEST :model groups (ALL) : all: check that maxOccurs default is 1,
    elements in instant XML = 2, minOccurs=absent, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgC003.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgC003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_c002_mg_c002_v():
    """
    TEST :model groups (ALL) : all: check that minOccurs default is 1,
    elements in instant XML = 1, minOccurs=absent, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgC002.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgC002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_c001_mg_c001_i():
    """
    TEST :model groups (ALL) : all: check that minOccurs default is 1,
    elements in instant XML = 0, minOccurs=absent, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/modelGroups/mgC001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgC001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_mg_b006_mg_b006_v():
    """
    TEST :model groups (ALL) : all: with one element only
    """
    assert_bindings(
        schema="msData/modelGroups/mgB006.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgB006.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_b004_mg_b004_v():
    """
    TEST :model groups (ALL) : all: with annotation follow by 1 element
    """
    assert_bindings(
        schema="msData/modelGroups/mgB004.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgB004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_b002_mg_b002_v():
    """
    TEST :model groups (ALL) : all: with one annotation only
    """
    assert_bindings(
        schema="msData/modelGroups/mgB002.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgB002.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_b001_mg_b001_v():
    """
    TEST :model groups (ALL) : all: with no child node
    """
    assert_bindings(
        schema="msData/modelGroups/mgB001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgB001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_aa003_mg_aa003_v():
    """
    TEST :model groups (ALL) : all: minOccurs = 0
    """
    assert_bindings(
        schema="msData/modelGroups/mgAa003.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgAa003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_a017_mg_a017_v():
    """
    TEST :model groups (ALL) : all: with parent group
    """
    assert_bindings(
        schema="msData/modelGroups/mgA017.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgA017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_mg_a015_mg_a015_v():
    """
    TEST :model groups (ALL) : all: with parent restriction
    """
    assert_bindings(
        schema="msData/modelGroups/mgA015.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgA015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_mg_a014_mg_a014_v():
    """
    TEST :model groups (ALL) : all: with parent complexType
    """
    assert_bindings(
        schema="msData/modelGroups/mgA014.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgA014.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_mg_a001_mg_a001_v():
    """
    TEST :model groups (ALL) : all: id, id="foo"
    """
    assert_bindings(
        schema="msData/modelGroups/mgA001.xsd",
        is_valid=True,
        instance="msData/modelGroups/mgA001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_notat_h003_notat_h003_i():
    """
    TEST :Notations : Instance document with (Schema with 3 Notations and
    an attribute with type=NOTATION) and attribute contains two notation
    names
    """
    assert_bindings(
        schema="msData/notations/notatH003.xsd",
        is_valid=True,
        instance="msData/notations/notatH003.xml",
        instance_is_valid=False,
        class_name="Foo",
        version="1.0",
    )


@pytest.mark.xfail
def test_notat_h002v_notat_h002v_i():
    """
    TEST :Notations : Instance document doesn't declare a notation type
    """
    assert_bindings(
        schema="msData/notations/notatH002.xsd",
        is_valid=True,
        instance="msData/notations/notatH002.xml",
        instance_is_valid=False,
        class_name="Foo",
        version="1.0",
    )


@pytest.mark.xfail
def test_notat_h001v_notat_h001v_v():
    """
    TEST :Notations : Instance document declares a notation type
    """
    assert_bindings(
        schema="msData/notations/notatH001.xsd",
        is_valid=True,
        instance="msData/notations/notatH001.xml",
        instance_is_valid=True,
        class_name="Foo",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_z040_particles_z040_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : XSD: validation on a sequence involving an
    optional wildcard
    """
    assert_bindings(
        schema="msData/particles/particlesZ040.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ040.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_z036_c_particles_z036_c_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Schema validation engine validates as xs:any if
    maxOccurs greater than 4096(15) TSTF concluded no change required to
    instance test here The validity of these schemas was never in doubt,
    prior 'queried' status was in error
    """
    assert_bindings(
        schema="msData/particles/particlesZ036_c.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ036_c.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_z036_b2_particles_z036_b2_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Schema validation engine validates as xs:any if
    maxOccurs greater than 4096(15) TSTF concluded the instances are OK
    The validity of these schemas was never in doubt, prior 'queried'
    status was in error
    """
    assert_bindings(
        schema="msData/particles/particlesZ036_b.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ036_b2.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_z036_b1_particles_z036_b1_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Schema validation engine validates as xs:any if
    maxOccurs greater than 4096(14) TSTF concluded the instances are OK
    The validity of these schemas was never in doubt, prior 'queried'
    status was in error
    """
    assert_bindings(
        schema="msData/particles/particlesZ036_b.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ036_b1.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_z036_a_particles_z036_a_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Schema validation engine validates as xs:any if
    maxOccurs greater than 4096(13) TSTF concluded no change required to
    instance test here The validity of these schemas was never in doubt,
    prior 'queried' status was in error
    """
    assert_bindings(
        schema="msData/particles/particlesZ036_a.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ036_a.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_z035_a_particles_z035_a_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Schema validation engine validates as xs:any if
    maxOccurs greater than 4096(12)
    """
    assert_bindings(
        schema="msData/particles/particlesZ035_a.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ035_a.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_z034_b_particles_z034_b_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Schema validation engine validates as xs:any if
    maxOccurs greater than 4096(11)
    """
    assert_bindings(
        schema="msData/particles/particlesZ034_b.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ034_b1.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_z034_a3_particles_z034_a3_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Schema validation engine validates as xs:any if
    maxOccurs greater than 4096(10)
    """
    assert_bindings(
        schema="msData/particles/particlesZ034_a.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ034_a3.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_z034_a2_particles_z034_a2_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Schema validation engine validates as xs:any if
    maxOccurs greater than 4096(9)
    """
    assert_bindings(
        schema="msData/particles/particlesZ034_a.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ034_a2.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_z034_a1_particles_z034_a1_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Schema validation engine validates as xs:any if
    maxOccurs greater than 4096(8)
    """
    assert_bindings(
        schema="msData/particles/particlesZ034_a.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ034_a1.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_z026_particles_z026_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Substitution across namespaces(2) TSTF concluded
    the schema's validity was implementation-determined, WG must decide
    what to do with this test
    """
    assert_bindings(
        schema="msData/particles/particlesZ026a.xsd",
        is_valid=False,
        instance="msData/particles/particlesZ026.xml",
        instance_is_valid=False,
        class_name="Sequence",
        version="1.0",
    )


def test_particles_z025_particles_z025_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Substitution across namespaces
    """
    assert_bindings(
        schema="",
        is_valid=False,
        instance="msData/particles/particlesZ025.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_particles_z016_particles_z016_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : id="86932" description="We should proceed to
    validate XML instance even if the schema compilation throws a warning"
    """
    assert_bindings(
        schema="msData/particles/particlesZ016.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ016.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_particles_z015_particles_z015_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : id="86379" description="xsd: derived attribute's
    type should validly derived from base attribute's type."
    """
    assert_bindings(
        schema="msData/particles/particlesZ015.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ015.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_z012_particles_z012_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : id="86379" description="xsd: derived attribute's
    type should validly derived from base attribute's type."
    """
    assert_bindings(
        schema="msData/particles/particlesZ012.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ012.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_particles_z008_particles_z008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Restriction of abstract classes with abstract
    particles via substitution group should be valid.
    """
    assert_bindings(
        schema="msData/particles/particlesZ008.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ008.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_particles_z007_particles_z007_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : xsd: test valid value in instance XML, whose xsd
    type derived by restriction from union.
    """
    assert_bindings(
        schema="msData/particles/particlesZ007.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ007.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_particles_z005_particles_z005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : xsd: test valid value in instance XML, whose xsd
    type derived by restriction from union.
    """
    assert_bindings(
        schema="msData/particles/particlesZ005.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ005.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_z003_particles_z003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : xsd: should allow and recognize declaration of
    namespace URI in local level as well as root level.
    """
    assert_bindings(
        schema="msData/particles/particlesZ003.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_z002_particles_z002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Schema Component Constraint: Derivation Valid
    (Restriction, Complex) rules in regard to attribute uses
    """
    assert_bindings(
        schema="msData/particles/particlesZ002.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_z001_particles_z001_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Schema Component Constraint: Particle Derivation
    OK (Elt:All/Choice/Sequence -- RecurseAsIfGroup) rule is ambiguous
    Invalid restriction which becomes valid in XSD 1.1 - MHK
    """
    assert_bindings(
        schema="msData/particles/particlesZ001.xsd",
        is_valid=True,
        instance="msData/particles/particlesZ001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_w016_particles_w016_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Sequence -
    Recurse) (Sequence) R drived by restriction from (Sequence) B : B has
    (a, b), R has (a) is a valid restriction of the 'a' in B
    """
    assert_bindings(
        schema="msData/particles/particlesW016.xsd",
        is_valid=True,
        instance="msData/particles/particlesW016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_w011_particles_w011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Sequence -
    Recurse) (Sequence) R drived by restriction from (Sequence) B : B has
    (a, b, c), R has (a, b, c)
    """
    assert_bindings(
        schema="msData/particles/particlesW011.xsd",
        is_valid=True,
        instance="msData/particles/particlesW011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_w008_particles_w008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Sequence -
    Recurse) (Sequence) R drived by restriction from (Sequence) B : B has
    (a, b, c), b and c are emptiable, R has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesW008.xsd",
        is_valid=True,
        instance="msData/particles/particlesW008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_w003_particles_w003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Sequence -
    Recurse) (Sequence) R drived by restriction from (Sequence) B : B's
    min,maxOccuranceRange=(3, 9), R's min,maxOccuranceRange=(4, 8)
    """
    assert_bindings(
        schema="msData/particles/particlesW003.xsd",
        is_valid=True,
        instance="msData/particles/particlesW003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_w001_particles_w001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Sequence -
    Recurse) (Sequence) R drived by restriction from (Sequence) B : B's
    minOccuranceRange=6, R's minOccuranceRange=6
    """
    assert_bindings(
        schema="msData/particles/particlesW001.xsd",
        is_valid=True,
        instance="msData/particles/particlesW001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_v015_particles_v015_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B has
    (a | b | c), R has (c, b, a)
    """
    assert_bindings(
        schema="msData/particles/particlesV015.xsd",
        is_valid=True,
        instance="msData/particles/particlesV015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_v014_particles_v014_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B has
    (a | b | c), R has (a, c)
    """
    assert_bindings(
        schema="msData/particles/particlesV014.xsd",
        is_valid=True,
        instance="msData/particles/particlesV014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_v013_particles_v013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B has
    (a | b | c), R has (b, c)
    """
    assert_bindings(
        schema="msData/particles/particlesV013.xsd",
        is_valid=True,
        instance="msData/particles/particlesV013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_v012_particles_v012_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B has
    (a | b | c), R has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesV012.xsd",
        is_valid=True,
        instance="msData/particles/particlesV012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_v011_particles_v011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B has
    (a | b | c), R has ( c)
    """
    assert_bindings(
        schema="msData/particles/particlesV011.xsd",
        is_valid=True,
        instance="msData/particles/particlesV011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_v010_particles_v010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B has
    (a | b | c), R has (b)
    """
    assert_bindings(
        schema="msData/particles/particlesV010.xsd",
        is_valid=True,
        instance="msData/particles/particlesV010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_v009_particles_v009_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B has
    (a | b | c), R has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesV009.xsd",
        is_valid=True,
        instance="msData/particles/particlesV009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_v008_particles_v008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B has
    (a | b), R has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesV008.xsd",
        is_valid=True,
        instance="msData/particles/particlesV008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_v007_particles_v007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B has
    (a | b), R has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesV007.xsd",
        is_valid=True,
        instance="msData/particles/particlesV007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_v006_particles_v006_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B's
    min,maxOccuranceRange=(0,0), R's min,maxOccuranceRange=(0,0)
    """
    assert_bindings(
        schema="msData/particles/particlesV006.xsd",
        is_valid=True,
        instance="msData/particles/particlesV006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_v004_particles_v004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B's
    maxOccuranceRange=6, R's maxOccuranceRange=6
    """
    assert_bindings(
        schema="msData/particles/particlesV004.xsd",
        is_valid=True,
        instance="msData/particles/particlesV004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_v003_particles_v003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Choice -
    MapAndSum) (Sequence) R drived by restriction from (Choice) B : B's
    min,maxOccuranceRange=(3, 9), R's min,maxOccuranceRange=(4, 8)
    """
    assert_bindings(
        schema="msData/particles/particlesV003.xsd",
        is_valid=True,
        instance="msData/particles/particlesV003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_u007_particles_u007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:All -
    RecurseUnordered) (Sequence) R drived by restriction from (All) B : B
    has (a, b, c, d), R has (d,b,c,a)
    """
    assert_bindings(
        schema="msData/particles/particlesU007.xsd",
        is_valid=True,
        instance="msData/particles/particlesU007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_u005_particles_u005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:All -
    RecurseUnordered) (Sequence) R drived by restriction from (All) B : B
    has (a, b, c), c is emptiable, R has ( a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesU005.xsd",
        is_valid=True,
        instance="msData/particles/particlesU005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_u004_particles_u004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:All -
    RecurseUnordered) (Sequence) R drived by restriction from (All) B : B
    has (a, b, c), c is emptiable, R has (b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesU004.xsd",
        is_valid=True,
        instance="msData/particles/particlesU004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_u003_particles_u003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:All -
    RecurseUnordered) (Sequence) R drived by restriction from (All) B : B
    has (a, b), R has (b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesU003.xsd",
        is_valid=True,
        instance="msData/particles/particlesU003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q032_particles_q032_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's namespace=##targetNamespace, foo, bar, R has an elements
    from targetNamespace, and foo
    """
    assert_bindings(
        schema="msData/particles/particlesQ032.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ032.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q030_particles_q030_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's namespace=foo, bar', R has an element from foo and bar
    """
    assert_bindings(
        schema="msData/particles/particlesQ030.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ030.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q029_particles_q029_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's namespace=foo, bar', R has an element from foo
    """
    assert_bindings(
        schema="msData/particles/particlesQ029.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ029.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q024_particles_q024_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's namespace=##targetNamespace, R has an element
    targetNamespace
    """
    assert_bindings(
        schema="msData/particles/particlesQ024.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ024.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q022_particles_q022_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's namespace=##local, R has an element from no namespace
    """
    assert_bindings(
        schema="msData/particles/particlesQ022.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ022.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q020_particles_q020_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's namespace=##other, R has an element from foo
    """
    assert_bindings(
        schema="msData/particles/particlesQ020.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ020.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q017_particles_q017_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's namespace=##any, R has an element from namespace foo
    """
    assert_bindings(
        schema="msData/particles/particlesQ017.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q016_particles_q016_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's namespace=##any, R has an element from no namespace
    """
    assert_bindings(
        schema="msData/particles/particlesQ016.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q013_particles_q013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's minOccurs=4, B's maxOccurs=4, R has 2 groups, each has
    one child with minOccurs as 2
    """
    assert_bindings(
        schema="msData/particles/particlesQ013.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q011_particles_q011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's minOccurs=0, B's maxOccurs=4, R has 2 groups, each has
    one child with maxOccurs as 2
    """
    assert_bindings(
        schema="msData/particles/particlesQ011.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q007_particles_q007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's minOccurs=0, B's maxOccurs=4, R has 2 elements, each
    with maxOccurs as 2
    """
    assert_bindings(
        schema="msData/particles/particlesQ007.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q005_particles_q005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's minOccurs=0, B's maxOccurs=unbounded, R's maxOccurs =
    1000, R has element with maxOccurs unbounded
    """
    assert_bindings(
        schema="msData/particles/particlesQ005.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q004_particles_q004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's minOccurs=0, B's maxOccurs=6, R has an element with
    minOccurs=1, maxOccurs=6
    """
    assert_bindings(
        schema="msData/particles/particlesQ004.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q003_particles_q003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's minOccurs=0, B's maxOccurs=6, R's minOccurs=1, R's
    maxOccurs=6
    """
    assert_bindings(
        schema="msData/particles/particlesQ003.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q002_particles_q002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's minOccurs=1, B's maxOccurs=1, R's minOccurs=1, R's
    maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesQ002.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_q001_particles_q001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Sequence:Any -
    NSRecurseCheckCardinality) (Sequence) R drived by restriction from
    (any) B : B's minOccurs=0, B's maxOccurs=1, R's minOccurs=1, R's
    maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesQ001.xsd",
        is_valid=True,
        instance="msData/particles/particlesQ001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_t014_particles_t014_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Choice -
    RecurseLax) (Choice) R drived by restriction from (All) B : B's
    maxOccurs=unbounded, R's maxOccurs = 3 (a | b | c) all with maxOccurs
    ( 0 and 10 and 100 )
    """
    assert_bindings(
        schema="msData/particles/particlesT014.xsd",
        is_valid=True,
        instance="msData/particles/particlesT014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_t013_particles_t013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Choice -
    RecurseLax) (Choice) R drived by restriction from (All) B : B's
    maxOccurs=unbounded, R's maxOccurs=unbounded
    """
    assert_bindings(
        schema="msData/particles/particlesT013.xsd",
        is_valid=True,
        instance="msData/particles/particlesT013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_t012_particles_t012_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Choice -
    RecurseLax) (Choice) R drived by restriction from (All) B : B's
    maxOccurs=unbounded, R's maxOccurs=1, but has (a | b | c) all with
    maxOccurs=unbounded
    """
    assert_bindings(
        schema="msData/particles/particlesT012.xsd",
        is_valid=True,
        instance="msData/particles/particlesT012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_t007_particles_t007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Choice -
    RecurseLax) (Choice) R drived by restriction from (All) B : B has (a |
    b | c), R has (a | b | c)
    """
    assert_bindings(
        schema="msData/particles/particlesT007.xsd",
        is_valid=True,
        instance="msData/particles/particlesT007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_t006_particles_t006_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Choice -
    RecurseLax) (Choice) R drived by restriction from (All) B : B has (a |
    b | c), c is NOT emptiable, R has (a | b)
    """
    assert_bindings(
        schema="msData/particles/particlesT006.xsd",
        is_valid=True,
        instance="msData/particles/particlesT006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_t005_particles_t005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Choice -
    RecurseLax) (Choice) R drived by restriction from (All) B : B has (a |
    b | c), b is but c is NOT emptiable, R has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesT005.xsd",
        is_valid=True,
        instance="msData/particles/particlesT005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_t004_particles_t004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Choice -
    RecurseLax) (Choice) R drived by restriction from (All) B : B has (a |
    b | c), c is emptiable, R has (a | b) c is emptiable
    """
    assert_bindings(
        schema="msData/particles/particlesT004.xsd",
        is_valid=True,
        instance="msData/particles/particlesT004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_t003_particles_t003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Choice -
    RecurseLax) (Choice) R drived by restriction from (All) B : B has (a |
    b | c), b and c are emptiable, R has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesT003.xsd",
        is_valid=True,
        instance="msData/particles/particlesT003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_t001_particles_t001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Choice -
    RecurseLax) (Choice) R drived by restriction from (All) B : B has (a |
    b), R has (a | b)
    """
    assert_bindings(
        schema="msData/particles/particlesT001.xsd",
        is_valid=True,
        instance="msData/particles/particlesT001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r030_particles_r030_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's namespace=foo, bar', R has an element from bar
    """
    assert_bindings(
        schema="msData/particles/particlesR030.xsd",
        is_valid=True,
        instance="msData/particles/particlesR030.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r029_particles_r029_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's namespace=foo, bar', R has an element from foo
    """
    assert_bindings(
        schema="msData/particles/particlesR029.xsd",
        is_valid=True,
        instance="msData/particles/particlesR029.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r024_particles_r024_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's namespace=##targetNamespace, R has an element
    targetNamespace
    """
    assert_bindings(
        schema="msData/particles/particlesR024.xsd",
        is_valid=True,
        instance="msData/particles/particlesR024.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r022_particles_r022_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's namespace=##local, R has an element from no namespace
    """
    assert_bindings(
        schema="msData/particles/particlesR022.xsd",
        is_valid=True,
        instance="msData/particles/particlesR022.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r020_particles_r020_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's namespace=##other, R has an element from foo
    """
    assert_bindings(
        schema="msData/particles/particlesR020.xsd",
        is_valid=True,
        instance="msData/particles/particlesR020.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r017_particles_r017_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's namespace=##any, R has an element from foo
    """
    assert_bindings(
        schema="msData/particles/particlesR017.xsd",
        is_valid=True,
        instance="msData/particles/particlesR017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r016_particles_r016_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's namespace=##any, R has an element from no namespace
    """
    assert_bindings(
        schema="msData/particles/particlesR016.xsd",
        is_valid=True,
        instance="msData/particles/particlesR016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r015_particles_r015_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's namespace=##any, R has an element targetNamespace
    """
    assert_bindings(
        schema="msData/particles/particlesR015.xsd",
        is_valid=True,
        instance="msData/particles/particlesR015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r013_particles_r013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's minOccurs=3, B's maxOccurs=8, R's minOccurs=3, B's
    maxOccurs=4, have 2 children
    """
    assert_bindings(
        schema="msData/particles/particlesR013.xsd",
        is_valid=True,
        instance="msData/particles/particlesR013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r012_particles_r012_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's minOccurs=0, B's maxOccurs=3, R's minOccurs=0, B's
    maxOccurs=2, but have 2 children
    """
    assert_bindings(
        schema="msData/particles/particlesR012.xsd",
        is_valid=True,
        instance="msData/particles/particlesR012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r011_particles_r011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's minOccurs=0, B's maxOccurs=4, R has 2 groups, each
    with maxOccurs as 4 and 0
    """
    assert_bindings(
        schema="msData/particles/particlesR011.xsd",
        is_valid=True,
        instance="msData/particles/particlesR011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r009_particles_r009_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's minOccurs=4, B's maxOccurs=4, R has 2 elements, each
    with minOccurs as 2 and 2
    """
    assert_bindings(
        schema="msData/particles/particlesR009.xsd",
        is_valid=True,
        instance="msData/particles/particlesR009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r008_particles_r008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's minOccurs=0, B's maxOccurs=3, R has 2 elements, each
    with maxOccurs as 2 and 2
    """
    assert_bindings(
        schema="msData/particles/particlesR008.xsd",
        is_valid=True,
        instance="msData/particles/particlesR008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r007_particles_r007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's minOccurs=0, B's maxOccurs=4, R has 2 elements, each
    with maxOccurs as 2 and 2
    """
    assert_bindings(
        schema="msData/particles/particlesR007.xsd",
        is_valid=True,
        instance="msData/particles/particlesR007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r005_particles_r005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's minOccurs=0, B's maxOccurs=unbounded, R has an
    element with minOccurs=1, maxOccurs=3
    """
    assert_bindings(
        schema="msData/particles/particlesR005.xsd",
        is_valid=True,
        instance="msData/particles/particlesR005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r004_particles_r004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's minOccurs=0, B's maxOccurs=3, R has an element with
    minOccurs=1, maxOccurs=3
    """
    assert_bindings(
        schema="msData/particles/particlesR004.xsd",
        is_valid=True,
        instance="msData/particles/particlesR004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r003_particles_r003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's minOccurs=0, B's maxOccurs=2, R's minOccurs=1, R's
    maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesR003.xsd",
        is_valid=True,
        instance="msData/particles/particlesR003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r002_particles_r002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's minOccurs=1, B's maxOccurs=1, R's minOccurs=1, R's
    maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesR002.xsd",
        is_valid=True,
        instance="msData/particles/particlesR002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_r001_particles_r001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Choice:Any -
    NSRecurseCheckCardinality) (Choice) R drived by restriction from
    (Choice) B : B's minOccurs=0, B's maxOccurs=1, R's minOccurs=1, R's
    maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesR001.xsd",
        is_valid=True,
        instance="msData/particles/particlesR001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_s011_particles_s011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (All:All - Recurse) (All)
    R drived by restriction from (All) B : B has (a, b), R has (a) which
    has a type that is a valid restriction from type of B
    """
    assert_bindings(
        schema="msData/particles/particlesS011.xsd",
        is_valid=True,
        instance="msData/particles/particlesS011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_s007_particles_s007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (All:All - Recurse) (All)
    R drived by restriction from (All) B : B has (a, b, c), R has (a, b,
    c)
    """
    assert_bindings(
        schema="msData/particles/particlesS007.xsd",
        is_valid=True,
        instance="msData/particles/particlesS007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_s004_particles_s004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (All:All - Recurse) (All)
    R drived by restriction from (All) B : B has (a, b, c), c is
    emptiable, R has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesS004.xsd",
        is_valid=True,
        instance="msData/particles/particlesS004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_s003_particles_s003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (All:All - Recurse) (All)
    R drived by restriction from (All) B : B has (a, b, c), b and c are
    emptiable, R has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesS003.xsd",
        is_valid=True,
        instance="msData/particles/particlesS003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_s001_particles_s001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (All:All - Recurse) (All)
    R drived by restriction from (All) B : B has (a, b), R has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesS001.xsd",
        is_valid=True,
        instance="msData/particles/particlesS001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_p002_particles_p002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (All:Any -
    NSRecurseCheckCardinality) (All) R drived by restriction from (any) B
    : B's minOccurs=1, B's maxOccurs=1, R has one child
    """
    assert_bindings(
        schema="msData/particles/particlesP002.xsd",
        is_valid=True,
        instance="msData/particles/particlesP002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob060_particles_ob060_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##local, foo,
    bar, ##targetNamespace, R's namespace=bar Added schemaDoc for
    xsi:schemaLoc'd additional schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb060.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb060.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob059_particles_ob059_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##local, foo,
    bar, ##targetNamespace, R's namespace=foo Added schemaDoc for
    xsi:schemaLoc'd additional schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb059.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb059.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob057_particles_ob057_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##local, foo,
    bar, ##targetNamespace, R's namespace=foo, ##local, bar Added
    schemaDoc for xsi:schemaLoc'd additional schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb057.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb057.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob056_particles_ob056_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##local, foo,
    bar, ##targetNamespace, R's namespace=##targetNamespace, ##local
    """
    assert_bindings(
        schema="msData/particles/particlesOb056.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb056.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob055_particles_ob055_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##local, foo,
    bar, ##targetNamespace, R's namespace=##local, foo, bar,
    ##targetNamespace
    """
    assert_bindings(
        schema="msData/particles/particlesOb055.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb055.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob054_particles_ob054_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##local, foo,
    bar, ##targetNamespace, R's namespace=foo bar' Added schemaDoc for
    xsi:schemaLoc'd additional schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb054.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb054.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob053_particles_ob053_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##local, foo,
    bar, ##targetNamespace, R's namespace=##targetNamespace
    """
    assert_bindings(
        schema="msData/particles/particlesOb053.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb053.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob052_particles_ob052_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##local, foo,
    bar, ##targetNamespace, R's namespace=##local Added schemaDoc for
    xsi:schemaLoc'd additional schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb052.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb052.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob048_particles_ob048_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=foo bar', R's
    namespace=bar Added schemaDoc for xsi:schemaLoc'd additional schema,
    per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb048.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb048.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob047_particles_ob047_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=foo bar', R's
    namespace=foo Added schemaDoc for xsi:schemaLoc'd additional schema,
    per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb047.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb047.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob042_particles_ob042_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=foo bar', R's
    namespace=foo bar' Added schemaDoc for xsi:schemaLoc'd additional
    schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb042.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb042.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob032_particles_ob032_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's
    namespace=##targetNamespace, R's namespace=##targetNamespace
    """
    assert_bindings(
        schema="msData/particles/particlesOb032.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb032.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob022_particles_ob022_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##local, R's
    namespace=##local Added schemaDoc for xsi:schemaLoc'd additional
    schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb022.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb022.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob015_particles_ob015_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##other, R's
    namespace=foo bar' Added schemaDoc for xsi:schemaLoc'd additional
    schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb015.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob012_particles_ob012_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##other, R's
    namespace=##other Added schemaDoc for xsi:schemaLoc'd additional
    schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb012.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob007_particles_ob007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##any, R's
    namespace=##local, foo, bar, ##targetNamespace Added schemaDoc for
    xsi:schemaLoc'd additional schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb007.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob006_particles_ob006_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##any, R's
    namespace=foo bar' Added schemaDoc for xsi:schemaLoc'd additional
    schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb006.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob005_particles_ob005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##any, R's
    namespace=##targetNamespace
    """
    assert_bindings(
        schema="msData/particles/particlesOb005.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ob003_particles_ob003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's namespace=##any, R's
    namespace=##other Added schemaDoc for xsi:schemaLoc'd additional
    schema, per WG decision
    """
    assert_bindings(
        schema="msData/particles/particlesOb003.xsd",
        is_valid=True,
        instance="msData/particles/particlesOb003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_oa014_particles_oa014_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's minOccurs=2, B's
    maxOccurs=4, R's minOccurs=3, R's maxOccurs=3
    """
    assert_bindings(
        schema="msData/particles/particlesOa014.xsd",
        is_valid=True,
        instance="msData/particles/particlesOa014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_oa013_particles_oa013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's minOccurs=2, B's
    maxOccurs=4, R's minOccurs=2, R's maxOccurs=3
    """
    assert_bindings(
        schema="msData/particles/particlesOa013.xsd",
        is_valid=True,
        instance="msData/particles/particlesOa013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_oa012_particles_oa012_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's minOccurs=2, B's
    maxOccurs=4, R's minOccurs=3, R's maxOccurs=4
    """
    assert_bindings(
        schema="msData/particles/particlesOa012.xsd",
        is_valid=True,
        instance="msData/particles/particlesOa012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_oa011_particles_oa011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's minOccurs=2, B's
    maxOccurs=4, R's minOccurs=2, R's maxOccurs=4
    """
    assert_bindings(
        schema="msData/particles/particlesOa011.xsd",
        is_valid=True,
        instance="msData/particles/particlesOa011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_oa006_particles_oa006_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's minOccurs=absent, B's
    maxOccurs=absent, R's minOccurs=absent, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesOa006.xsd",
        is_valid=True,
        instance="msData/particles/particlesOa006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_oa003_particles_oa003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's minOccurs=absent, B's
    maxOccurs=absent, R's minOccurs=1, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesOa003.xsd",
        is_valid=True,
        instance="msData/particles/particlesOa003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_oa001_particles_oa001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Any:Any- NSSubset) (any)
    R drived by restriction from (any) B : B's minOccurs=absent, B's
    maxOccurs=absent, R's minOccurs=absent, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesOa001.xsd",
        is_valid=True,
        instance="msData/particles/particlesOa001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_m035_particles_m035_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Sequence -
    RecurseAsIfGroup) element R drived by restriction from (Sequence) B :
    B's parent is choice, B=(a*, b+), R=(b+)
    """
    assert_bindings(
        schema="msData/particles/particlesM035.xsd",
        is_valid=True,
        instance="msData/particles/particlesM035.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_m003_particles_m003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Sequence -
    RecurseAsIfGroup) element R drived by restriction from (Sequence) B :
    B's parent is choice, B's minOccurs=2, R's minOccurs=3
    """
    assert_bindings(
        schema="msData/particles/particlesM003.xsd",
        is_valid=True,
        instance="msData/particles/particlesM003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_m002_particles_m002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Sequence -
    RecurseAsIfGroup) element R drived by restriction from (Sequence) B :
    B's parent is choice, B's minOccurs=2, R's minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesM002.xsd",
        is_valid=True,
        instance="msData/particles/particlesM002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l029_particles_l029_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B has element 'foo' with final=#all, R has
    element 'foo' with final=#all
    """
    assert_bindings(
        schema="msData/particles/particlesL029.xsd",
        is_valid=True,
        instance="msData/particles/particlesL029.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l028_particles_l028_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B has element 'foo' with block=substitution, R
    has element 'foo' with block=substitution
    """
    assert_bindings(
        schema="msData/particles/particlesL028.xsd",
        is_valid=True,
        instance="msData/particles/particlesL028.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l025_particles_l025_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B has element 'foo' with block=substitution, R
    has element 'foo' with block=#all
    """
    assert_bindings(
        schema="msData/particles/particlesL025.xsd",
        is_valid=True,
        instance="msData/particles/particlesL025.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l023_particles_l023_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B has element 'foo' with block=restriction, R
    has element 'foo' with block=restriction
    """
    assert_bindings(
        schema="msData/particles/particlesL023.xsd",
        is_valid=True,
        instance="msData/particles/particlesL023.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l021_particles_l021_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B has element 'foo' with block=restriction, R
    has element 'foo' with block=#all
    """
    assert_bindings(
        schema="msData/particles/particlesL021.xsd",
        is_valid=True,
        instance="msData/particles/particlesL021.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l018_particles_l018_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B has element 'foo' with block=extension, R
    has element 'foo' with block=extension
    """
    assert_bindings(
        schema="msData/particles/particlesL018.xsd",
        is_valid=True,
        instance="msData/particles/particlesL018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l017_particles_l017_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B has element 'foo' with block=extension, R
    has element 'foo' with block=#all
    """
    assert_bindings(
        schema="msData/particles/particlesL017.xsd",
        is_valid=True,
        instance="msData/particles/particlesL017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l013_particles_l013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B has element 'foo' with block=#all, R has
    element 'foo' with block=#all
    """
    assert_bindings(
        schema="msData/particles/particlesL013.xsd",
        is_valid=True,
        instance="msData/particles/particlesL013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l012_particles_l012_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B has element 'foo' with mixed=TRUE, R has
    element 'foo' with mixed=FALSE
    """
    assert_bindings(
        schema="msData/particles/particlesL012.xsd",
        is_valid=True,
        instance="msData/particles/particlesL012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l007_particles_l007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B's minOccurs=B' maxOccurs=absent, R's
    maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesL007.xsd",
        is_valid=True,
        instance="msData/particles/particlesL007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l006_particles_l006_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B's minOccurs=B' maxOccurs=absent, R's
    minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesL006.xsd",
        is_valid=True,
        instance="msData/particles/particlesL006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_l003_particles_l003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:Choice -
    RecurseAsIfGroup) element R drived by restriction from (Choice) B :
    B's parent is sequence, B's minOccurs= 2, R's maxOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesL003.xsd",
        is_valid=True,
        instance="msData/particles/particlesL003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_k008_particles_k008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:All -
    RecurseAsIfGroup) element R drived by restriction from (all) B : R has
    an element (min=maxOccurs=1) from a different namespace than the
    targetNS
    """
    assert_bindings(
        schema="msData/particles/particlesK008.xsd",
        is_valid=True,
        instance="msData/particles/particlesK008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_k005_particles_k005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:All -
    RecurseAsIfGroup) element R drived by restriction from (all) B : B's
    minOccurs=0, B' maxOccurs=absent, R's minOccurs=1, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesK005.xsd",
        is_valid=True,
        instance="msData/particles/particlesK005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_k003_particles_k003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:All -
    RecurseAsIfGroup) element R drived by restriction from (all) B : B's
    minOccurs=1, B' maxOccurs=absent, R's minOccurs=absent, R's
    maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesK003.xsd",
        is_valid=True,
        instance="msData/particles/particlesK003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_k002_particles_k002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:All -
    RecurseAsIfGroup) element R drived by restriction from (all) B : B's
    minOccurs=absent, B' maxOccurs=1, R's minOccurs=1, R's
    maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesK002.xsd",
        is_valid=True,
        instance="msData/particles/particlesK002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_k001_particles_k001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (Elt:All -
    RecurseAsIfGroup) element R drived by restriction from (all) B : B's
    minOccurs=1, B' maxOccurs=1, R's minOccurs=1, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesK001.xsd",
        is_valid=True,
        instance="msData/particles/particlesK001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ju003_particles_ju003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (##local, ##targetNamespace, nsFoo, nsBar), R's
    targetNamespace=targetNamespace, B's minOccurs less than R's minOccurs
    , B's maxOccurs > R's maxOccurs
    """
    assert_bindings(
        schema="msData/particles/particlesJu003.xsd",
        is_valid=True,
        instance="msData/particles/particlesJu003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ju002_particles_ju002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (##local, ##targetNamespace, nsFoo, nsBar), R's targetNamespace=nsFoo,
    B's minOccurs less than R's minOccurs , B's maxOccurs > R's maxOccurs
    """
    assert_bindings(
        schema="msData/particles/particlesJu002.xsd",
        is_valid=True,
        instance="msData/particles/particlesJu002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ju001_particles_ju001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (##local, ##targetNamespace, nsFoo, nsBar), R's
    targetNamespace=absent, B's minOccurs less than R's minOccurs , B's
    maxOccurs > R's maxOccurs
    """
    assert_bindings(
        schema="msData/particles/particlesJu001.xsd",
        is_valid=True,
        instance="msData/particles/particlesJu001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_js001_particles_js001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (##local), R's namespace=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJs001.xsd",
        is_valid=True,
        instance="msData/particles/particlesJs001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_jq010_particles_jq010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (##targetNamespace), R's namespace=targetNamespace, B's
    maxOccurs=absent, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJq010.xsd",
        is_valid=True,
        instance="msData/particles/particlesJq010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jq008_particles_jq008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (##targetNamespace), R's namespace=targetNamespace, B's maxOccurs=1,
    R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJq008.xsd",
        is_valid=True,
        instance="msData/particles/particlesJq008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_jq007_particles_jq007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (##targetNamespace), R's namespace=targetNamespace, B's maxOccurs=1,
    R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJq007.xsd",
        is_valid=True,
        instance="msData/particles/particlesJq007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_jp005_particles_jp005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (##targetNamespace), R's namespace=targetNamespace, B's minOccurs=1,
    R's minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesJp005.xsd",
        is_valid=True,
        instance="msData/particles/particlesJp005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jp004_particles_jp004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (##targetNamespace), R's namespace=targetNamespace, B's minOccurs=1,
    R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJp004.xsd",
        is_valid=True,
        instance="msData/particles/particlesJp004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jn010_particles_jn010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (uriReferences), R's targetNamespace=ref of an elt from valid
    targetNS, B's maxOccurs=absent, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJn010.xsd",
        is_valid=True,
        instance="msData/particles/particlesJn010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jn008_particles_jn008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (uriReferences), R's targetNamespace=ref of an elt from valid
    targetNS, B's maxOccurs=1, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJn008.xsd",
        is_valid=True,
        instance="msData/particles/particlesJn008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jn007_particles_jn007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (uriReferences), R's targetNamespace=ref of an elt from valid
    targetNS, B's maxOccurs=1, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJn007.xsd",
        is_valid=True,
        instance="msData/particles/particlesJn007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jm005_particles_jm005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (uriReferences), R's targetNamespace=ref of an elt from valid
    targetNS, B's minOccurs=1, R's minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesJm005.xsd",
        is_valid=True,
        instance="msData/particles/particlesJm005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jm004_particles_jm004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (uriReferences), R's targetNamespace=ref of an elt from valid
    targetNS, B's minOccurs=1, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJm004.xsd",
        is_valid=True,
        instance="msData/particles/particlesJm004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jl001_particles_jl001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=list
    (uriReferences [ foo, bar ]), R's targetNamespace=foo
    """
    assert_bindings(
        schema="msData/particles/particlesJl001.xsd",
        is_valid=True,
        instance="msData/particles/particlesJl001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk016_particles_jk016_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=absent, B's maxOccurs=2, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJk016.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk015_particles_jk015_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=1, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJk015.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk013_particles_jk013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=absent, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJk013.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk011_particles_jk011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=absent, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJk011.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk010_particles_jk010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=absent, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJk010.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk008_particles_jk008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=1, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJk008.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk007_particles_jk007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=1, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJk007.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk005_particles_jk005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=0, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJk005.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk004_particles_jk004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=unbounded, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJk004.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk003_particles_jk003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=unbounded, R's maxOccurs=999999
    """
    assert_bindings(
        schema="msData/particles/particlesJk003.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk002_particles_jk002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=unbounded, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJk002.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jk001_particles_jk001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=unbounded, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJk001.xsd",
        is_valid=True,
        instance="msData/particles/particlesJk001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jj011_particles_jj011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=1, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJj011.xsd",
        is_valid=True,
        instance="msData/particles/particlesJj011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jj010_particles_jj010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=0, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJj010.xsd",
        is_valid=True,
        instance="msData/particles/particlesJj010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jj009_particles_jj009_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=absent, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJj009.xsd",
        is_valid=True,
        instance="msData/particles/particlesJj009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jj008_particles_jj008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=absent, R's minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesJj008.xsd",
        is_valid=True,
        instance="msData/particles/particlesJj008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jj007_particles_jj007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=absent, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJj007.xsd",
        is_valid=True,
        instance="msData/particles/particlesJj007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jj005_particles_jj005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=1, R's minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesJj005.xsd",
        is_valid=True,
        instance="msData/particles/particlesJj005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jj004_particles_jj004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=1, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJj004.xsd",
        is_valid=True,
        instance="msData/particles/particlesJj004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jj002_particles_jj002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=0, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJj002.xsd",
        is_valid=True,
        instance="msData/particles/particlesJj002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jj001_particles_jj001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##other,
    R's targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=0, R's minOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJj001.xsd",
        is_valid=True,
        instance="msData/particles/particlesJj001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf016_particles_jf016_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=2, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJf016.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf015_particles_jf015_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=1, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJf015.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf013_particles_jf013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=absent, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJf013.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf011_particles_jf011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=absent, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJf011.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf010_particles_jf010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=absent, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJf010.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf008_particles_jf008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=1, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJf008.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf007_particles_jf007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=1, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJf007.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf005_particles_jf005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=0, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJf005.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf004_particles_jf004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=unbounded, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJf004.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf003_particles_jf003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=unbounded, R's maxOccurs=999999
    """
    assert_bindings(
        schema="msData/particles/particlesJf003.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf002_particles_jf002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=unbounded, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJf002.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jf001_particles_jf001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    maxOccurs=unbounded, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJf001.xsd",
        is_valid=True,
        instance="msData/particles/particlesJf001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_je011_particles_je011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=1, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJe011.xsd",
        is_valid=True,
        instance="msData/particles/particlesJe011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_je010_particles_je010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=0, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJe010.xsd",
        is_valid=True,
        instance="msData/particles/particlesJe010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_je009_particles_je009_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=absent, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJe009.xsd",
        is_valid=True,
        instance="msData/particles/particlesJe009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_je008_particles_je008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=absent, R's minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesJe008.xsd",
        is_valid=True,
        instance="msData/particles/particlesJe008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_je007_particles_je007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=absent, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJe007.xsd",
        is_valid=True,
        instance="msData/particles/particlesJe007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_je005_particles_je005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=1, R's minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesJe005.xsd",
        is_valid=True,
        instance="msData/particles/particlesJe005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_je004_particles_je004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=1, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJe004.xsd",
        is_valid=True,
        instance="msData/particles/particlesJe004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_je002_particles_je002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=0, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJe002.xsd",
        is_valid=True,
        instance="msData/particles/particlesJe002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_je001_particles_je001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=ref of an elt from different targetNS, B's
    minOccurs=0, R's minOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJe001.xsd",
        is_valid=True,
        instance="msData/particles/particlesJe001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jd016_particles_jd016_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=2, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJd016.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jd015_particles_jd015_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=1, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJd015.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jd013_particles_jd013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=absent, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJd013.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jd011_particles_jd011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=absent, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJd011.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jd010_particles_jd010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=absent, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJd010.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jd008_particles_jd008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=1, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJd008.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_jd007_particles_jd007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=1, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJd007.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jd005_particles_jd005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=0, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJd005.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jd004_particles_jd004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=unbounded, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJd004.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_jd003_particles_jd003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=unbounded, R's maxOccurs=999999
    """
    assert_bindings(
        schema="msData/particles/particlesJd003.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jd002_particles_jd002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=unbounded, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJd002.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jd001_particles_jd001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's maxOccurs=unbounded, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJd001.xsd",
        is_valid=True,
        instance="msData/particles/particlesJd001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jc011_particles_jc011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's minOccurs=1, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJc011.xsd",
        is_valid=True,
        instance="msData/particles/particlesJc011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jc010_particles_jc010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's minOccurs=0, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJc010.xsd",
        is_valid=True,
        instance="msData/particles/particlesJc010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jc009_particles_jc009_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's minOccurs=absent, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJc009.xsd",
        is_valid=True,
        instance="msData/particles/particlesJc009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jc008_particles_jc008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's minOccurs=absent, R's minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesJc008.xsd",
        is_valid=True,
        instance="msData/particles/particlesJc008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jc007_particles_jc007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's minOccurs=absent, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJc007.xsd",
        is_valid=True,
        instance="msData/particles/particlesJc007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jc005_particles_jc005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's minOccurs=1, R's minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesJc005.xsd",
        is_valid=True,
        instance="msData/particles/particlesJc005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jc004_particles_jc004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's minOccurs=1, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJc004.xsd",
        is_valid=True,
        instance="msData/particles/particlesJc004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jc002_particles_jc002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's minOccurs=0, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJc002.xsd",
        is_valid=True,
        instance="msData/particles/particlesJc002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jc001_particles_jc001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=absent, B's minOccurs=0, R's minOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJc001.xsd",
        is_valid=True,
        instance="msData/particles/particlesJc001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jb016_particles_jb016_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=2, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJb016.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jb015_particles_jb015_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=1, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJb015.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jb013_particles_jb013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=absent, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJb013.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jb011_particles_jb011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=absent, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJb011.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_jb010_particles_jb010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=absent, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJb010.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jb008_particles_jb008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=1, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJb008.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_jb007_particles_jb007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=1, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJb007.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_jb005_particles_jb005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=0, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJb005.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jb004_particles_jb004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=unbounded, R's maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJb004.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_jb003_particles_jb003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=unbounded, R's maxOccurs=999999
    """
    assert_bindings(
        schema="msData/particles/particlesJb003.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_jb002_particles_jb002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=unbounded, R's maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJb002.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_jb001_particles_jb001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's maxOccurs=unbounded, R's maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJb001.xsd",
        is_valid=True,
        instance="msData/particles/particlesJb001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ja011_particles_ja011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's minOccurs=1, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJa011.xsd",
        is_valid=True,
        instance="msData/particles/particlesJa011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ja010_particles_ja010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's minOccurs=0, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJa010.xsd",
        is_valid=True,
        instance="msData/particles/particlesJa010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ja009_particles_ja009_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's minOccurs=absent, R's minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesJa009.xsd",
        is_valid=True,
        instance="msData/particles/particlesJa009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ja008_particles_ja008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's minOccurs=absent, R's minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesJa008.xsd",
        is_valid=True,
        instance="msData/particles/particlesJa008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ja007_particles_ja007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's minOccurs=absent, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJa007.xsd",
        is_valid=True,
        instance="msData/particles/particlesJa007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ja005_particles_ja005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's minOccurs=1, R's minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesJa005.xsd",
        is_valid=True,
        instance="msData/particles/particlesJa005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ja004_particles_ja004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's minOccurs=1, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJa004.xsd",
        is_valid=True,
        instance="msData/particles/particlesJa004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ja002_particles_ja002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's minOccurs=0, R's minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesJa002.xsd",
        is_valid=True,
        instance="msData/particles/particlesJa002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ja001_particles_ja001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Particle Derivation OK (elt:Any) element R
    drived by restriction from wildcard (any) B : B's namespace=##any, R's
    targetNamespace=foo, B's minOccurs=0, R's minOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesJa001.xsd",
        is_valid=True,
        instance="msData/particles/particlesJa001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ik026_particles_ik026_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B type=U1, union of simpleType s1, s2, R
    type=x1 which is drived by restriction from the U1.
    """
    assert_bindings(
        schema="msData/particles/particlesIk026.xsd",
        is_valid=True,
        instance="msData/particles/particlesIk026.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ik012_particles_ik012_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B type=simpleType with union (S1, S2), R
    type=simpleType with union (S1, S2)
    """
    assert_bindings(
        schema="msData/particles/particlesIk012.xsd",
        is_valid=True,
        instance="msData/particles/particlesIk012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ik004_particles_ik004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B type=simpleType xsd:string, R
    type=simpleType restriction of xsd:string
    """
    assert_bindings(
        schema="msData/particles/particlesIk004.xsd",
        is_valid=True,
        instance="msData/particles/particlesIk004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ik001_particles_ik001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B type=simpleType 'foo', R type=simpleType
    'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesIk001.xsd",
        is_valid=True,
        instance="msData/particles/particlesIk001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ij006_particles_ij006_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B type=complexType 'Z' which is a drived
    by restriction of 'foo', R type=complexType 'Z' which is a drived by
    restriction of 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesIj006.xsd",
        is_valid=True,
        instance="msData/particles/particlesIj006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ij005_particles_ij005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B type=complexType 'foo', R
    type=complexType 'Z' which is a drived by restriction of 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesIj005.xsd",
        is_valid=True,
        instance="msData/particles/particlesIj005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ij002_particles_ij002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B type=complexType 'foo', R
    type=complexType 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesIj002.xsd",
        is_valid=True,
        instance="msData/particles/particlesIj002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ij001_particles_ij001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B type=absent, R type=anyType
    """
    assert_bindings(
        schema="msData/particles/particlesIj001.xsd",
        is_valid=True,
        instance="msData/particles/particlesIj001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ig015_particles_ig015_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B disallowed substitutions=empty, R
    disallowed substitutions=sub
    """
    assert_bindings(
        schema="msData/particles/particlesIg015.xsd",
        is_valid=True,
        instance="msData/particles/particlesIg015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ig014_particles_ig014_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B disallowed substitutions=absent, R
    disallowed substitutions=sub
    """
    assert_bindings(
        schema="msData/particles/particlesIg014.xsd",
        is_valid=True,
        instance="msData/particles/particlesIg014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ig012_particles_ig012_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B disallowed substitutions=sub, ext , R
    disallowed substitutions=#all
    """
    assert_bindings(
        schema="msData/particles/particlesIg012.xsd",
        is_valid=True,
        instance="msData/particles/particlesIg012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ig011_particles_ig011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B disallowed substitutions=res, sub, R
    disallowed substitutions=res, sub, ext
    """
    assert_bindings(
        schema="msData/particles/particlesIg011.xsd",
        is_valid=True,
        instance="msData/particles/particlesIg011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ig005_particles_ig005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B disallowed substitutions=sub, ext, res,
    R disallowed substitutions=#all
    """
    assert_bindings(
        schema="msData/particles/particlesIg005.xsd",
        is_valid=True,
        instance="msData/particles/particlesIg005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ig003_particles_ig003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B disallowed substitutions=restriction, R
    disallowed substitutions=restriction
    """
    assert_bindings(
        schema="msData/particles/particlesIg003.xsd",
        is_valid=True,
        instance="msData/particles/particlesIg003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ig002_particles_ig002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B disallowed substitutions=extension, R
    disallowed substitutions=extension
    """
    assert_bindings(
        schema="msData/particles/particlesIg002.xsd",
        is_valid=True,
        instance="msData/particles/particlesIg002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ig001_particles_ig001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B disallowed substitutions=substitution, R
    disallowed substitutions=substitution
    """
    assert_bindings(
        schema="msData/particles/particlesIg001.xsd",
        is_valid=True,
        instance="msData/particles/particlesIg001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_if006_particles_if006_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B fixed=empty, R fixed=empty
    """
    assert_bindings(
        schema="msData/particles/particlesIf006.xsd",
        is_valid=True,
        instance="msData/particles/particlesIf006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_if005_particles_if005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B fixed=foo', R fixed=foo'
    """
    assert_bindings(
        schema="msData/particles/particlesIf005.xsd",
        is_valid=True,
        instance="msData/particles/particlesIf005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_if004_particles_if004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B default=empty, R default=foo'
    """
    assert_bindings(
        schema="msData/particles/particlesIf004.xsd",
        is_valid=True,
        instance="msData/particles/particlesIf004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_if003_particles_if003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B default=bar, R default=foo'
    """
    assert_bindings(
        schema="msData/particles/particlesIf003.xsd",
        is_valid=True,
        instance="msData/particles/particlesIf003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_if002_particles_if002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B default=absent, R default=foo'
    """
    assert_bindings(
        schema="msData/particles/particlesIf002.xsd",
        is_valid=True,
        instance="msData/particles/particlesIf002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_if001_particles_if001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B default=absent, R default=empty
    """
    assert_bindings(
        schema="msData/particles/particlesIf001.xsd",
        is_valid=True,
        instance="msData/particles/particlesIf001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie016_particles_ie016_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=2, R maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesIe016.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie015_particles_ie015_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=1, R maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesIe015.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie013_particles_ie013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=absent, R maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesIe013.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie011_particles_ie011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=absent, R maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesIe011.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie010_particles_ie010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=absent, R maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesIe010.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie008_particles_ie008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=1, R maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesIe008.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie007_particles_ie007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=1, R maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesIe007.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie005_particles_ie005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=0, R maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesIe005.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie004_particles_ie004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=unbounded, R maxOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesIe004.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie003_particles_ie003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=unbounded, R maxOccurs=999999
    """
    assert_bindings(
        schema="msData/particles/particlesIe003.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie002_particles_ie002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=unbounded, R maxOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesIe002.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ie001_particles_ie001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B maxOccurs=unbounded, R maxOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesIe001.xsd",
        is_valid=True,
        instance="msData/particles/particlesIe001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_id011_particles_id011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B minOccurs=1, R minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesId011.xsd",
        is_valid=True,
        instance="msData/particles/particlesId011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_id010_particles_id010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B minOccurs=0, R minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesId010.xsd",
        is_valid=True,
        instance="msData/particles/particlesId010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_id009_particles_id009_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B minOccurs=absent, R minOccurs=absent
    """
    assert_bindings(
        schema="msData/particles/particlesId009.xsd",
        is_valid=True,
        instance="msData/particles/particlesId009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_id008_particles_id008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B minOccurs=absent, R minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesId008.xsd",
        is_valid=True,
        instance="msData/particles/particlesId008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_id007_particles_id007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B minOccurs=absent, R minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesId007.xsd",
        is_valid=True,
        instance="msData/particles/particlesId007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_id005_particles_id005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B minOccurs=1, R minOccurs=2
    """
    assert_bindings(
        schema="msData/particles/particlesId005.xsd",
        is_valid=True,
        instance="msData/particles/particlesId005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_id004_particles_id004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B minOccurs=1, R minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesId004.xsd",
        is_valid=True,
        instance="msData/particles/particlesId004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_id002_particles_id002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B minOccurs=0, R minOccurs=1
    """
    assert_bindings(
        schema="msData/particles/particlesId002.xsd",
        is_valid=True,
        instance="msData/particles/particlesId002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_id001_particles_id001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B minOccurs=0, R minOccurs=0
    """
    assert_bindings(
        schema="msData/particles/particlesId001.xsd",
        is_valid=True,
        instance="msData/particles/particlesId001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ic007_particles_ic007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B (B is from included XSD): B
    targetNanespace=absent, R targetNanespace=foo
    """
    assert_bindings(
        schema="msData/particles/particlesIc007.xsd",
        is_valid=True,
        instance="msData/particles/particlesIc007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ic006_particles_ic006_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B (B is from included XSD): B
    targetNanespace=absent, R targetNanespace=absent
    """
    assert_bindings(
        schema="msData/particles/particlesIc006.xsd",
        is_valid=True,
        instance="msData/particles/particlesIc006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ic005_particles_ic005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B (B is from included XSD): B
    targetNanespace=foo, R targetNanespace=foo
    """
    assert_bindings(
        schema="msData/particles/particlesIc005.xsd",
        is_valid=True,
        instance="msData/particles/particlesIc005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ic001_particles_ic001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B targetNanespace=foo, R
    targetNanespace=foo
    """
    assert_bindings(
        schema="msData/particles/particlesIc001.xsd",
        is_valid=True,
        instance="msData/particles/particlesIc001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ib005_particles_ib005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B name=foo, R name=ref to group which has
    foo only
    """
    assert_bindings(
        schema="msData/particles/particlesIb005.xsd",
        is_valid=True,
        instance="msData/particles/particlesIb005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ib003_particles_ib003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B name=foo, R name=ref to foo
    """
    assert_bindings(
        schema="msData/particles/particlesIb003.xsd",
        is_valid=True,
        instance="msData/particles/particlesIb003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ib001_particles_ib001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B name=foo, R name=foo
    """
    assert_bindings(
        schema="msData/particles/particlesIb001.xsd",
        is_valid=True,
        instance="msData/particles/particlesIb001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ia005_particles_ia005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B nillable=absent, R nillable=FALSE
    """
    assert_bindings(
        schema="msData/particles/particlesIa005.xsd",
        is_valid=True,
        instance="msData/particles/particlesIa005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ia004_particles_ia004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B nillable=FALSE, R nillable=absent
    """
    assert_bindings(
        schema="msData/particles/particlesIa004.xsd",
        is_valid=True,
        instance="msData/particles/particlesIa004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ia003_particles_ia003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B nillable=absent, R nillable=absent
    """
    assert_bindings(
        schema="msData/particles/particlesIa003.xsd",
        is_valid=True,
        instance="msData/particles/particlesIa003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ia002_particles_ia002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B nillable=TRUE, R nillable=TRUE
    """
    assert_bindings(
        schema="msData/particles/particlesIa002.xsd",
        is_valid=True,
        instance="msData/particles/particlesIa002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ia001_particles_ia001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : NameAndTypedOK (elt:elt ) element R drived by
    restriction from element B: B nillable=FALSE, R nillable=FALSE
    """
    assert_bindings(
        schema="msData/particles/particlesIa001.xsd",
        is_valid=True,
        instance="msData/particles/particlesIa001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha018_particles_ha018_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of particles: All
    has only one member
    """
    assert_bindings(
        schema="msData/particles/particlesHa018.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha017_particles_ha017_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of particles: All is
    empty
    """
    assert_bindings(
        schema="msData/particles/particlesHa017.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha016_particles_ha016_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'choice' : choice
    ( C) appears under 'sequence' (P) with minOccurs=maxOccurs=1, and the
    (P) is itself among the particles of a 'choice'
    """
    assert_bindings(
        schema="msData/particles/particlesHa016.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha015_particles_ha015_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'choice' : choice
    ( C) appears under 'choice' (P) with minOccurs=maxOccurs=1, and the
    (P) is itself among the particles of a 'choice'
    """
    assert_bindings(
        schema="msData/particles/particlesHa015.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha014_particles_ha014_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'choice' : choice
    ( C) appears under group (P) with minOccurs=maxOccurs=1, and the (P)
    is itself among the particles of a 'choice'
    """
    assert_bindings(
        schema="msData/particles/particlesHa014.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha013_particles_ha013_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'choice' : choice
    ( C) appears under 'sequence' (P) with minOccurs=maxOccurs=1, and the
    ( C) has only one member
    """
    assert_bindings(
        schema="msData/particles/particlesHa013.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa013.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha012_particles_ha012_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'choice' : choice
    ( C) appears under 'choice' (P) with minOccurs=maxOccurs=1, and the (
    C) has only one member
    """
    assert_bindings(
        schema="msData/particles/particlesHa012.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha011_particles_ha011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'choice' : choice
    ( C) appears under group (P) with minOccurs=maxOccurs=1, and the ( C)
    has only one member
    """
    assert_bindings(
        schema="msData/particles/particlesHa011.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha010_particles_ha010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'choice' : choice
    ( C) is empty and the 'sequence' within which ( C) appears has
    minOccurs of 0
    """
    assert_bindings(
        schema="msData/particles/particlesHa010.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha009_particles_ha009_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'choice' : choice
    ( C) is empty and the 'choice' within which ( C) appears has minOccurs
    of 0
    """
    assert_bindings(
        schema="msData/particles/particlesHa009.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha007_particles_ha007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'sequence' :
    sequence (S) appears under a 'sequence' (P) with
    minOccurs=maxOccurs=1, and the (P) is itself among the particles of a
    'sequence'
    """
    assert_bindings(
        schema="msData/particles/particlesHa007.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha006_particles_ha006_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'sequence' :
    sequence (S) appears under a 'choice' (P) with minOccurs=maxOccurs=1,
    and the (P) is itself among the particles of a 'sequence'
    """
    assert_bindings(
        schema="msData/particles/particlesHa006.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha005_particles_ha005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'sequence' :
    sequence (S) appears under a model group (P) with
    minOccurs=maxOccurs=1, and the (P) is itself among the particles of a
    'sequence'
    """
    assert_bindings(
        schema="msData/particles/particlesHa005.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha004_particles_ha004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'sequence' :
    sequence (S) appears under a 'sequence' (P) with
    minOccurs=maxOccurs=1, and the (S) has only one member
    """
    assert_bindings(
        schema="msData/particles/particlesHa004.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha003_particles_ha003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'sequence' :
    sequence (S) appears under a 'choice' (P) with minOccurs=maxOccurs=1,
    and the (S) has only one member
    """
    assert_bindings(
        schema="msData/particles/particlesHa003.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha002_particles_ha002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'sequence' :
    sequence (S) appears under a model group (P) with
    minOccurs=maxOccurs=1, and the (S) has only one member
    """
    assert_bindings(
        schema="msData/particles/particlesHa002.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ha001_particles_ha001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : ignore pointless occurences of 'sequence'
    :sequence is empty
    """
    assert_bindings(
        schema="msData/particles/particlesHa001.xsd",
        is_valid=True,
        instance="msData/particles/particlesHa001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_fb004_particles_fb004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : E drived by extension from B, B=group,
    E=sequence with B as the first content particle (follow by sequence)
    """
    assert_bindings(
        schema="msData/particles/particlesFb004.xsd",
        is_valid=True,
        instance="msData/particles/particlesFb004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_fb001_particles_fb001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : E drived by extension from B, B=choice,
    E=sequence with B as the first content particle (follow by group)
    """
    assert_bindings(
        schema="msData/particles/particlesFb001.xsd",
        is_valid=True,
        instance="msData/particles/particlesFb001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_fa005_particles_fa005_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : E drived by extension from B, B= 'any', E=same
    as B
    """
    assert_bindings(
        schema="msData/particles/particlesFa005.xsd",
        is_valid=True,
        instance="msData/particles/particlesFa005.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_fa004_particles_fa004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : E drived by extension from B, B= group, E=same
    as B
    """
    assert_bindings(
        schema="msData/particles/particlesFa004.xsd",
        is_valid=True,
        instance="msData/particles/particlesFa004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_fa003_particles_fa003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : E drived by extension from B, B= 'choice',
    E=same as B, different annotation properties
    """
    assert_bindings(
        schema="msData/particles/particlesFa003.xsd",
        is_valid=True,
        instance="msData/particles/particlesFa003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_fa002_particles_fa002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : E drived by extension from B, B= 'sequence',
    E=same as B, same annotation properties
    """
    assert_bindings(
        schema="msData/particles/particlesFa002.xsd",
        is_valid=True,
        instance="msData/particles/particlesFa002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec041_particles_ec041_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (x)
    """
    assert_bindings(
        schema="msData/particles/particlesEc041.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc041.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec040_particles_ec040_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (b,b,b,b,x)
    """
    assert_bindings(
        schema="msData/particles/particlesEc040.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc040.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec039_particles_ec039_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (b,b,b,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc039.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc039.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec038_particles_ec038_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (a,a,a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc038.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc038.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec037_particles_ec037_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (b,b,b,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc037.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc037.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec036_particles_ec036_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (b,a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc036.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc036.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ec035_particles_ec035_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (a,a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc035.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc035.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec034_particles_ec034_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc034.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc034.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec033_particles_ec033_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc033.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc033.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec032_particles_ec032_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc032.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc032.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec031_particles_ec031_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc031.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc031.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ec030_particles_ec030_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (b,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc030.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc030.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_ec029_particles_ec029_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc029.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc029.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec028_particles_ec028_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc028.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc028.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec027_particles_ec027_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc027.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc027.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec026_particles_ec026_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=choice (a|b), and the instant XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesEc026.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc026.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec025_particles_ec025_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=choice (a|b), and the instant
    XML has ( x )
    """
    assert_bindings(
        schema="msData/particles/particlesEc025.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc025.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec024_particles_ec024_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=choice (a|b), and the instant
    XML has (a, a, x)
    """
    assert_bindings(
        schema="msData/particles/particlesEc024.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc024.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec023_particles_ec023_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=choice (a|b), and the instant
    XML has (b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc023.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc023.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec022_particles_ec022_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=choice (a|b), and the instant
    XML has (a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc022.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc022.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec021_particles_ec021_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=choice (a|b), and the instant
    XML has (b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc021.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc021.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec020_particles_ec020_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=choice (a|b), and the instant
    XML has (b,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc020.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc020.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec019_particles_ec019_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=choice (a|b), and the instant
    XML has (a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc019.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc019.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec018_particles_ec018_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=choice (a|b), and the instant
    XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc018.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec017_particles_ec017_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=choice (a|b), and the instant
    XML has (b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc017.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec016_particles_ec016_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=choice (a|b), and the instant
    XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc016.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc016.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec015_particles_ec015_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=choice (a|b), and the instant
    XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesEc015.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc015.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec014_particles_ec014_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=choice (a|b), and the instant
    XML has ( x )
    """
    assert_bindings(
        schema="msData/particles/particlesEc014.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc014.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec013_particles_ec013_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=choice (a|b), and the instant
    XML has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc013.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc013.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec012_particles_ec012_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=choice (a|b), and the instant
    XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc012.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc012.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec011_particles_ec011_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=choice (a|b), and the instant
    XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesEc011.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc011.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec008_particles_ec008_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=choice (a|b), and the instant XML has ( x )
    """
    assert_bindings(
        schema="msData/particles/particlesEc008.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec007_particles_ec007_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=choice (a|b), and the instant XML has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc007.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc007.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec006_particles_ec006_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=choice (a|b), and the instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc006.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec005_particles_ec005_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=choice (a|b), and the instant XML has no
    element
    """
    assert_bindings(
        schema="msData/particles/particlesEc005.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec004_particles_ec004_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=0,
    maxOccurs=absent, content=choice (a|b), and the instant XML has ( x)
    """
    assert_bindings(
        schema="msData/particles/particlesEc004.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc004.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec003_particles_ec003_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=0,
    maxOccurs=absent, content=choice (a|b), and the instant XML has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesEc003.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec002_particles_ec002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=0,
    maxOccurs=absent, content=choice (a|b), and the instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEc002.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ec001_particles_ec001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=0,
    maxOccurs=absent, content=choice (a|b), and the instant XML has no
    element
    """
    assert_bindings(
        schema="msData/particles/particlesEc001.xsd",
        is_valid=True,
        instance="msData/particles/particlesEc001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_eb041_particles_eb041_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : Valid restriction of a content model from within
    the content model
    """
    assert_bindings(
        schema="msData/particles/particlesEb041.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb041.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_particles_eb039_particles_eb039_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=sequence (a,b), and the instant XML has (x)
    """
    assert_bindings(
        schema="msData/particles/particlesEb039.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb039.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_eb038_particles_eb038_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=sequence (a,b), and the instant XML has
    (a,b,a,b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb038.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb038.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb037_particles_eb037_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=sequence (a,b), and the instant XML has
    (a,b,a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb037.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb037.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_eb036_particles_eb036_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=sequence (a,b), and the instant XML has (a,b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb036.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb036.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb035_particles_eb035_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=sequence (a,b), and the instant XML has (a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb035.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb035.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb034_particles_eb034_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=sequence (a,b), and the instant XML has (b,a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb034.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb034.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb033_particles_eb033_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=sequence (a,b), and the instant XML has (a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb033.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb033.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb032_particles_eb032_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=2,
    maxOccurs=4, content=sequence (a,b), and the instant XML has no
    element
    """
    assert_bindings(
        schema="msData/particles/particlesEb032.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb032.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb031_particles_eb031_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=sequence (a,b), and the instant
    XML has ( x )
    """
    assert_bindings(
        schema="msData/particles/particlesEb031.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb031.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb030_particles_eb030_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=sequence (a,b), and the instant
    XML has (a,b,a,b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb030.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb030.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb029_particles_eb029_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=sequence (a,b), and the instant
    XML has (a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb029.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb029.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb028_particles_eb028_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=sequence (a,b), and the instant
    XML has (b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb028.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb028.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb027_particles_eb027_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=sequence (a,b), and the instant
    XML has (a,b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb027.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb027.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb026_particles_eb026_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=sequence (a,b), and the instant
    XML has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb026.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb026.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb025_particles_eb025_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=sequence (a,b), and the instant
    XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb025.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb025.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb024_particles_eb024_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=2, content=sequence (a,b), and the instant
    XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesEb024.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb024.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb023_particles_eb023_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=sequence (a,b), and the instant
    XML has ( x )
    """
    assert_bindings(
        schema="msData/particles/particlesEb023.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb023.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb022_particles_eb022_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=sequence (a,b), and the instant
    XML has (a,b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb022.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb022.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb021_particles_eb021_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=sequence (a,b), and the instant
    XML has (a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb021.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb021.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb020_particles_eb020_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=sequence (a,b), and the instant
    XML has (b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb020.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb020.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb019_particles_eb019_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=sequence (a,b), and the instant
    XML has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb019.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb019.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb018_particles_eb018_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=sequence (a,b), and the instant
    XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb018.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb018.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb017_particles_eb017_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=sequence (a,b), and the instant
    XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesEb017.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb017.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb014_particles_eb014_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has ( x
    )
    """
    assert_bindings(
        schema="msData/particles/particlesEb014.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb014.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb013_particles_eb013_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has
    (a,b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb013.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb013.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb012_particles_eb012_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has
    (a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb012.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb012.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb011_particles_eb011_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has
    (b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb011.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb011.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb010_particles_eb010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has (a,
    b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb010.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb009_particles_eb009_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb009.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb009.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb008_particles_eb008_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has no
    element
    """
    assert_bindings(
        schema="msData/particles/particlesEb008.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb007_particles_eb007_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=0,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has ( x)
    """
    assert_bindings(
        schema="msData/particles/particlesEb007.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb007.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb006_particles_eb006_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=0,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has
    (a,b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb006.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb005_particles_eb005_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=0,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has
    (a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb005.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb004_particles_eb004_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=0,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has
    (b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb004.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb004.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb003_particles_eb003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=0,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has (a,
    b)
    """
    assert_bindings(
        schema="msData/particles/particlesEb003.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb002_particles_eb002_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=0,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEb002.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb002.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_eb001_particles_eb001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=0,
    maxOccurs=absent, content=sequence (a,b), and the instant XML has no
    element
    """
    assert_bindings(
        schema="msData/particles/particlesEb001.xsd",
        is_valid=True,
        instance="msData/particles/particlesEb001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea021_particles_ea021_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=all (a,b), and the instant XML
    has ( x)
    """
    assert_bindings(
        schema="msData/particles/particlesEa021.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa021.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea020_particles_ea020_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=all (a,b), and the instant XML
    has (a,b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEa020.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa020.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea019_particles_ea019_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=all (a,b), and the instant XML
    has (a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEa019.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa019.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea018_particles_ea018_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=all (a,b), and the instant XML
    has (b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEa018.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea017_particles_ea017_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=all (a,b), and the instant XML
    has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesEa017.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea016_particles_ea016_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=all (a,b), and the instant XML
    has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEa016.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa016.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea015_particles_ea015_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=1, content=all (a,b), and the instant XML
    has no element
    """
    assert_bindings(
        schema="msData/particles/particlesEa015.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa015.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea014_particles_ea014_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=all (a,b), and the instant XML has ( x)
    """
    assert_bindings(
        schema="msData/particles/particlesEa014.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa014.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea013_particles_ea013_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=all (a,b), and the instant XML has (a,b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEa013.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa013.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea012_particles_ea012_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=all (a,b), and the instant XML has (a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEa012.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa012.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea011_particles_ea011_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=all (a,b), and the instant XML has (b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEa011.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea010_particles_ea010_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=all (a,b), and the instant XML has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesEa010.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa010.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea009_particles_ea009_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=all (a,b), and the instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEa009.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa009.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea008_particles_ea008_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with minOccurs=1,
    maxOccurs=absent, content=all (a,b), and the instant XML has no
    element
    """
    assert_bindings(
        schema="msData/particles/particlesEa008.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea007_particles_ea007_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=absent, content=all (a,b), and the instant
    XML has ( x)
    """
    assert_bindings(
        schema="msData/particles/particlesEa007.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa007.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea006_particles_ea006_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=absent, content=all (a,b), and the instant
    XML has (a,b,a,b)
    """
    assert_bindings(
        schema="msData/particles/particlesEa006.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea005_particles_ea005_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=absent, content=all (a,b), and the instant
    XML has (a,b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEa005.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea004_particles_ea004_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=absent, content=all (a,b), and the instant
    XML has (b,a)
    """
    assert_bindings(
        schema="msData/particles/particlesEa004.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea003_particles_ea003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=absent, content=all (a,b), and the instant
    XML has (a, b)
    """
    assert_bindings(
        schema="msData/particles/particlesEa003.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea002_particles_ea002_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=absent, content=all (a,b), and the instant
    XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesEa002.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa002.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_ea001_particles_ea001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model group with
    minOccurs=absent, maxOccurs=absent, content=all (a,b) with
    minOccurs="0", and the instant XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesEa001.xsd",
        is_valid=True,
        instance="msData/particles/particlesEa001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_dc009_particles_dc009_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=TRUE, block =extension substitution restriction, instant
    element name resolved to element declared as a valid substitution
    group
    """
    assert_bindings(
        schema="msData/particles/particlesDc009.xsd",
        is_valid=True,
        instance="msData/particles/particlesDc009.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_dc008_particles_dc008_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=TRUE, block =restriction substitution, instant element name
    resolved to element declared as a valid substitution group
    """
    assert_bindings(
        schema="msData/particles/particlesDc008.xsd",
        is_valid=True,
        instance="msData/particles/particlesDc008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_dc007_particles_dc007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=TRUE, block =extension restriction, instant element name
    resolved to element declared as a valid substitution group
    """
    assert_bindings(
        schema="msData/particles/particlesDc007.xsd",
        is_valid=True,
        instance="msData/particles/particlesDc007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_dc006_particles_dc006_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=TRUE, block =extension substitution, instant element name
    resolved to element declared as a valid substitution group
    """
    assert_bindings(
        schema="msData/particles/particlesDc006.xsd",
        is_valid=True,
        instance="msData/particles/particlesDc006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_dc005_particles_dc005_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=TRUE, block =#all, instant element name resolved to element
    declared as a valid substitution group
    """
    assert_bindings(
        schema="msData/particles/particlesDc005.xsd",
        is_valid=True,
        instance="msData/particles/particlesDc005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_dc004_particles_dc004_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=TRUE, block =substitution', instant element name resolved to
    element declared as a valid substitution group
    """
    assert_bindings(
        schema="msData/particles/particlesDc004.xsd",
        is_valid=True,
        instance="msData/particles/particlesDc004.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_dc003_particles_dc003_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=TRUE, block =restriction, instant element name resolved to
    element declared as a valid substitution group
    """
    assert_bindings(
        schema="msData/particles/particlesDc003.xsd",
        is_valid=True,
        instance="msData/particles/particlesDc003.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_dc002_particles_dc002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=TRUE, block =extension, instant element name resolved to
    element declared as a valid substitution group
    """
    assert_bindings(
        schema="msData/particles/particlesDc002.xsd",
        is_valid=True,
        instance="msData/particles/particlesDc002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_dc001_particles_dc001_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=FALSE, block =absent, instant element name resolved to
    element declared as a valid substitution group
    """
    assert_bindings(
        schema="msData/particles/particlesDc001.xsd",
        is_valid=True,
        instance="msData/particles/particlesDc001.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_db011_particles_db011_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=TRUE, instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesDb011.xsd",
        is_valid=True,
        instance="msData/particles/particlesDb011.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_db010_particles_db010_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=FALSE, instant element's namespace is 'targetNamespace', the
    local name is not the same
    """
    assert_bindings(
        schema="msData/particles/particlesDb010.xsd",
        is_valid=True,
        instance="msData/particles/particlesDb010.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_db009_particles_db009_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=FALSE, instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesDb009.xsd",
        is_valid=True,
        instance="msData/particles/particlesDb009.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_db008_particles_db008_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=FALSE, instant element's namespace is unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesDb008.xsd",
        is_valid=True,
        instance="msData/particles/particlesDb008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_db007_particles_db007_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=FALSE, instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesDb007.xsd",
        is_valid=True,
        instance="msData/particles/particlesDb007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_particles_db006_particles_db006_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=FALSE, instant element's namespace is targetNamespace of an
    imported XSD which is different from the main xsd's targetNS
    """
    assert_bindings(
        schema="msData/particles/particlesDb006.xsd",
        is_valid=True,
        instance="msData/particles/particlesDb006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_db005_particles_db005_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=absent, instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesDb005.xsd",
        is_valid=True,
        instance="msData/particles/particlesDb005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_db004_particles_db004_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=absent, instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesDb004.xsd",
        is_valid=True,
        instance="msData/particles/particlesDb004.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_db003_particles_db003_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=absent, instant element's namespace is unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesDb003.xsd",
        is_valid=True,
        instance="msData/particles/particlesDb003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_db002_particles_db002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=absent, instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesDb002.xsd",
        is_valid=True,
        instance="msData/particles/particlesDb002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_db001_particles_db001_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=global,
    abstract=absent, instant element's namespace is targetNamespace of an
    imported XSD which is different from the main xsd's targetNS
    """
    assert_bindings(
        schema="msData/particles/particlesDb001.xsd",
        is_valid=True,
        instance="msData/particles/particlesDb001.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_da005_particles_da005_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=local,
    abstract=absent, instant element's namespace is 'targetNamespace', the
    local name is not the same
    """
    assert_bindings(
        schema="msData/particles/particlesDa005.xsd",
        is_valid=True,
        instance="msData/particles/particlesDa005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_da004_particles_da004_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=local,
    abstract=absent, instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesDa004.xsd",
        is_valid=True,
        instance="msData/particles/particlesDa004.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_da003_particles_da003_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=local,
    abstract=absent, instant element's namespace is unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesDa003.xsd",
        is_valid=True,
        instance="msData/particles/particlesDa003.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_particles_da002_particles_da002_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=local,
    abstract=absent, instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesDa002.xsd",
        is_valid=True,
        instance="msData/particles/particlesDa002.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_da001_particles_da001_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'element' with scope=local,
    abstract=absent, instant element's namespace is targetNamespace of an
    imported XSD which is different from the main xsd's targetNS
    """
    assert_bindings(
        schema="msData/particles/particlesDa001.xsd",
        is_valid=True,
        instance="msData/particles/particlesDa001.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c048_particles_c048_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo
    ##targetNamespace bar ##local', instant element's namespace is 'xyz'
    """
    assert_bindings(
        schema="msData/particles/particlesC048.xsd",
        is_valid=True,
        instance="msData/particles/particlesC048.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c047_particles_c047_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo
    ##targetNamespace bar ##local', instant element's namespace is
    targetNamespace of an imported XSD which is different from the main
    xsd's targetNS
    """
    assert_bindings(
        schema="msData/particles/particlesC047.xsd",
        is_valid=True,
        instance="msData/particles/particlesC047.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c046_particles_c046_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo
    ##targetNamespace bar ##local', instant element's namespace is
    'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesC046.xsd",
        is_valid=True,
        instance="msData/particles/particlesC046.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c045_particles_c045_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo
    ##targetNamespace bar ##local', instant element's namespace is
    unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesC045.xsd",
        is_valid=True,
        instance="msData/particles/particlesC045.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c044_particles_c044_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo
    ##targetNamespace bar ##local', instant element's namespace is 'bar'
    """
    assert_bindings(
        schema="msData/particles/particlesC044.xsd",
        is_valid=True,
        instance="msData/particles/particlesC044.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c043_particles_c043_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo
    ##targetNamespace bar ##local', instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesC043.xsd",
        is_valid=True,
        instance="msData/particles/particlesC043.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c042_particles_c042_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    '##targetNamespace ##local', instant element's namespace is
    targetNamespace of an imported XSD which is different from the main
    xsd's targetNS
    """
    assert_bindings(
        schema="msData/particles/particlesC042.xsd",
        is_valid=True,
        instance="msData/particles/particlesC042.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c041_particles_c041_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    '##targetNamespace ##local', instant element's namespace is
    unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesC041.xsd",
        is_valid=True,
        instance="msData/particles/particlesC041.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c040_particles_c040_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    '##targetNamespace ##local', instant element's namespace is
    'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesC040.xsd",
        is_valid=True,
        instance="msData/particles/particlesC040.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c039_particles_c039_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    '##targetNamespace ##local', instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesC039.xsd",
        is_valid=True,
        instance="msData/particles/particlesC039.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c038_particles_c038_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo
    ##local', instant element's namespace is targetNamespace of an
    imported XSD which is different from the main xsd's targetNS
    """
    assert_bindings(
        schema="msData/particles/particlesC038.xsd",
        is_valid=True,
        instance="msData/particles/particlesC038.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c037_particles_c037_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo
    ##local', instant element's namespace is unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesC037.xsd",
        is_valid=True,
        instance="msData/particles/particlesC037.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c036_particles_c036_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo
    ##local', instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesC036.xsd",
        is_valid=True,
        instance="msData/particles/particlesC036.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c035_particles_c035_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo
    ##local', instant element's namespace is 'bar'
    """
    assert_bindings(
        schema="msData/particles/particlesC035.xsd",
        is_valid=True,
        instance="msData/particles/particlesC035.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c034_particles_c034_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo
    ##local', instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesC034.xsd",
        is_valid=True,
        instance="msData/particles/particlesC034.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c033_particles_c033_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo bar
    ##targetNamespace', instant element's namespace is targetNamespace of
    an imported XSD which is different from the main xsd's targetNS
    """
    assert_bindings(
        schema="msData/particles/particlesC033.xsd",
        is_valid=True,
        instance="msData/particles/particlesC033.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c032_particles_c032_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo bar
    ##targetNamespace', instant element's namespace is unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesC032.xsd",
        is_valid=True,
        instance="msData/particles/particlesC032.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c031_particles_c031_i():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo bar
    ##targetNamespace', instant element's namespace is 'xyz'
    """
    assert_bindings(
        schema="msData/particles/particlesC031.xsd",
        is_valid=True,
        instance="msData/particles/particlesC031.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles_c030_particles_c030_v():
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo bar
    ##targetNamespace', instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesC030.xsd",
        is_valid=True,
        instance="msData/particles/particlesC030.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )
