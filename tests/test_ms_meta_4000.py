import pytest

from tests.utils import assert_bindings


def test_particles_c029_particles_c029_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo bar
    ##targetNamespace', instant element's namespace is 'bar'
    """
    assert_bindings(
        schema="msData/particles/particlesC029.xsd",
        instance="msData/particles/particlesC029.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c028_particles_c028_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo bar
    ##targetNamespace', instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesC028.xsd",
        instance="msData/particles/particlesC028.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c027_particles_c027_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= ##local,
    instant element's namespace is unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesC027.xsd",
        instance="msData/particles/particlesC027.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c026_particles_c026_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= ##local,
    instant element's namespace is targetNamespace of an imported XSD
    which is different from the main xsd's targetNS
    """
    assert_bindings(
        schema="msData/particles/particlesC026.xsd",
        instance="msData/particles/particlesC026.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c025_particles_c025_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= ##local,
    instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesC025.xsd",
        instance="msData/particles/particlesC025.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c024_particles_c024_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= ##local,
    instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesC024.xsd",
        instance="msData/particles/particlesC024.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c023_particles_c023_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    ##targetNamespace, instant element's namespace is unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesC023.xsd",
        instance="msData/particles/particlesC023.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c022_particles_c022_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    ##targetNamespace, instant element's namespace is targetNamespace of
    an imported XSD which is different from the main xsd's targetNS
    """
    assert_bindings(
        schema="msData/particles/particlesC022.xsd",
        instance="msData/particles/particlesC022.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c021_particles_c021_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    ##targetNamespace, instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesC021.xsd",
        instance="msData/particles/particlesC021.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c020_particles_c020_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    ##targetNamespace, instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesC020.xsd",
        instance="msData/particles/particlesC020.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c019_particles_c019_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo bar',
    instant element's namespace is 'xyz'
    """
    assert_bindings(
        schema="msData/particles/particlesC019.xsd",
        instance="msData/particles/particlesC019.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c018_particles_c018_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo bar',
    instant element's namespace is unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesC018.xsd",
        instance="msData/particles/particlesC018.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c017_particles_c017_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo bar',
    instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesC017.xsd",
        instance="msData/particles/particlesC017.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c016_particles_c016_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo bar',
    instant element's namespace is 'bar'
    """
    assert_bindings(
        schema="msData/particles/particlesC016.xsd",
        instance="msData/particles/particlesC016.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c015_particles_c015_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace= 'foo bar',
    instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesC015.xsd",
        instance="msData/particles/particlesC015.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c014_particles_c014_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    'http://xslt', instant element's namespace is unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesC014.xsd",
        instance="msData/particles/particlesC014.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c013_particles_c013_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    'http://xslt', instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesC013.xsd",
        instance="msData/particles/particlesC013.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c012_particles_c012_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    'http://xslt', instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesC012.xsd",
        instance="msData/particles/particlesC012.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c011_particles_c011_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=
    'http://xslt', instant element's namespace is 'http://xslt'
    """
    assert_bindings(
        schema="msData/particles/particlesC011.xsd",
        instance="msData/particles/particlesC011.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c010_particles_c010_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=##other,
    instant element's namespace is targetNamespace of an imported XSD
    which is different from the main xsd's targetNS, it is invalid because
    local instance violate ##other.
    """
    assert_bindings(
        schema="msData/particles/particlesC010.xsd",
        instance="msData/particles/particlesC010.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c009_particles_c009_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=##other,
    instant element's namespace is unqualified. Note: ##other mean NOT
    ##targetNamespace or ##local, therefore unqualified names which fall
    under ##local will be a violation of the namespace=##other.
    """
    assert_bindings(
        schema="msData/particles/particlesC009.xsd",
        instance="msData/particles/particlesC009.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c008_particles_c008_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=##other,
    instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesC008.xsd",
        instance="msData/particles/particlesC008.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_c007_particles_c007_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=##other,
    instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesC007.xsd",
        instance="msData/particles/particlesC007.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c006_particles_c006_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=##any,
    instant element's namespace is unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesC006.xsd",
        instance="msData/particles/particlesC006.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c005_particles_c005_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=##any,
    instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesC005.xsd",
        instance="msData/particles/particlesC005.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c004_particles_c004_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=##any,
    instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesC004.xsd",
        instance="msData/particles/particlesC004.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c003_particles_c003_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=absent
    (default to ##any), instant element's namespace is unqualified
    """
    assert_bindings(
        schema="msData/particles/particlesC003.xsd",
        instance="msData/particles/particlesC003.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c002_particles_c002_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=absent
    (default to ##any), instant element's namespace is 'targetNamespace'
    """
    assert_bindings(
        schema="msData/particles/particlesC002.xsd",
        instance="msData/particles/particlesC002.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_c001_particles_c001_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with namespace=absent
    (default to ##any), instant element's namespace is 'foo'
    """
    assert_bindings(
        schema="msData/particles/particlesC001.xsd",
        instance="msData/particles/particlesC001.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_b015_particles_b015_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    maxOccurs=2, instant XML has (a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesB015.xsd",
        instance="msData/particles/particlesB015.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_b014_particles_b014_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    maxOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesB014.xsd",
        instance="msData/particles/particlesB014.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_b013_particles_b013_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    maxOccurs=2, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesB013.xsd",
        instance="msData/particles/particlesB013.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_b012_particles_b012_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    maxOccurs=2, instant XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesB012.xsd",
        instance="msData/particles/particlesB012.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_b011_particles_b011_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), maxOccurs=2, instant XML has (a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesB011.xsd",
        instance="msData/particles/particlesB011.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_b010_particles_b010_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), maxOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesB010.xsd",
        instance="msData/particles/particlesB010.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_b009_particles_b009_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), maxOccurs=2, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesB009.xsd",
        instance="msData/particles/particlesB009.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_b008_particles_b008_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), maxOccurs=2, instant XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesB008.xsd",
        instance="msData/particles/particlesB008.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_b007_particles_b007_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), maxOccurs=2, instant XML has (a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesB007.xsd",
        instance="msData/particles/particlesB007.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_b006_particles_b006_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), maxOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesB006.xsd",
        instance="msData/particles/particlesB006.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_b005_particles_b005_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), maxOccurs=2, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesB005.xsd",
        instance="msData/particles/particlesB005.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_b004_particles_b004_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), maxOccurs=2, instant XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesB004.xsd",
        instance="msData/particles/particlesB004.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_b003_particles_b003_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'all' with child
    content=(a), maxOccurs=1, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesB003.xsd",
        instance="msData/particles/particlesB003.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_b002_particles_b002_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'all' with child
    content=(a), maxOccurs=1, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesB002.xsd",
        instance="msData/particles/particlesB002.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_b001_particles_b001_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'all' with child
    content=(a), maxOccurs=1, instant XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesB001.xsd",
        instance="msData/particles/particlesB001.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_a015_particles_a015_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    minOccurs=2, instant XML has (a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA015.xsd",
        instance="msData/particles/particlesA015.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_a014_particles_a014_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    minOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA014.xsd",
        instance="msData/particles/particlesA014.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_a013_particles_a013_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    minOccurs=2, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesA013.xsd",
        instance="msData/particles/particlesA013.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_a012_particles_a012_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is 'any' with child content=(a),
    minOccurs=2, instant XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesA012.xsd",
        instance="msData/particles/particlesA012.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_a011_particles_a011_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), minOccurs=2, instant XML has (a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA011.xsd",
        instance="msData/particles/particlesA011.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_a010_particles_a010_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), minOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA010.xsd",
        instance="msData/particles/particlesA010.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_a009_particles_a009_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), minOccurs=2, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesA009.xsd",
        instance="msData/particles/particlesA009.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_a008_particles_a008_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'choice' with child
    content=(a), minOccurs=2, instant XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesA008.xsd",
        instance="msData/particles/particlesA008.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_a007_particles_a007_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), minOccurs=2, instant XML has (a,a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA007.xsd",
        instance="msData/particles/particlesA007.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_a006_particles_a006_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), minOccurs=2, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA006.xsd",
        instance="msData/particles/particlesA006.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_a005_particles_a005_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), minOccurs=2, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesA005.xsd",
        instance="msData/particles/particlesA005.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_a004_particles_a004_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'sequence' with child
    content=(a), minOccurs=2, instant XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesA004.xsd",
        instance="msData/particles/particlesA004.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_a003_particles_a003_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'all' with child
    content=(a), minOccurs=1, instant XML has (a,a)
    """
    assert_bindings(
        schema="msData/particles/particlesA003.xsd",
        instance="msData/particles/particlesA003.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_particles_a002_particles_a002_v(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'all' with child
    content=(a), minOccurs=1, instant XML has (a)
    """
    assert_bindings(
        schema="msData/particles/particlesA002.xsd",
        instance="msData/particles/particlesA002.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_particles_a001_particles_a001_i(mode, save_output):
    """
    TEST :3.9.1 The Particle Schema Component [ check length of element
    information items ] : The {term} is a model 'all' with child
    content=(a), minOccurs=1, instant XML has no element
    """
    assert_bindings(
        schema="msData/particles/particlesA001.xsd",
        instance="msData/particles/particlesA001.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_z006i_re_z006i_i(mode, save_output):
    r"""
    TEST :branch : Invalid characeter mappings from character sequence \c
    """
    assert_bindings(
        schema="msData/regex/schema_c.xsd",
        instance="msData/regex/invalid.c.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_z006v_re_z006v_v(mode, save_output):
    r"""
    TEST :branch : Valid characeter mappings from character sequence \c
    """
    assert_bindings(
        schema="msData/regex/schema_c.xsd",
        instance="msData/regex/valid.c.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_z005i_re_z005i_i(mode, save_output):
    r"""
    TEST :branch : Invalid characeter mappings from character sequence \i
    """
    assert_bindings(
        schema="msData/regex/schema_i.xsd",
        instance="msData/regex/invalid.i.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_z005v_re_z005v_v(mode, save_output):
    r"""
    TEST :branch : Valid characeter mappings from character sequence \i
    """
    assert_bindings(
        schema="msData/regex/schema_i.xsd",
        instance="msData/regex/valid.i.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_z004i_re_z004i_i(mode, save_output):
    r"""
    TEST :branch : Invalid characeter mappings from character sequence \d
    """
    assert_bindings(
        schema="msData/regex/schema_d.xsd",
        instance="msData/regex/invalid.d.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_z004v_re_z004v_v(mode, save_output):
    r"""
    TEST :branch : Valid characeter mappings from character sequence \d
    """
    assert_bindings(
        schema="msData/regex/schema_d.xsd",
        instance="msData/regex/valid.d.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_z003v_re_z003v_v(mode, save_output):
    r"""
    TEST :branch : Valid characeter mappings from character sequence \w
    """
    assert_bindings(
        schema="msData/regex/reZ003.xsd",
        instance="msData/regex/reZ003v.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_z002_re_z002_i(mode, save_output):
    """
    TEST :branch : 381386 : character class escape whack w in pattern
    facet matches Low Line
    """
    assert_bindings(
        schema="msData/regex/reZ002.xsd",
        instance="msData/regex/reZ002.xml",
        class_name="Document",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_z001_re_z001_v(mode, save_output):
    """
    TEST :branch : XSD: an email regex pattern takes more than one minute
    to validate HST agrees this one doesn't match
    """
    assert_bindings(
        schema="msData/regex/reZ001.xsd",
        instance="msData/regex/reZ001.xml",
        class_name="Email",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_specials_specials_v(mode, save_output):
    """
    TEST :branch : Specials
    """
    assert_bindings(
        schema="msData/regex/Specials.xsd",
        instance="msData/regex/Specials.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_halfwidthand_fullwidth_forms_halfwidthand_fullwidth_forms_v(mode, save_output):
    """
    TEST :branch : HalfwidthandFullwidthForms
    """
    assert_bindings(
        schema="msData/regex/HalfwidthandFullwidthForms.xsd",
        instance="msData/regex/HalfwidthandFullwidthForms.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_small_form_variants_small_form_variants_v(mode, save_output):
    """
    TEST :branch : SmallFormVariants
    """
    assert_bindings(
        schema="msData/regex/SmallFormVariants.xsd",
        instance="msData/regex/SmallFormVariants.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_cjkcompatibility_forms_cjkcompatibility_forms_v(mode, save_output):
    """
    TEST :branch : CJKCompatibilityForms
    """
    assert_bindings(
        schema="msData/regex/CJKCompatibilityForms.xsd",
        instance="msData/regex/CJKCompatibilityForms.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_combining_half_marks_combining_half_marks_v(mode, save_output):
    """
    TEST :branch : CombiningHalfMarks
    """
    assert_bindings(
        schema="msData/regex/CombiningHalfMarks.xsd",
        instance="msData/regex/CombiningHalfMarks.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_arabic_presentation_forms_a_arabic_presentation_forms_a_v(mode, save_output):
    """
    TEST :branch : ArabicPresentationForms-A
    """
    assert_bindings(
        schema="msData/regex/ArabicPresentationForms-A.xsd",
        instance="msData/regex/ArabicPresentationForms-A.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_alphabetic_presentation_forms_alphabetic_presentation_forms_v(mode, save_output):
    """
    TEST :branch : AlphabeticPresentationForms
    """
    assert_bindings(
        schema="msData/regex/AlphabeticPresentationForms.xsd",
        instance="msData/regex/AlphabeticPresentationForms.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_cjkcompatibility_ideographs_cjkcompatibility_ideographs_v(mode, save_output):
    """
    TEST :branch : CJKCompatibilityIdeographs
    """
    assert_bindings(
        schema="msData/regex/CJKCompatibilityIdeographs.xsd",
        instance="msData/regex/CJKCompatibilityIdeographs.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_high_surrogates_high_surrogates_i(mode, save_output):
    """
    TEST :branch : HighSurrogates
    """
    assert_bindings(
        schema="msData/regex/HighSurrogates.xsd",
        instance="msData/regex/HighSurrogates.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_yi_radicals_yi_radicals_v(mode, save_output):
    """
    TEST :branch : YiRadicals
    """
    assert_bindings(
        schema="msData/regex/YiRadicals.xsd",
        instance="msData/regex/YiRadicals.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_yi_syllables_yi_syllables_v(mode, save_output):
    """
    TEST :branch : YiSyllables
    """
    assert_bindings(
        schema="msData/regex/YiSyllables.xsd",
        instance="msData/regex/YiSyllables.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_cjkunified_ideographs_cjkunified_ideographs_v(mode, save_output):
    """
    TEST :branch : CJKUnifiedIdeographs
    """
    assert_bindings(
        schema="msData/regex/CJKUnifiedIdeographs.xsd",
        instance="msData/regex/CJKUnifiedIdeographs.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_cjkcompatibility_cjkcompatibility_v(mode, save_output):
    """
    TEST :branch : CJKCompatibility
    """
    assert_bindings(
        schema="msData/regex/CJKCompatibility.xsd",
        instance="msData/regex/CJKCompatibility.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_enclosed_cjklettersand_months_enclosed_cjklettersand_months_v(mode, save_output):
    """
    TEST :branch : EnclosedCJKLettersandMonths
    """
    assert_bindings(
        schema="msData/regex/EnclosedCJKLettersandMonths.xsd",
        instance="msData/regex/EnclosedCJKLettersandMonths.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_bopomofo_extended_bopomofo_extended_v(mode, save_output):
    """
    TEST :branch : BopomofoExtended
    """
    assert_bindings(
        schema="msData/regex/BopomofoExtended.xsd",
        instance="msData/regex/BopomofoExtended.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_kanbun_kanbun_v(mode, save_output):
    """
    TEST :branch : Kanbun
    """
    assert_bindings(
        schema="msData/regex/Kanbun.xsd",
        instance="msData/regex/Kanbun.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_hangul_compatibility_jamo_hangul_compatibility_jamo_v(mode, save_output):
    """
    TEST :branch : HangulCompatibilityJamo
    """
    assert_bindings(
        schema="msData/regex/HangulCompatibilityJamo.xsd",
        instance="msData/regex/HangulCompatibilityJamo.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_bopomofo_bopomofo_v(mode, save_output):
    """
    TEST :branch : Bopomofo
    """
    assert_bindings(
        schema="msData/regex/Bopomofo.xsd",
        instance="msData/regex/Bopomofo.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_katakana_katakana_v(mode, save_output):
    """
    TEST :branch : Katakana
    """
    assert_bindings(
        schema="msData/regex/Katakana.xsd",
        instance="msData/regex/Katakana.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_hiragana_hiragana_v(mode, save_output):
    """
    TEST :branch : Hiragana
    """
    assert_bindings(
        schema="msData/regex/Hiragana.xsd",
        instance="msData/regex/Hiragana.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_cjksymbolsand_punctuation_cjksymbolsand_punctuation_v(mode, save_output):
    """
    TEST :branch : CJKSymbolsandPunctuation
    """
    assert_bindings(
        schema="msData/regex/CJKSymbolsandPunctuation.xsd",
        instance="msData/regex/CJKSymbolsandPunctuation.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_ideographic_description_characters_ideographic_description_characters_v(mode, save_output):
    """
    TEST :branch : IdeographicDescriptionCharacters
    """
    assert_bindings(
        schema="msData/regex/IdeographicDescriptionCharacters.xsd",
        instance="msData/regex/IdeographicDescriptionCharacters.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_kangxi_radicals_kangxi_radicals_v(mode, save_output):
    """
    TEST :branch : KangxiRadicals
    """
    assert_bindings(
        schema="msData/regex/KangxiRadicals.xsd",
        instance="msData/regex/KangxiRadicals.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_cjkradicals_supplement_cjkradicals_supplement_v(mode, save_output):
    """
    TEST :branch : CJKRadicalsSupplement
    """
    assert_bindings(
        schema="msData/regex/CJKRadicalsSupplement.xsd",
        instance="msData/regex/CJKRadicalsSupplement.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_braille_patterns_braille_patterns_v(mode, save_output):
    """
    TEST :branch : BraillePatterns
    """
    assert_bindings(
        schema="msData/regex/BraillePatterns.xsd",
        instance="msData/regex/BraillePatterns.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_dingbats_dingbats_v(mode, save_output):
    """
    TEST :branch : Dingbats
    """
    assert_bindings(
        schema="msData/regex/Dingbats.xsd",
        instance="msData/regex/Dingbats.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_miscellaneous_symbols_miscellaneous_symbols_v(mode, save_output):
    """
    TEST :branch : MiscellaneousSymbols
    """
    assert_bindings(
        schema="msData/regex/MiscellaneousSymbols.xsd",
        instance="msData/regex/MiscellaneousSymbols.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_geometric_shapes_geometric_shapes_v(mode, save_output):
    """
    TEST :branch : GeometricShapes
    """
    assert_bindings(
        schema="msData/regex/GeometricShapes.xsd",
        instance="msData/regex/GeometricShapes.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_block_elements_block_elements_v(mode, save_output):
    """
    TEST :branch : BlockElements
    """
    assert_bindings(
        schema="msData/regex/BlockElements.xsd",
        instance="msData/regex/BlockElements.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_box_drawing_box_drawing_v(mode, save_output):
    """
    TEST :branch : BoxDrawing
    """
    assert_bindings(
        schema="msData/regex/BoxDrawing.xsd",
        instance="msData/regex/BoxDrawing.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_enclosed_alphanumerics_enclosed_alphanumerics_v(mode, save_output):
    """
    TEST :branch : EnclosedAlphanumerics
    """
    assert_bindings(
        schema="msData/regex/EnclosedAlphanumerics.xsd",
        instance="msData/regex/EnclosedAlphanumerics.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_optical_character_recognition_optical_character_recognition_v(mode, save_output):
    """
    TEST :branch : OpticalCharacterRecognition
    """
    assert_bindings(
        schema="msData/regex/OpticalCharacterRecognition.xsd",
        instance="msData/regex/OpticalCharacterRecognition.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_control_pictures_control_pictures_v(mode, save_output):
    """
    TEST :branch : ControlPictures
    """
    assert_bindings(
        schema="msData/regex/ControlPictures.xsd",
        instance="msData/regex/ControlPictures.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_miscellaneous_technical_miscellaneous_technical_v(mode, save_output):
    """
    TEST :branch : MiscellaneousTechnical
    """
    assert_bindings(
        schema="msData/regex/MiscellaneousTechnical.xsd",
        instance="msData/regex/MiscellaneousTechnical.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_mathematical_operators_mathematical_operators_v(mode, save_output):
    """
    TEST :branch : MathematicalOperators
    """
    assert_bindings(
        schema="msData/regex/MathematicalOperators.xsd",
        instance="msData/regex/MathematicalOperators.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_arrows_arrows_v(mode, save_output):
    """
    TEST :branch : Arrows
    """
    assert_bindings(
        schema="msData/regex/Arrows.xsd",
        instance="msData/regex/Arrows.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_number_forms_number_forms_v(mode, save_output):
    """
    TEST :branch : NumberForms
    """
    assert_bindings(
        schema="msData/regex/NumberForms.xsd",
        instance="msData/regex/NumberForms.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_letterlike_symbols_letterlike_symbols_v(mode, save_output):
    """
    TEST :branch : LetterlikeSymbols
    """
    assert_bindings(
        schema="msData/regex/LetterlikeSymbols.xsd",
        instance="msData/regex/LetterlikeSymbols.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_currency_symbols_currency_symbols_v(mode, save_output):
    """
    TEST :branch : CurrencySymbols
    """
    assert_bindings(
        schema="msData/regex/CurrencySymbols.xsd",
        instance="msData/regex/CurrencySymbols.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_superscriptsand_subscripts_superscriptsand_subscripts_v(mode, save_output):
    """
    TEST :branch : SuperscriptsandSubscripts
    """
    assert_bindings(
        schema="msData/regex/SuperscriptsandSubscripts.xsd",
        instance="msData/regex/SuperscriptsandSubscripts.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_general_punctuation_general_punctuation_v(mode, save_output):
    """
    TEST :branch : GeneralPunctuation
    """
    assert_bindings(
        schema="msData/regex/GeneralPunctuation.xsd",
        instance="msData/regex/GeneralPunctuation.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_greek_extended_greek_extended_v(mode, save_output):
    """
    TEST :branch : GreekExtended
    """
    assert_bindings(
        schema="msData/regex/GreekExtended.xsd",
        instance="msData/regex/GreekExtended.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_latin_extended_additional_latin_extended_additional_v(mode, save_output):
    """
    TEST :branch : LatinExtendedAdditional
    """
    assert_bindings(
        schema="msData/regex/LatinExtendedAdditional.xsd",
        instance="msData/regex/LatinExtendedAdditional.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_mongolian_mongolian_v(mode, save_output):
    """
    TEST :branch : Mongolian
    """
    assert_bindings(
        schema="msData/regex/Mongolian.xsd",
        instance="msData/regex/Mongolian.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_khmer_khmer_v(mode, save_output):
    """
    TEST :branch : Khmer
    """
    assert_bindings(
        schema="msData/regex/Khmer.xsd",
        instance="msData/regex/Khmer.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_runic_runic_v(mode, save_output):
    """
    TEST :branch : Runic
    """
    assert_bindings(
        schema="msData/regex/Runic.xsd",
        instance="msData/regex/Runic.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_ogham_ogham_v(mode, save_output):
    """
    TEST :branch : Ogham
    """
    assert_bindings(
        schema="msData/regex/Ogham.xsd",
        instance="msData/regex/Ogham.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_unified_canadian_aboriginal_syllabics_unified_canadian_aboriginal_syllabics_v(mode, save_output):
    """
    TEST :branch : UnifiedCanadianAboriginalSyllabics
    """
    assert_bindings(
        schema="msData/regex/UnifiedCanadianAboriginalSyllabics.xsd",
        instance="msData/regex/UnifiedCanadianAboriginalSyllabics.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_cherokee_cherokee_v(mode, save_output):
    """
    TEST :branch : Cherokee
    """
    assert_bindings(
        schema="msData/regex/Cherokee.xsd",
        instance="msData/regex/Cherokee.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_ethiopic_ethiopic_v(mode, save_output):
    """
    TEST :branch : Ethiopic
    """
    assert_bindings(
        schema="msData/regex/Ethiopic.xsd",
        instance="msData/regex/Ethiopic.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_hangul_jamo_hangul_jamo_v(mode, save_output):
    """
    TEST :branch : HangulJamo
    """
    assert_bindings(
        schema="msData/regex/HangulJamo.xsd",
        instance="msData/regex/HangulJamo.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_georgian_georgian_v(mode, save_output):
    """
    TEST :branch : Georgian
    """
    assert_bindings(
        schema="msData/regex/Georgian.xsd",
        instance="msData/regex/Georgian.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_myanmar_myanmar_v(mode, save_output):
    """
    TEST :branch : Myanmar
    """
    assert_bindings(
        schema="msData/regex/Myanmar.xsd",
        instance="msData/regex/Myanmar.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_tibetan_tibetan_v(mode, save_output):
    """
    TEST :branch : Tibetan
    """
    assert_bindings(
        schema="msData/regex/Tibetan.xsd",
        instance="msData/regex/Tibetan.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_lao_lao_v(mode, save_output):
    """
    TEST :branch : Lao
    """
    assert_bindings(
        schema="msData/regex/Lao.xsd",
        instance="msData/regex/Lao.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_thai_thai_v(mode, save_output):
    """
    TEST :branch : Thai
    """
    assert_bindings(
        schema="msData/regex/Thai.xsd",
        instance="msData/regex/Thai.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_sinhala_sinhala_v(mode, save_output):
    """
    TEST :branch : Sinhala
    """
    assert_bindings(
        schema="msData/regex/Sinhala.xsd",
        instance="msData/regex/Sinhala.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_malayalam_malayalam_v(mode, save_output):
    """
    TEST :branch : Malayalam
    """
    assert_bindings(
        schema="msData/regex/Malayalam.xsd",
        instance="msData/regex/Malayalam.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_kannada_kannada_v(mode, save_output):
    """
    TEST :branch : Kannada
    """
    assert_bindings(
        schema="msData/regex/Kannada.xsd",
        instance="msData/regex/Kannada.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_telugu_telugu_v(mode, save_output):
    """
    TEST :branch : Telugu
    """
    assert_bindings(
        schema="msData/regex/Telugu.xsd",
        instance="msData/regex/Telugu.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_tamil_tamil_v(mode, save_output):
    """
    TEST :branch : Tamil
    """
    assert_bindings(
        schema="msData/regex/Tamil.xsd",
        instance="msData/regex/Tamil.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_oriya_oriya_v(mode, save_output):
    """
    TEST :branch : Oriya
    """
    assert_bindings(
        schema="msData/regex/Oriya.xsd",
        instance="msData/regex/Oriya.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_gujarati_gujarati_v(mode, save_output):
    """
    TEST :branch : Gujarati
    """
    assert_bindings(
        schema="msData/regex/Gujarati.xsd",
        instance="msData/regex/Gujarati.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_gurmukhi_gurmukhi_v(mode, save_output):
    """
    TEST :branch : Gurmukhi
    """
    assert_bindings(
        schema="msData/regex/Gurmukhi.xsd",
        instance="msData/regex/Gurmukhi.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_bengali_bengali_v(mode, save_output):
    """
    TEST :branch : Bengali
    """
    assert_bindings(
        schema="msData/regex/Bengali.xsd",
        instance="msData/regex/Bengali.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_devanagari_devanagari_v(mode, save_output):
    """
    TEST :branch : Devanagari
    """
    assert_bindings(
        schema="msData/regex/Devanagari.xsd",
        instance="msData/regex/Devanagari.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_thaana_thaana_v(mode, save_output):
    """
    TEST :branch : Thaana
    """
    assert_bindings(
        schema="msData/regex/Thaana.xsd",
        instance="msData/regex/Thaana.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_syriac_syriac_v(mode, save_output):
    """
    TEST :branch : Syriac
    """
    assert_bindings(
        schema="msData/regex/Syriac.xsd",
        instance="msData/regex/Syriac.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_arabic_arabic_v(mode, save_output):
    """
    TEST :branch : Arabic
    """
    assert_bindings(
        schema="msData/regex/Arabic.xsd",
        instance="msData/regex/Arabic.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_hebrew_hebrew_v(mode, save_output):
    """
    TEST :branch : Hebrew
    """
    assert_bindings(
        schema="msData/regex/Hebrew.xsd",
        instance="msData/regex/Hebrew.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_armenian_armenian_v(mode, save_output):
    """
    TEST :branch : Armenian
    """
    assert_bindings(
        schema="msData/regex/Armenian.xsd",
        instance="msData/regex/Armenian.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_cyrillic_cyrillic_v(mode, save_output):
    """
    TEST :branch : Cyrillic
    """
    assert_bindings(
        schema="msData/regex/Cyrillic.xsd",
        instance="msData/regex/Cyrillic.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_combining_diacritical_marks_combining_diacritical_marks_v(mode, save_output):
    """
    TEST :branch : CombiningDiacriticalMarks
    """
    assert_bindings(
        schema="msData/regex/CombiningDiacriticalMarks.xsd",
        instance="msData/regex/CombiningDiacriticalMarks.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_spacing_modifier_letters_spacing_modifier_letters_v(mode, save_output):
    """
    TEST :branch : SpacingModifierLetters
    """
    assert_bindings(
        schema="msData/regex/SpacingModifierLetters.xsd",
        instance="msData/regex/SpacingModifierLetters.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_ipaextensions_ipaextensions_v(mode, save_output):
    """
    TEST :branch : IPAExtensions
    """
    assert_bindings(
        schema="msData/regex/IPAExtensions.xsd",
        instance="msData/regex/IPAExtensions.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_latin_extended_b_latin_extended_b_v(mode, save_output):
    """
    TEST :branch : LatinExtended-B
    """
    assert_bindings(
        schema="msData/regex/LatinExtended-B.xsd",
        instance="msData/regex/LatinExtended-B.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_latin_extended_a_latin_extended_a_v(mode, save_output):
    """
    TEST :branch : LatinExtended-A
    """
    assert_bindings(
        schema="msData/regex/LatinExtended-A.xsd",
        instance="msData/regex/LatinExtended-A.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_latin_1_supplement_latin_1_supplement_v(mode, save_output):
    """
    TEST :branch : Latin-1Supplement
    """
    assert_bindings(
        schema="msData/regex/Latin-1Supplement.xsd",
        instance="msData/regex/Latin-1Supplement.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_basic_latin_basic_latin_v(mode, save_output):
    """
    TEST :branch : BasicLatin
    """
    assert_bindings(
        schema="msData/regex/BasicLatin.xsd",
        instance="msData/regex/BasicLatin.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_535_regex_test_535_v(mode, save_output):
    """
    TEST :branch : RegexTest_535
    """
    assert_bindings(
        schema="msData/regex/RegexTest_535.xsd",
        instance="msData/regex/RegexTest_535.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_533_regex_test_533_i(mode, save_output):
    """
    TEST :branch : RegexTest_533
    """
    assert_bindings(
        schema="msData/regex/RegexTest_533.xsd",
        instance="msData/regex/RegexTest_533.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_532_regex_test_532_i(mode, save_output):
    """
    TEST :branch : RegexTest_532
    """
    assert_bindings(
        schema="msData/regex/RegexTest_532.xsd",
        instance="msData/regex/RegexTest_532.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_531_regex_test_531_i(mode, save_output):
    """
    TEST :branch : RegexTest_531
    """
    assert_bindings(
        schema="msData/regex/RegexTest_531.xsd",
        instance="msData/regex/RegexTest_531.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_530_regex_test_530_v(mode, save_output):
    """
    TEST :branch : RegexTest_530
    """
    assert_bindings(
        schema="msData/regex/RegexTest_530.xsd",
        instance="msData/regex/RegexTest_530.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_529_regex_test_529_i(mode, save_output):
    """
    TEST :branch : RegexTest_529
    """
    assert_bindings(
        schema="msData/regex/RegexTest_529.xsd",
        instance="msData/regex/RegexTest_529.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_528_regex_test_528_i(mode, save_output):
    """
    TEST :branch : RegexTest_528
    """
    assert_bindings(
        schema="msData/regex/RegexTest_528.xsd",
        instance="msData/regex/RegexTest_528.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_525_regex_test_525_v(mode, save_output):
    """
    TEST :branch : RegexTest_525
    """
    assert_bindings(
        schema="msData/regex/RegexTest_525.xsd",
        instance="msData/regex/RegexTest_525.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_522_regex_test_522_v(mode, save_output):
    """
    TEST :branch : RegexTest_522
    """
    assert_bindings(
        schema="msData/regex/RegexTest_522.xsd",
        instance="msData/regex/RegexTest_522.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_520_regex_test_520_i(mode, save_output):
    """
    TEST :branch : RegexTest_520
    """
    assert_bindings(
        schema="msData/regex/RegexTest_520.xsd",
        instance="msData/regex/RegexTest_520.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_515_regex_test_515_v(mode, save_output):
    """
    TEST :branch : RegexTest_515
    """
    assert_bindings(
        schema="msData/regex/RegexTest_515.xsd",
        instance="msData/regex/RegexTest_515.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_514_regex_test_514_i(mode, save_output):
    """
    TEST :branch : RegexTest_514
    """
    assert_bindings(
        schema="msData/regex/RegexTest_514.xsd",
        instance="msData/regex/RegexTest_514.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_513_regex_test_513_v(mode, save_output):
    """
    TEST :branch : RegexTest_513
    """
    assert_bindings(
        schema="msData/regex/RegexTest_513.xsd",
        instance="msData/regex/RegexTest_513.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_508_regex_test_508_i(mode, save_output):
    """
    TEST :branch : RegexTest_508
    """
    assert_bindings(
        schema="msData/regex/RegexTest_508.xsd",
        instance="msData/regex/RegexTest_508.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_506_regex_test_506_i(mode, save_output):
    """
    TEST :branch : RegexTest_506
    """
    assert_bindings(
        schema="msData/regex/RegexTest_506.xsd",
        instance="msData/regex/RegexTest_506.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_504_regex_test_504_i(mode, save_output):
    """
    TEST :branch : RegexTest_504
    """
    assert_bindings(
        schema="msData/regex/RegexTest_504.xsd",
        instance="msData/regex/RegexTest_504.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_503_regex_test_503_i(mode, save_output):
    """
    TEST :branch : RegexTest_503
    """
    assert_bindings(
        schema="msData/regex/RegexTest_503.xsd",
        instance="msData/regex/RegexTest_503.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_502_regex_test_502_i(mode, save_output):
    """
    TEST :branch : RegexTest_502
    """
    assert_bindings(
        schema="msData/regex/RegexTest_502.xsd",
        instance="msData/regex/RegexTest_502.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_501_regex_test_501_i(mode, save_output):
    """
    TEST :branch : RegexTest_501
    """
    assert_bindings(
        schema="msData/regex/RegexTest_501.xsd",
        instance="msData/regex/RegexTest_501.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_500_regex_test_500_i(mode, save_output):
    """
    TEST :branch : RegexTest_500
    """
    assert_bindings(
        schema="msData/regex/RegexTest_500.xsd",
        instance="msData/regex/RegexTest_500.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_499_regex_test_499_i(mode, save_output):
    """
    TEST :branch : RegexTest_499
    """
    assert_bindings(
        schema="msData/regex/RegexTest_499.xsd",
        instance="msData/regex/RegexTest_499.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_498_regex_test_498_i(mode, save_output):
    """
    TEST :branch : RegexTest_498
    """
    assert_bindings(
        schema="msData/regex/RegexTest_498.xsd",
        instance="msData/regex/RegexTest_498.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_497_regex_test_497_i(mode, save_output):
    """
    TEST :branch : RegexTest_497
    """
    assert_bindings(
        schema="msData/regex/RegexTest_497.xsd",
        instance="msData/regex/RegexTest_497.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_496_regex_test_496_i(mode, save_output):
    """
    TEST :branch : RegexTest_496
    """
    assert_bindings(
        schema="msData/regex/RegexTest_496.xsd",
        instance="msData/regex/RegexTest_496.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_495_regex_test_495_v(mode, save_output):
    """
    TEST :branch : RegexTest_495
    """
    assert_bindings(
        schema="msData/regex/RegexTest_495.xsd",
        instance="msData/regex/RegexTest_495.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_494_regex_test_494_i(mode, save_output):
    """
    TEST :branch : RegexTest_494
    """
    assert_bindings(
        schema="msData/regex/RegexTest_494.xsd",
        instance="msData/regex/RegexTest_494.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_493_regex_test_493_i(mode, save_output):
    """
    TEST :branch : RegexTest_493
    """
    assert_bindings(
        schema="msData/regex/RegexTest_493.xsd",
        instance="msData/regex/RegexTest_493.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_492_regex_test_492_i(mode, save_output):
    """
    TEST :branch : RegexTest_492
    """
    assert_bindings(
        schema="msData/regex/RegexTest_492.xsd",
        instance="msData/regex/RegexTest_492.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_491_regex_test_491_i(mode, save_output):
    """
    TEST :branch : RegexTest_491
    """
    assert_bindings(
        schema="msData/regex/RegexTest_491.xsd",
        instance="msData/regex/RegexTest_491.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_489_regex_test_489_i(mode, save_output):
    """
    TEST :branch : RegexTest_489
    """
    assert_bindings(
        schema="msData/regex/RegexTest_489.xsd",
        instance="msData/regex/RegexTest_489.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_488_regex_test_488_i(mode, save_output):
    """
    TEST :branch : RegexTest_488
    """
    assert_bindings(
        schema="msData/regex/RegexTest_488.xsd",
        instance="msData/regex/RegexTest_488.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_476_regex_test_476_i(mode, save_output):
    """
    TEST :branch : RegexTest_476
    """
    assert_bindings(
        schema="msData/regex/RegexTest_476.xsd",
        instance="msData/regex/RegexTest_476.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_475_regex_test_475_i(mode, save_output):
    """
    TEST :branch : RegexTest_475
    """
    assert_bindings(
        schema="msData/regex/RegexTest_475.xsd",
        instance="msData/regex/RegexTest_475.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_474_regex_test_474_i(mode, save_output):
    """
    TEST :branch : RegexTest_474
    """
    assert_bindings(
        schema="msData/regex/RegexTest_474.xsd",
        instance="msData/regex/RegexTest_474.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_468_regex_test_468_i(mode, save_output):
    """
    TEST :branch : RegexTest_468
    """
    assert_bindings(
        schema="msData/regex/RegexTest_468.xsd",
        instance="msData/regex/RegexTest_468.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_467_regex_test_467_i(mode, save_output):
    """
    TEST :branch : RegexTest_467
    """
    assert_bindings(
        schema="msData/regex/RegexTest_467.xsd",
        instance="msData/regex/RegexTest_467.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_466_regex_test_466_i(mode, save_output):
    """
    TEST :branch : RegexTest_466
    """
    assert_bindings(
        schema="msData/regex/RegexTest_466.xsd",
        instance="msData/regex/RegexTest_466.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_462_regex_test_462_i(mode, save_output):
    """
    TEST :branch : RegexTest_462
    """
    assert_bindings(
        schema="msData/regex/RegexTest_462.xsd",
        instance="msData/regex/RegexTest_462.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_461_regex_test_461_i(mode, save_output):
    """
    TEST :branch : RegexTest_461
    """
    assert_bindings(
        schema="msData/regex/RegexTest_461.xsd",
        instance="msData/regex/RegexTest_461.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_460_regex_test_460_i(mode, save_output):
    """
    TEST :branch : RegexTest_460
    """
    assert_bindings(
        schema="msData/regex/RegexTest_460.xsd",
        instance="msData/regex/RegexTest_460.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_459_regex_test_459_i(mode, save_output):
    """
    TEST :branch : RegexTest_459
    """
    assert_bindings(
        schema="msData/regex/RegexTest_459.xsd",
        instance="msData/regex/RegexTest_459.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_439_regex_test_439_i(mode, save_output):
    """
    TEST :branch : RegexTest_439
    """
    assert_bindings(
        schema="msData/regex/RegexTest_439.xsd",
        instance="msData/regex/RegexTest_439.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_438_regex_test_438_i(mode, save_output):
    """
    TEST :branch : RegexTest_438
    """
    assert_bindings(
        schema="msData/regex/RegexTest_438.xsd",
        instance="msData/regex/RegexTest_438.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_434_regex_test_434_i(mode, save_output):
    """
    TEST :branch : RegexTest_434
    """
    assert_bindings(
        schema="msData/regex/RegexTest_434.xsd",
        instance="msData/regex/RegexTest_434.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_433_regex_test_433_i(mode, save_output):
    """
    TEST :branch : RegexTest_433
    """
    assert_bindings(
        schema="msData/regex/RegexTest_433.xsd",
        instance="msData/regex/RegexTest_433.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_430_regex_test_430_i(mode, save_output):
    """
    TEST :branch : RegexTest_430
    """
    assert_bindings(
        schema="msData/regex/RegexTest_430.xsd",
        instance="msData/regex/RegexTest_430.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_429_regex_test_429_i(mode, save_output):
    """
    TEST :branch : RegexTest_429
    """
    assert_bindings(
        schema="msData/regex/RegexTest_429.xsd",
        instance="msData/regex/RegexTest_429.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_426_regex_test_426_i(mode, save_output):
    """
    TEST :branch : RegexTest_426
    """
    assert_bindings(
        schema="msData/regex/RegexTest_426.xsd",
        instance="msData/regex/RegexTest_426.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_425_regex_test_425_i(mode, save_output):
    """
    TEST :branch : RegexTest_425
    """
    assert_bindings(
        schema="msData/regex/RegexTest_425.xsd",
        instance="msData/regex/RegexTest_425.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_424_regex_test_424_i(mode, save_output):
    """
    TEST :branch : RegexTest_424
    """
    assert_bindings(
        schema="msData/regex/RegexTest_424.xsd",
        instance="msData/regex/RegexTest_424.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_422_regex_test_422_i(mode, save_output):
    """
    TEST :branch : RegexTest_422
    """
    assert_bindings(
        schema="msData/regex/RegexTest_422.xsd",
        instance="msData/regex/RegexTest_422.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_421_regex_test_421_i(mode, save_output):
    """
    TEST :branch : RegexTest_421
    """
    assert_bindings(
        schema="msData/regex/RegexTest_421.xsd",
        instance="msData/regex/RegexTest_421.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_420_regex_test_420_i(mode, save_output):
    """
    TEST :branch : RegexTest_420
    """
    assert_bindings(
        schema="msData/regex/RegexTest_420.xsd",
        instance="msData/regex/RegexTest_420.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_375_regex_test_375_i(mode, save_output):
    """
    TEST :branch : RegexTest_375
    """
    assert_bindings(
        schema="msData/regex/RegexTest_375.xsd",
        instance="msData/regex/RegexTest_375.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_374_regex_test_374_i(mode, save_output):
    """
    TEST :branch : RegexTest_374
    """
    assert_bindings(
        schema="msData/regex/RegexTest_374.xsd",
        instance="msData/regex/RegexTest_374.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_373_regex_test_373_i(mode, save_output):
    """
    TEST :branch : RegexTest_373
    """
    assert_bindings(
        schema="msData/regex/RegexTest_373.xsd",
        instance="msData/regex/RegexTest_373.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_372_regex_test_372_i(mode, save_output):
    """
    TEST :branch : RegexTest_372
    """
    assert_bindings(
        schema="msData/regex/RegexTest_372.xsd",
        instance="msData/regex/RegexTest_372.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_371_regex_test_371_i(mode, save_output):
    """
    TEST :branch : RegexTest_371
    """
    assert_bindings(
        schema="msData/regex/RegexTest_371.xsd",
        instance="msData/regex/RegexTest_371.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_370_regex_test_370_i(mode, save_output):
    """
    TEST :branch : RegexTest_370
    """
    assert_bindings(
        schema="msData/regex/RegexTest_370.xsd",
        instance="msData/regex/RegexTest_370.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_367_regex_test_367_i(mode, save_output):
    """
    TEST :branch : RegexTest_367
    """
    assert_bindings(
        schema="msData/regex/RegexTest_367.xsd",
        instance="msData/regex/RegexTest_367.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_365_regex_test_365_i(mode, save_output):
    """
    TEST :branch : RegexTest_365
    """
    assert_bindings(
        schema="msData/regex/RegexTest_365.xsd",
        instance="msData/regex/RegexTest_365.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_364_regex_test_364_i(mode, save_output):
    """
    TEST :branch : RegexTest_364
    """
    assert_bindings(
        schema="msData/regex/RegexTest_364.xsd",
        instance="msData/regex/RegexTest_364.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_363_regex_test_363_i(mode, save_output):
    """
    TEST :branch : RegexTest_363
    """
    assert_bindings(
        schema="msData/regex/RegexTest_363.xsd",
        instance="msData/regex/RegexTest_363.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_359_regex_test_359_i(mode, save_output):
    """
    TEST :branch : RegexTest_359
    """
    assert_bindings(
        schema="msData/regex/RegexTest_359.xsd",
        instance="msData/regex/RegexTest_359.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_358_regex_test_358_i(mode, save_output):
    """
    TEST :branch : RegexTest_358
    """
    assert_bindings(
        schema="msData/regex/RegexTest_358.xsd",
        instance="msData/regex/RegexTest_358.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_357_regex_test_357_i(mode, save_output):
    """
    TEST :branch : RegexTest_357
    """
    assert_bindings(
        schema="msData/regex/RegexTest_357.xsd",
        instance="msData/regex/RegexTest_357.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_356_regex_test_356_i(mode, save_output):
    """
    TEST :branch : RegexTest_356
    """
    assert_bindings(
        schema="msData/regex/RegexTest_356.xsd",
        instance="msData/regex/RegexTest_356.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_354_regex_test_354_i(mode, save_output):
    """
    TEST :branch : RegexTest_354
    """
    assert_bindings(
        schema="msData/regex/RegexTest_354.xsd",
        instance="msData/regex/RegexTest_354.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_353_regex_test_353_i(mode, save_output):
    """
    TEST :branch : RegexTest_353
    """
    assert_bindings(
        schema="msData/regex/RegexTest_353.xsd",
        instance="msData/regex/RegexTest_353.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_352_regex_test_352_i(mode, save_output):
    """
    TEST :branch : RegexTest_352
    """
    assert_bindings(
        schema="msData/regex/RegexTest_352.xsd",
        instance="msData/regex/RegexTest_352.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_350_regex_test_350_i(mode, save_output):
    """
    TEST :branch : RegexTest_350
    """
    assert_bindings(
        schema="msData/regex/RegexTest_350.xsd",
        instance="msData/regex/RegexTest_350.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_349_regex_test_349_i(mode, save_output):
    """
    TEST :branch : RegexTest_349
    """
    assert_bindings(
        schema="msData/regex/RegexTest_349.xsd",
        instance="msData/regex/RegexTest_349.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_348_regex_test_348_i(mode, save_output):
    """
    TEST :branch : RegexTest_348
    """
    assert_bindings(
        schema="msData/regex/RegexTest_348.xsd",
        instance="msData/regex/RegexTest_348.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_347_regex_test_347_i(mode, save_output):
    """
    TEST :branch : RegexTest_347
    """
    assert_bindings(
        schema="msData/regex/RegexTest_347.xsd",
        instance="msData/regex/RegexTest_347.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_346_regex_test_346_i(mode, save_output):
    """
    TEST :branch : RegexTest_346
    """
    assert_bindings(
        schema="msData/regex/RegexTest_346.xsd",
        instance="msData/regex/RegexTest_346.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_345_regex_test_345_i(mode, save_output):
    """
    TEST :branch : RegexTest_345
    """
    assert_bindings(
        schema="msData/regex/RegexTest_345.xsd",
        instance="msData/regex/RegexTest_345.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_344_regex_test_344_i(mode, save_output):
    """
    TEST :branch : RegexTest_344
    """
    assert_bindings(
        schema="msData/regex/RegexTest_344.xsd",
        instance="msData/regex/RegexTest_344.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_343_regex_test_343_i(mode, save_output):
    """
    TEST :branch : RegexTest_343
    """
    assert_bindings(
        schema="msData/regex/RegexTest_343.xsd",
        instance="msData/regex/RegexTest_343.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_342_regex_test_342_i(mode, save_output):
    """
    TEST :branch : RegexTest_342
    """
    assert_bindings(
        schema="msData/regex/RegexTest_342.xsd",
        instance="msData/regex/RegexTest_342.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_341_regex_test_341_i(mode, save_output):
    """
    TEST :branch : RegexTest_341
    """
    assert_bindings(
        schema="msData/regex/RegexTest_341.xsd",
        instance="msData/regex/RegexTest_341.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_340_regex_test_340_i(mode, save_output):
    """
    TEST :branch : RegexTest_340
    """
    assert_bindings(
        schema="msData/regex/RegexTest_340.xsd",
        instance="msData/regex/RegexTest_340.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_339_regex_test_339_i(mode, save_output):
    """
    TEST :branch : RegexTest_339
    """
    assert_bindings(
        schema="msData/regex/RegexTest_339.xsd",
        instance="msData/regex/RegexTest_339.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_337_regex_test_337_i(mode, save_output):
    """
    TEST :branch : RegexTest_337
    """
    assert_bindings(
        schema="msData/regex/RegexTest_337.xsd",
        instance="msData/regex/RegexTest_337.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_336_regex_test_336_i(mode, save_output):
    """
    TEST :branch : RegexTest_336
    """
    assert_bindings(
        schema="msData/regex/RegexTest_336.xsd",
        instance="msData/regex/RegexTest_336.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_335_regex_test_335_i(mode, save_output):
    """
    TEST :branch : RegexTest_335
    """
    assert_bindings(
        schema="msData/regex/RegexTest_335.xsd",
        instance="msData/regex/RegexTest_335.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_334_regex_test_334_i(mode, save_output):
    """
    TEST :branch : RegexTest_334
    """
    assert_bindings(
        schema="msData/regex/RegexTest_334.xsd",
        instance="msData/regex/RegexTest_334.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_333_regex_test_333_i(mode, save_output):
    """
    TEST :branch : RegexTest_333
    """
    assert_bindings(
        schema="msData/regex/RegexTest_333.xsd",
        instance="msData/regex/RegexTest_333.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_332_regex_test_332_i(mode, save_output):
    """
    TEST :branch : RegexTest_332
    """
    assert_bindings(
        schema="msData/regex/RegexTest_332.xsd",
        instance="msData/regex/RegexTest_332.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_329_regex_test_329_i(mode, save_output):
    """
    TEST :branch : RegexTest_329
    """
    assert_bindings(
        schema="msData/regex/RegexTest_329.xsd",
        instance="msData/regex/RegexTest_329.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_328_regex_test_328_i(mode, save_output):
    """
    TEST :branch : RegexTest_328
    """
    assert_bindings(
        schema="msData/regex/RegexTest_328.xsd",
        instance="msData/regex/RegexTest_328.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_327_regex_test_327_i(mode, save_output):
    """
    TEST :branch : RegexTest_327
    """
    assert_bindings(
        schema="msData/regex/RegexTest_327.xsd",
        instance="msData/regex/RegexTest_327.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_326_regex_test_326_i(mode, save_output):
    """
    TEST :branch : RegexTest_326
    """
    assert_bindings(
        schema="msData/regex/RegexTest_326.xsd",
        instance="msData/regex/RegexTest_326.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_325_regex_test_325_i(mode, save_output):
    """
    TEST :branch : RegexTest_325
    """
    assert_bindings(
        schema="msData/regex/RegexTest_325.xsd",
        instance="msData/regex/RegexTest_325.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_324_regex_test_324_i(mode, save_output):
    """
    TEST :branch : RegexTest_324
    """
    assert_bindings(
        schema="msData/regex/RegexTest_324.xsd",
        instance="msData/regex/RegexTest_324.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_323_regex_test_323_i(mode, save_output):
    """
    TEST :branch : RegexTest_323
    """
    assert_bindings(
        schema="msData/regex/RegexTest_323.xsd",
        instance="msData/regex/RegexTest_323.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_322_regex_test_322_i(mode, save_output):
    """
    TEST :branch : RegexTest_322
    """
    assert_bindings(
        schema="msData/regex/RegexTest_322.xsd",
        instance="msData/regex/RegexTest_322.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_319_regex_test_319_v(mode, save_output):
    """
    TEST :branch : RegexTest_319
    """
    assert_bindings(
        schema="msData/regex/RegexTest_319.xsd",
        instance="msData/regex/RegexTest_319.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_286_regex_test_286_i(mode, save_output):
    """
    TEST :branch : RegexTest_286
    """
    assert_bindings(
        schema="msData/regex/RegexTest_286.xsd",
        instance="msData/regex/RegexTest_286.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_285_regex_test_285_i(mode, save_output):
    """
    TEST :branch : RegexTest_285
    """
    assert_bindings(
        schema="msData/regex/RegexTest_285.xsd",
        instance="msData/regex/RegexTest_285.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_284_regex_test_284_i(mode, save_output):
    """
    TEST :branch : RegexTest_284
    """
    assert_bindings(
        schema="msData/regex/RegexTest_284.xsd",
        instance="msData/regex/RegexTest_284.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_283_regex_test_283_i(mode, save_output):
    """
    TEST :branch : RegexTest_283
    """
    assert_bindings(
        schema="msData/regex/RegexTest_283.xsd",
        instance="msData/regex/RegexTest_283.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_282_regex_test_282_i(mode, save_output):
    """
    TEST :branch : RegexTest_282
    """
    assert_bindings(
        schema="msData/regex/RegexTest_282.xsd",
        instance="msData/regex/RegexTest_282.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_281_regex_test_281_i(mode, save_output):
    """
    TEST :branch : RegexTest_281
    """
    assert_bindings(
        schema="msData/regex/RegexTest_281.xsd",
        instance="msData/regex/RegexTest_281.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_280_regex_test_280_i(mode, save_output):
    """
    TEST :branch : RegexTest_280
    """
    assert_bindings(
        schema="msData/regex/RegexTest_280.xsd",
        instance="msData/regex/RegexTest_280.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_279_regex_test_279_i(mode, save_output):
    """
    TEST :branch : RegexTest_279
    """
    assert_bindings(
        schema="msData/regex/RegexTest_279.xsd",
        instance="msData/regex/RegexTest_279.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_278_regex_test_278_i(mode, save_output):
    """
    TEST :branch : RegexTest_278
    """
    assert_bindings(
        schema="msData/regex/RegexTest_278.xsd",
        instance="msData/regex/RegexTest_278.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_277_regex_test_277_i(mode, save_output):
    """
    TEST :branch : RegexTest_277
    """
    assert_bindings(
        schema="msData/regex/RegexTest_277.xsd",
        instance="msData/regex/RegexTest_277.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_276_regex_test_276_i(mode, save_output):
    """
    TEST :branch : RegexTest_276
    """
    assert_bindings(
        schema="msData/regex/RegexTest_276.xsd",
        instance="msData/regex/RegexTest_276.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_275_regex_test_275_i(mode, save_output):
    """
    TEST :branch : RegexTest_275
    """
    assert_bindings(
        schema="msData/regex/RegexTest_275.xsd",
        instance="msData/regex/RegexTest_275.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_274_regex_test_274_i(mode, save_output):
    """
    TEST :branch : RegexTest_274
    """
    assert_bindings(
        schema="msData/regex/RegexTest_274.xsd",
        instance="msData/regex/RegexTest_274.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_273_regex_test_273_i(mode, save_output):
    """
    TEST :branch : RegexTest_273
    """
    assert_bindings(
        schema="msData/regex/RegexTest_273.xsd",
        instance="msData/regex/RegexTest_273.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_272_regex_test_272_i(mode, save_output):
    """
    TEST :branch : RegexTest_272
    """
    assert_bindings(
        schema="msData/regex/RegexTest_272.xsd",
        instance="msData/regex/RegexTest_272.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_271_regex_test_271_i(mode, save_output):
    """
    TEST :branch : RegexTest_271
    """
    assert_bindings(
        schema="msData/regex/RegexTest_271.xsd",
        instance="msData/regex/RegexTest_271.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_270_regex_test_270_i(mode, save_output):
    """
    TEST :branch : RegexTest_270
    """
    assert_bindings(
        schema="msData/regex/RegexTest_270.xsd",
        instance="msData/regex/RegexTest_270.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_269_regex_test_269_i(mode, save_output):
    """
    TEST :branch : RegexTest_269
    """
    assert_bindings(
        schema="msData/regex/RegexTest_269.xsd",
        instance="msData/regex/RegexTest_269.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_268_regex_test_268_i(mode, save_output):
    """
    TEST :branch : RegexTest_268
    """
    assert_bindings(
        schema="msData/regex/RegexTest_268.xsd",
        instance="msData/regex/RegexTest_268.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_267_regex_test_267_i(mode, save_output):
    """
    TEST :branch : RegexTest_267
    """
    assert_bindings(
        schema="msData/regex/RegexTest_267.xsd",
        instance="msData/regex/RegexTest_267.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_264_regex_test_264_v(mode, save_output):
    """
    TEST :branch : RegexTest_264
    """
    assert_bindings(
        schema="msData/regex/RegexTest_264.xsd",
        instance="msData/regex/RegexTest_264.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_263_regex_test_263_v(mode, save_output):
    """
    TEST :branch : RegexTest_263
    """
    assert_bindings(
        schema="msData/regex/RegexTest_263.xsd",
        instance="msData/regex/RegexTest_263.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_262_regex_test_262_v(mode, save_output):
    """
    TEST :branch : RegexTest_262
    """
    assert_bindings(
        schema="msData/regex/RegexTest_262.xsd",
        instance="msData/regex/RegexTest_262.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_261_regex_test_261_v(mode, save_output):
    """
    TEST :branch : RegexTest_261
    """
    assert_bindings(
        schema="msData/regex/RegexTest_261.xsd",
        instance="msData/regex/RegexTest_261.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_260_regex_test_260_v(mode, save_output):
    """
    TEST :branch : RegexTest_260
    """
    assert_bindings(
        schema="msData/regex/RegexTest_260.xsd",
        instance="msData/regex/RegexTest_260.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_259_regex_test_259_v(mode, save_output):
    """
    TEST :branch : RegexTest_259
    """
    assert_bindings(
        schema="msData/regex/RegexTest_259.xsd",
        instance="msData/regex/RegexTest_259.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_255_regex_test_255_i(mode, save_output):
    """
    TEST :branch : RegexTest_255
    """
    assert_bindings(
        schema="msData/regex/RegexTest_255.xsd",
        instance="msData/regex/RegexTest_255.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_254_regex_test_254_i(mode, save_output):
    """
    TEST :branch : RegexTest_254
    """
    assert_bindings(
        schema="msData/regex/RegexTest_254.xsd",
        instance="msData/regex/RegexTest_254.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_253_regex_test_253_i(mode, save_output):
    """
    TEST :branch : RegexTest_253
    """
    assert_bindings(
        schema="msData/regex/RegexTest_253.xsd",
        instance="msData/regex/RegexTest_253.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_252_regex_test_252_i(mode, save_output):
    """
    TEST :branch : RegexTest_252
    """
    assert_bindings(
        schema="msData/regex/RegexTest_252.xsd",
        instance="msData/regex/RegexTest_252.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_251_regex_test_251_i(mode, save_output):
    """
    TEST :branch : RegexTest_251
    """
    assert_bindings(
        schema="msData/regex/RegexTest_251.xsd",
        instance="msData/regex/RegexTest_251.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_250_regex_test_250_i(mode, save_output):
    """
    TEST :branch : RegexTest_250
    """
    assert_bindings(
        schema="msData/regex/RegexTest_250.xsd",
        instance="msData/regex/RegexTest_250.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_239_regex_test_239_i(mode, save_output):
    """
    TEST :branch : RegexTest_239
    """
    assert_bindings(
        schema="msData/regex/RegexTest_239.xsd",
        instance="msData/regex/RegexTest_239.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_236_regex_test_236_i(mode, save_output):
    """
    TEST :branch : RegexTest_236
    """
    assert_bindings(
        schema="msData/regex/RegexTest_236.xsd",
        instance="msData/regex/RegexTest_236.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_235_regex_test_235_i(mode, save_output):
    """
    TEST :branch : RegexTest_235
    """
    assert_bindings(
        schema="msData/regex/RegexTest_235.xsd",
        instance="msData/regex/RegexTest_235.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_234_regex_test_234_v(mode, save_output):
    """
    TEST :branch : RegexTest_234
    """
    assert_bindings(
        schema="msData/regex/RegexTest_234.xsd",
        instance="msData/regex/RegexTest_234.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_182_regex_test_182_i(mode, save_output):
    """
    TEST :branch : RegexTest_182
    """
    assert_bindings(
        schema="msData/regex/RegexTest_182.xsd",
        instance="msData/regex/RegexTest_182.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_181_regex_test_181_i(mode, save_output):
    """
    TEST :branch : RegexTest_181
    """
    assert_bindings(
        schema="msData/regex/RegexTest_181.xsd",
        instance="msData/regex/RegexTest_181.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_180_regex_test_180_i(mode, save_output):
    """
    TEST :branch : RegexTest_180
    """
    assert_bindings(
        schema="msData/regex/RegexTest_180.xsd",
        instance="msData/regex/RegexTest_180.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_177_regex_test_177_i(mode, save_output):
    """
    TEST :branch : RegexTest_177
    """
    assert_bindings(
        schema="msData/regex/RegexTest_177.xsd",
        instance="msData/regex/RegexTest_177.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_176_regex_test_176_i(mode, save_output):
    """
    TEST :branch : RegexTest_176
    """
    assert_bindings(
        schema="msData/regex/RegexTest_176.xsd",
        instance="msData/regex/RegexTest_176.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_175_regex_test_175_i(mode, save_output):
    """
    TEST :branch : RegexTest_175
    """
    assert_bindings(
        schema="msData/regex/RegexTest_175.xsd",
        instance="msData/regex/RegexTest_175.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_118_regex_test_118_i(mode, save_output):
    """
    TEST :branch : RegexTest_118
    """
    assert_bindings(
        schema="msData/regex/RegexTest_118.xsd",
        instance="msData/regex/RegexTest_118.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_117_regex_test_117_i(mode, save_output):
    """
    TEST :branch : RegexTest_117
    """
    assert_bindings(
        schema="msData/regex/RegexTest_117.xsd",
        instance="msData/regex/RegexTest_117.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_81_regex_test_81_v(mode, save_output):
    """
    TEST :branch : RegexTest_81
    """
    assert_bindings(
        schema="msData/regex/RegexTest_81.xsd",
        instance="msData/regex/RegexTest_81.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_80_regex_test_80_v(mode, save_output):
    """
    TEST :branch : RegexTest_80
    """
    assert_bindings(
        schema="msData/regex/RegexTest_80.xsd",
        instance="msData/regex/RegexTest_80.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_79_regex_test_79_i(mode, save_output):
    """
    TEST :branch : RegexTest_79
    """
    assert_bindings(
        schema="msData/regex/RegexTest_79.xsd",
        instance="msData/regex/RegexTest_79.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_78_regex_test_78_i(mode, save_output):
    """
    TEST :branch : RegexTest_78
    """
    assert_bindings(
        schema="msData/regex/RegexTest_78.xsd",
        instance="msData/regex/RegexTest_78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_77_regex_test_77_i(mode, save_output):
    """
    TEST :branch : RegexTest_77
    """
    assert_bindings(
        schema="msData/regex/RegexTest_77.xsd",
        instance="msData/regex/RegexTest_77.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_76_regex_test_76_i(mode, save_output):
    """
    TEST :branch : RegexTest_76
    """
    assert_bindings(
        schema="msData/regex/RegexTest_76.xsd",
        instance="msData/regex/RegexTest_76.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_75_regex_test_75_i(mode, save_output):
    """
    TEST :branch : RegexTest_75
    """
    assert_bindings(
        schema="msData/regex/RegexTest_75.xsd",
        instance="msData/regex/RegexTest_75.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_74_regex_test_74_i(mode, save_output):
    """
    TEST :branch : RegexTest_74
    """
    assert_bindings(
        schema="msData/regex/RegexTest_74.xsd",
        instance="msData/regex/RegexTest_74.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_73_regex_test_73_v(mode, save_output):
    """
    TEST :branch : RegexTest_73
    """
    assert_bindings(
        schema="msData/regex/RegexTest_73.xsd",
        instance="msData/regex/RegexTest_73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_72_regex_test_72_v(mode, save_output):
    """
    TEST :branch : RegexTest_72
    """
    assert_bindings(
        schema="msData/regex/RegexTest_72.xsd",
        instance="msData/regex/RegexTest_72.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_71_regex_test_71_i(mode, save_output):
    """
    TEST :branch : RegexTest_71
    """
    assert_bindings(
        schema="msData/regex/RegexTest_71.xsd",
        instance="msData/regex/RegexTest_71.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_70_regex_test_70_i(mode, save_output):
    """
    TEST :branch : RegexTest_70
    """
    assert_bindings(
        schema="msData/regex/RegexTest_70.xsd",
        instance="msData/regex/RegexTest_70.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_69_regex_test_69_i(mode, save_output):
    """
    TEST :branch : RegexTest_69
    """
    assert_bindings(
        schema="msData/regex/RegexTest_69.xsd",
        instance="msData/regex/RegexTest_69.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_68_regex_test_68_i(mode, save_output):
    """
    TEST :branch : RegexTest_68
    """
    assert_bindings(
        schema="msData/regex/RegexTest_68.xsd",
        instance="msData/regex/RegexTest_68.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_67_regex_test_67_i(mode, save_output):
    """
    TEST :branch : RegexTest_67
    """
    assert_bindings(
        schema="msData/regex/RegexTest_67.xsd",
        instance="msData/regex/RegexTest_67.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_66_regex_test_66_i(mode, save_output):
    """
    TEST :branch : RegexTest_66
    """
    assert_bindings(
        schema="msData/regex/RegexTest_66.xsd",
        instance="msData/regex/RegexTest_66.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_63_regex_test_63_i(mode, save_output):
    """
    TEST :branch : RegexTest_63
    """
    assert_bindings(
        schema="msData/regex/RegexTest_63.xsd",
        instance="msData/regex/RegexTest_63.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_42_regex_test_42_v(mode, save_output):
    """
    TEST :branch : RegexTest_42
    """
    assert_bindings(
        schema="msData/regex/RegexTest_42.xsd",
        instance="msData/regex/RegexTest_42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_41_regex_test_41_v(mode, save_output):
    """
    TEST :branch : RegexTest_41
    """
    assert_bindings(
        schema="msData/regex/RegexTest_41.xsd",
        instance="msData/regex/RegexTest_41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_40_regex_test_40_i(mode, save_output):
    """
    TEST :branch : RegexTest_40
    """
    assert_bindings(
        schema="msData/regex/RegexTest_40.xsd",
        instance="msData/regex/RegexTest_40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_39_regex_test_39_i(mode, save_output):
    """
    TEST :branch : RegexTest_39
    """
    assert_bindings(
        schema="msData/regex/RegexTest_39.xsd",
        instance="msData/regex/RegexTest_39.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_38_regex_test_38_i(mode, save_output):
    """
    TEST :branch : RegexTest_38
    """
    assert_bindings(
        schema="msData/regex/RegexTest_38.xsd",
        instance="msData/regex/RegexTest_38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_37_regex_test_37_i(mode, save_output):
    """
    TEST :branch : RegexTest_37
    """
    assert_bindings(
        schema="msData/regex/RegexTest_37.xsd",
        instance="msData/regex/RegexTest_37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_36_regex_test_36_i(mode, save_output):
    """
    TEST :branch : RegexTest_36
    """
    assert_bindings(
        schema="msData/regex/RegexTest_36.xsd",
        instance="msData/regex/RegexTest_36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_35_regex_test_35_i(mode, save_output):
    """
    TEST :branch : RegexTest_35
    """
    assert_bindings(
        schema="msData/regex/RegexTest_35.xsd",
        instance="msData/regex/RegexTest_35.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_21_regex_test_21_v(mode, save_output):
    """
    TEST :branch : RegexTest_21
    """
    assert_bindings(
        schema="msData/regex/RegexTest_21.xsd",
        instance="msData/regex/RegexTest_21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_20_regex_test_20_v(mode, save_output):
    """
    TEST :branch : RegexTest_20
    """
    assert_bindings(
        schema="msData/regex/RegexTest_20.xsd",
        instance="msData/regex/RegexTest_20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_13_regex_test_13_i(mode, save_output):
    """
    TEST :branch : RegexTest_13
    """
    assert_bindings(
        schema="msData/regex/RegexTest_13.xsd",
        instance="msData/regex/RegexTest_13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_12_regex_test_12_i(mode, save_output):
    """
    TEST :branch : RegexTest_12
    """
    assert_bindings(
        schema="msData/regex/RegexTest_12.xsd",
        instance="msData/regex/RegexTest_12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_10_regex_test_10_i(mode, save_output):
    """
    TEST :branch : RegexTest_10
    """
    assert_bindings(
        schema="msData/regex/RegexTest_10.xsd",
        instance="msData/regex/RegexTest_10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_8_regex_test_8_i(mode, save_output):
    """
    TEST :branch : RegexTest_8
    """
    assert_bindings(
        schema="msData/regex/RegexTest_8.xsd",
        instance="msData/regex/RegexTest_8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_regex_test_7_regex_test_7_i(mode, save_output):
    """
    TEST :branch : RegexTest_7
    """
    assert_bindings(
        schema="msData/regex/RegexTest_7.xsd",
        instance="msData/regex/RegexTest_7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_6_regex_test_6_v(mode, save_output):
    """
    TEST :branch : RegexTest_6
    """
    assert_bindings(
        schema="msData/regex/RegexTest_6.xsd",
        instance="msData/regex/RegexTest_6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_5_regex_test_5_v(mode, save_output):
    """
    TEST :branch : RegexTest_5
    """
    assert_bindings(
        schema="msData/regex/RegexTest_5.xsd",
        instance="msData/regex/RegexTest_5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_4_regex_test_4_v(mode, save_output):
    """
    TEST :branch : RegexTest_4
    """
    assert_bindings(
        schema="msData/regex/RegexTest_4.xsd",
        instance="msData/regex/RegexTest_4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_3_regex_test_3_v(mode, save_output):
    """
    TEST :branch : RegexTest_3
    """
    assert_bindings(
        schema="msData/regex/RegexTest_3.xsd",
        instance="msData/regex/RegexTest_3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_2_regex_test_2_v(mode, save_output):
    """
    TEST :branch : RegexTest_2
    """
    assert_bindings(
        schema="msData/regex/RegexTest_2.xsd",
        instance="msData/regex/RegexTest_2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_regex_test_1_regex_test_1_v(mode, save_output):
    """
    TEST :branch : RegexTest_1
    """
    assert_bindings(
        schema="msData/regex/RegexTest_1.xsd",
        instance="msData/regex/RegexTest_1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_p21_p21_i(mode, save_output):
    """
    TEST :branch : restriction of two patterns in a simple type (1)
    "[abc]+" (2) "[123]+", should allow only the intersection, value="a1"
    [invalid]
    """
    assert_bindings(
        schema="msData/regex/p21.xsd",
        instance="msData/regex/p21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_p20_p20_v(mode, save_output):
    """
    TEST :branch : restriction of two patterns in a simple type (1)
    "[abc]+" (2) "[123]+", should allow only the intersection, value="a1"
    [invalid]
    """
    assert_bindings(
        schema="msData/regex/p20.xsd",
        instance="msData/regex/p20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_p19_p19_i(mode, save_output):
    """
    TEST :branch : two patterns in a simple type (1) "[abc]+" (2)
    "[123]+", should be same as [abc]+|[123]+, value="a1" [invalid]
    """
    assert_bindings(
        schema="msData/regex/p19.xsd",
        instance="msData/regex/p19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_p18_p18_i(mode, save_output):
    """
    TEST :branch : two patterns in a simple type (1) "[abc]+" (2)
    "[123]+", should be same as [abc]+|[123]+, value="1a" [invalid]
    """
    assert_bindings(
        schema="msData/regex/p18.xsd",
        instance="msData/regex/p18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_p17_p17_v(mode, save_output):
    """
    TEST :branch : two patterns in a simple type (1) "[abc]+" (2)
    "[123]+", should be same as [abc]+|[123]+, value="abcaabbccabc"
    [valid]
    """
    assert_bindings(
        schema="msData/regex/p17.xsd",
        instance="msData/regex/p17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_p16_p16_v(mode, save_output):
    """
    TEST :branch : two patterns in a simple type (1) "[abc]+" (2)
    "[123]+", should be same as [abc]+|[123]+, value="112233123" [valid]
    """
    assert_bindings(
        schema="msData/regex/p16.xsd",
        instance="msData/regex/p16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_p15_p15_i(mode, save_output):
    r"""
    TEST :branch : regex\pattern=123]+|[abc]+, value=a1[invalid]
    """
    assert_bindings(
        schema="msData/regex/p15.xsd",
        instance="msData/regex/p15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_p14_p14_i(mode, save_output):
    r"""
    TEST :branch : regex\pattern=123]+|[abc]+, value=1a[invalid]
    """
    assert_bindings(
        schema="msData/regex/p14.xsd",
        instance="msData/regex/p14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_p13_p13_v(mode, save_output):
    r"""
    TEST :branch : regex\pattern=123]+|[abc]+, value=abcaabbccabc [valid]
    """
    assert_bindings(
        schema="msData/regex/p13.xsd",
        instance="msData/regex/p13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_p12_p12_v(mode, save_output):
    """
    TEST :branch :
    """
    assert_bindings(
        schema="msData/regex/p12.xsd",
        instance="msData/regex/p12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_p11_p11_v(mode, save_output):
    r"""
    TEST :branch : regex\restriction of a type that defined as emum
    {1,2,3}, pattern="[13]", XML has value=3 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p11.xsd",
        instance="msData/regex/p11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_p10_p10_i(mode, save_output):
    r"""
    TEST :branch : regex\restriction of a type that defined as emum
    {1,2,3}, pattern="[13]", XML has value=2 [ invalid ]
    """
    assert_bindings(
        schema="msData/regex/p10.xsd",
        instance="msData/regex/p10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_p9_p9_v(mode, save_output):
    r"""
    TEST :branch : regex\restriction of a type that defined as emum
    {1,2,3}, pattern="[13]", XML has value=1 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p9.xsd",
        instance="msData/regex/p9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_p8_p8_v(mode, save_output):
    r"""
    TEST :branch : restriction of a type that defined as integer,
    minInclusive=-9, pattern="\-[0-9]*", XML has value=-9 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p8.xsd",
        instance="msData/regex/p8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_p7_p7_i(mode, save_output):
    r"""
    TEST :branch : regex\restriction of a type that defined as integer,
    minInclusive=-9, pattern="\-[0-9]*", XML has value=-10 [ invalid ]
    """
    assert_bindings(
        schema="msData/regex/p7.xsd",
        instance="msData/regex/p7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_p6_p6_v(mode, save_output):
    r"""
    TEST :branch : regex\restriction of a type that defined as integer,
    maxExclusive=10, pattern="\-[0-9]*", XML has value=-1 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p6.xsd",
        instance="msData/regex/p6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_p5_p5_v(mode, save_output):
    """
    TEST :branch : restriction of a type that defined as integer,
    maxExclusive=10, pattern="[0-9]*", XML has value=0 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p5.xsd",
        instance="msData/regex/p5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_p4_p4_i(mode, save_output):
    """
    TEST :branch : restriction of a type that defined as integer,
    maxExclusive=10, pattern="[0-9]*", XML has value=10 [ invalid ]
    """
    assert_bindings(
        schema="msData/regex/p4.xsd",
        instance="msData/regex/p4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_p3_p3_v(mode, save_output):
    """
    TEST :branch : restriction of a type that defined as integer,
    maxExclusive=10, pattern="[0-9]*", XML has value=9 [ valid ]
    """
    assert_bindings(
        schema="msData/regex/p3.xsd",
        instance="msData/regex/p3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_p2_p2_i(mode, save_output):
    """
    TEST :branch : restriction of a type that defined as integer,
    pattern="abc" [ invalid ]
    """
    assert_bindings(
        schema="msData/regex/p2.xsd",
        instance="msData/regex/p2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_di14_re_di14_v(mode, save_output):
    r"""
    TEST :branch : base='positiveInteger', pattern='\d+', value='123',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI14.xsd",
        instance="msData/regex/reDI14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_di13_re_di13_i(mode, save_output):
    r"""
    TEST :branch : base='unshgiedByte', pattern='\d+', value='123',
    type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI13.xsd",
        instance="msData/regex/reDI13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_di12_re_di12_i(mode, save_output):
    r"""
    TEST :branch : base='unsignedShort', pattern='\d+', value='123',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI12.xsd",
        instance="msData/regex/reDI12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_di11_re_di11_v(mode, save_output):
    r"""
    TEST :branch : base='unsignedInt', pattern='\d+', value='123',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI11.xsd",
        instance="msData/regex/reDI11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_di10_re_di10_v(mode, save_output):
    r"""
    TEST :branch : base='unsignedLong', pattern='\d+', value='123',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI10.xsd",
        instance="msData/regex/reDI10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_di9_re_di9_v(mode, save_output):
    r"""
    TEST :branch : base='nonNegativeInteger', pattern='\d+', value='1111',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI9.xsd",
        instance="msData/regex/reDI9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_di8_re_di8_v(mode, save_output):
    r"""
    TEST :branch : base='byte', pattern='(\- |
    \+)?((1[0-2]?[0-7]?)|([1-9]?[0-9]?))|(\+?128)', value='128',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI8.xsd",
        instance="msData/regex/reDI8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_di7_re_di7_v(mode, save_output):
    r"""
    TEST :branch : base='short', pattern='\-?[0-3]{3}', value='-300',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI7.xsd",
        instance="msData/regex/reDI7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_di6_re_di6_v(mode, save_output):
    r"""
    TEST :branch : base='int', pattern='\d+', value='123', type='valid',
    RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI6.xsd",
        instance="msData/regex/reDI6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_di5_re_di5_i(mode, save_output):
    r"""
    TEST :branch : base='long', pattern='\d+', value='a', type='invalid',
    RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI5.xsd",
        instance="msData/regex/reDI5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_di4_re_di4_i(mode, save_output):
    r"""
    TEST :branch : base='negativeInteger', pattern='\-?\d', value='+1',
    type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI4.xsd",
        instance="msData/regex/reDI4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_di3_re_di3_i(mode, save_output):
    r"""
    TEST :branch : base='nonPositiveIntebger', pattern='\-\d\d',
    value='11', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI3.xsd",
        instance="msData/regex/reDI3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_di2_re_di2_v(mode, save_output):
    r"""
    TEST :branch : base='integer', pattern='\p{Nd}+', value='10000201',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI2.xsd",
        instance="msData/regex/reDI2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_di1_re_di1_v(mode, save_output):
    r"""
    TEST :branch : base='decimal', pattern='\p{Nd}+', value='10000101',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDI1.xsd",
        instance="msData/regex/reDI1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dh11_re_dh11_v(mode, save_output):
    r"""
    TEST :branch : base='NMTOKEN', pattern='\c[\c\d]*', value='name1',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH11.xsd",
        instance="msData/regex/reDH11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_dh7a_re_dh7a_i(mode, save_output):
    r"""
    TEST :branch : base='IDREF', pattern='\c[\c\d]*', value='ab',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH7a.xsd",
        instance="msData/regex/reDH7a.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dh7_re_dh7_v(mode, save_output):
    r"""
    TEST :branch : base='IDREF', pattern='\c[\c\d]*', value='ab',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH7.xsd",
        instance="msData/regex/reDH7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dh6_re_dh6_v(mode, save_output):
    r"""
    TEST :branch : base='ID', pattern='\c[\c\d]*', value='a1b',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH6.xsd",
        instance="msData/regex/reDH6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dh5_re_dh5_v(mode, save_output):
    r"""
    TEST :branch : base='NCName', pattern='[\i-[:]][\c-[:]]*',
    value='a:b', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH5.xsd",
        instance="msData/regex/reDH5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dh4_re_dh4_v(mode, save_output):
    r"""
    TEST :branch : base='Name', pattern='\c+', value='abcdef',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH4.xsd",
        instance="msData/regex/reDH4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dh3_re_dh3_v(mode, save_output):
    r"""
    TEST :branch : base='language', pattern='\c{2,4}', value='ch-a',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH3.xsd",
        instance="msData/regex/reDH3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dh2_re_dh2_v(mode, save_output):
    r"""
    TEST :branch : base='token', pattern='\c+', value='a', type='valid',
    RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDH2.xsd",
        instance="msData/regex/reDH2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dg7_re_dg7_v(mode, save_output):
    """
    TEST :branch : base='gMonth', pattern='[123456789]|(10|11|12)',
    value='9', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDG7.xsd",
        instance="msData/regex/reDG7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dg6_re_dg6_v(mode, save_output):
    """
    TEST :branch : base='gDay', pattern='([123]0)|([12]?[1-9])|(31)',
    value='30', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDG6.xsd",
        instance="msData/regex/reDG6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dg5_re_dg5_v(mode, save_output):
    r"""
    TEST :branch : base='gMonthDay', pattern='0[123]\-(12|14)',
    value='03-14', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDG5.xsd",
        instance="msData/regex/reDG5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_dg4_re_dg4_i(mode, save_output):
    r"""
    TEST :branch : base='gYear', pattern='\p{Nd}{2}', value='1999',
    type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDG4.xsd",
        instance="msData/regex/reDG4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dg3_re_dg3_v(mode, save_output):
    r"""
    TEST :branch : base='gYear', pattern='\p{Nd}{4}', value='1999',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDG3.xsd",
        instance="msData/regex/reDG3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_dg2_re_dg2_i(mode, save_output):
    r"""
    TEST :branch : base='gYearMonth', pattern='\p{Nd}{4}-\p{Nd}{2}',
    value='12000-11', type='invalid', RULE='' Fixed schema typo in schema
    (twice) and instance and above
    """
    assert_bindings(
        schema="msData/regex/reDG2.xsd",
        instance="msData/regex/reDG2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dg1_re_dg1_v(mode, save_output):
    r"""
    TEST :branch : base='date', pattern='\p{Nd}{4}-\p{Nd}{2}-\p{Nd}{2}',
    value='1999-12-12', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDG1.xsd",
        instance="msData/regex/reDG1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_df5_re_df5_i(mode, save_output):
    r"""
    TEST :branch : base='time', pattern='\p{Nd}+:\d\d:\d\d(\-\d\d:\d\d)?',
    value='12345:12:12-12:12', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDF5.xsd",
        instance="msData/regex/reDF5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_df3_re_df3_i(mode, save_output):
    r"""
    TEST :branch : base='time', pattern='\c+', value='abc',
    type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDF3.xsd",
        instance="msData/regex/reDF3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_df2_re_df2_v(mode, save_output):
    r"""
    TEST :branch : base='time',
    pattern='\p{Nd}{2}:\d\d:\d\d(\-\d\d:\d\d)?', value='13:20:00-5:00',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDF2.xsd",
        instance="msData/regex/reDF2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_df1_re_df1_v(mode, save_output):
    r"""
    TEST :branch : base='time',
    pattern='\p{Nd}{2}:\d\d:\d\d(\-\d\d:\d\d)?', value='11:00:00',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDF1.xsd",
        instance="msData/regex/reDF1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_de4_re_de4_i(mode, save_output):
    r"""
    TEST :branch : base='dateTime',
    pattern='\p{Nd}{4}-\d\d-\d\dT\d\d:\d\d:\d\d',
    value='2001-06-32T12:12:00', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDE4.xsd",
        instance="msData/regex/reDE4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_de3_re_de3_i(mode, save_output):
    r"""
    TEST :branch : base='dateTime',
    pattern='\p{Nd}{4}-\d\d-\d\dT\d\d:\d\d:\d\d',
    value='2001-06-06T12:12:61', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDE3.xsd",
        instance="msData/regex/reDE3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_de2_re_de2_i(mode, save_output):
    r"""
    TEST :branch : base='dateTime',
    pattern='\p{Nd}{4}-\d\d-\d\dT\d\d:\d\d:\d\d', value='',
    type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDE2.xsd",
        instance="msData/regex/reDE2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_de1_re_de1_v(mode, save_output):
    r"""
    TEST :branch : base='dateTime',
    pattern='\p{Nd}{4}-\d\d-\d\dT\d\d:\d\d:\d\d',
    value='2001-06-06T12:12:00', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDE1.xsd",
        instance="msData/regex/reDE1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_dd8_re_dd8_i(mode, save_output):
    r"""
    TEST :branch : base='duration', pattern='P\p{Nd}{4}Y\p{Nd}{2}M',
    value='P11111Y13M', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDD8.xsd",
        instance="msData/regex/reDD8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_dd7_re_dd7_i(mode, save_output):
    r"""
    TEST :branch : base='duration', pattern='P\p{Nd}{4}Y\p{Nd}{2}M',
    value='P11111Y00M', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDD7.xsd",
        instance="msData/regex/reDD7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_dd6_re_dd6_i(mode, save_output):
    r"""
    TEST :branch : base='duration', pattern='P\p{Nd}{4}Y\p{Nd}{2}M',
    value='P12M', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDD6.xsd",
        instance="msData/regex/reDD6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_dd5_re_dd5_i(mode, save_output):
    r"""
    TEST :branch : base='duration', pattern='P\p{Nd}{4}Y\p{Nd}{2}M',
    value='P1111Y', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDD5.xsd",
        instance="msData/regex/reDD5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_dd4_re_dd4_i(mode, save_output):
    r"""
    TEST :branch : base='duration', pattern='P\p{Nd}{4}Y\p{Nd}{2}M',
    value='P11111Y12M', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDD4.xsd",
        instance="msData/regex/reDD4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_dd3_re_dd3_i(mode, save_output):
    r"""
    TEST :branch : base='duration', pattern='P\p{Nd}{4}Y\p{Nd}{2}M',
    value='P1111Y1M', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDD3.xsd",
        instance="msData/regex/reDD3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_dd2_re_dd2_i(mode, save_output):
    r"""
    TEST :branch : base='duration', pattern='P\p{Nd}{4}Y\p{Nd}{2}M',
    value='P111Y12M', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDD2.xsd",
        instance="msData/regex/reDD2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dd1_re_dd1_v(mode, save_output):
    r"""
    TEST :branch : base='duration', pattern='P\p{Nd}{4}Y\p{Nd}{2}M',
    value='P1111Y12M', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDD1.xsd",
        instance="msData/regex/reDD1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dc5_re_dc5_v(mode, save_output):
    r"""
    TEST :branch : base='Qname',
    pattern='[\i-[:]][\c-[:]]+:[\i-[:]][\c-[:]]+', value='a:b',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDC5.xsd",
        instance="msData/regex/reDC5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dc4_re_dc4_v(mode, save_output):
    r"""
    TEST :branch : base='anyURI', pattern='http://\c*',
    value='http://www.foo.com', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDC4.xsd",
        instance="msData/regex/reDC4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dc3_re_dc3_v(mode, save_output):
    r"""
    TEST :branch : base='double', pattern='\d*\.\d+', value='1.001',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDC3.xsd",
        instance="msData/regex/reDC3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dc2_re_dc2_v(mode, save_output):
    r"""
    TEST :branch : base='float', pattern='\d*\.\d+', value='1.001',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDC2.xsd",
        instance="msData/regex/reDC2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_dc1_re_dc1_v(mode, save_output):
    """
    TEST :branch : base='hexBinary', pattern='AF01D1', value='AF01D1',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDC1.xsd",
        instance="msData/regex/reDC1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_db6_re_db6_i(mode, save_output):
    """
    TEST :branch : base='base64Binary', pattern='([0-1]{4} | (0 | 1){8})',
    value='111111111', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDB6.xsd",
        instance="msData/regex/reDB6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_db5_re_db5_i(mode, save_output):
    """
    TEST :branch : base='base64Binary', pattern='([0-1]{4} | (0 | 1){8})',
    value='1111111', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDB5.xsd",
        instance="msData/regex/reDB5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_db4_re_db4_i(mode, save_output):
    """
    TEST :branch : base='base64Binary', pattern='([0-1]{4} | (0 | 1){8})',
    value='11111', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDB4.xsd",
        instance="msData/regex/reDB4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_db3_re_db3_i(mode, save_output):
    """
    TEST :branch : base='base64Binary', pattern='([0-1]{4} | (0 | 1){8})',
    value='111', type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDB3.xsd",
        instance="msData/regex/reDB3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_db2_re_db2_v(mode, save_output):
    """
    TEST :branch : base='base64Binary', pattern='([0-1]{4} | (0 | 1){8})',
    value='110100111', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDB2.xsd",
        instance="msData/regex/reDB2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_db1_re_db1_v(mode, save_output):
    """
    TEST :branch : base='base64Binary', pattern='([0-1]{4} | (0 | 1){8})',
    value='1111', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDB1.xsd",
        instance="msData/regex/reDB1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_da15_re_da15_v(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='(1|true|false|0|0)',
    value='0', type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA15.xsd",
        instance="msData/regex/reDA15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_da14_re_da14_i(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='(1|true)', value='2',
    type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA14.xsd",
        instance="msData/regex/reDA14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_da13_re_da13_i(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='(1|true)', value='',
    type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA13.xsd",
        instance="msData/regex/reDA13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_da12_re_da12_i(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='(1|true)', value='FALSE',
    type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA12.xsd",
        instance="msData/regex/reDA12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_da11_re_da11_i(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='(1|true)', value='0',
    type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA11.xsd",
        instance="msData/regex/reDA11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_da10_re_da10_i(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='(1|true)', value='TRUE',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA10.xsd",
        instance="msData/regex/reDA10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_da9_re_da9_v(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='(1|true)', value='1',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA9.xsd",
        instance="msData/regex/reDA9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_da6_re_da6_v(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='(true|false)', value='false',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA6.xsd",
        instance="msData/regex/reDA6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_da5_re_da5_v(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='(true|false)', value='true',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA5.xsd",
        instance="msData/regex/reDA5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_da4_re_da4_v(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='false', value='false',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA4.xsd",
        instance="msData/regex/reDA4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_da3_re_da3_i(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='false', value='true',
    type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA3.xsd",
        instance="msData/regex/reDA3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_da2_re_da2_i(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='true', value='false',
    type='invalid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA2.xsd",
        instance="msData/regex/reDA2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_da1_re_da1_v(mode, save_output):
    """
    TEST :branch : base='boolean', pattern='true', value='true',
    type='valid', RULE=''
    """
    assert_bindings(
        schema="msData/regex/reDA1.xsd",
        instance="msData/regex/reDA1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v43_re_v43_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1D1DD;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV43.xsd",
        instance="msData/regex/reV43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v42_re_v42_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x3190;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV42.xsd",
        instance="msData/regex/reV42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v41_re_v41_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x3190;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV41.xsd",
        instance="msData/regex/reV41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v40_re_v40_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#xFFE3;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV40.xsd",
        instance="msData/regex/reV40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v39_re_v39_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x309B;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV39.xsd",
        instance="msData/regex/reV39.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v38_re_v38_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x309B;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV38.xsd",
        instance="msData/regex/reV38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v37_re_v37_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#xFFE6;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV37.xsd",
        instance="msData/regex/reV37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v36_re_v36_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x20A0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV36.xsd",
        instance="msData/regex/reV36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v35_re_v35_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x20A0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV35.xsd",
        instance="msData/regex/reV35.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v34_re_v34_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#xFFE2;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV34.xsd",
        instance="msData/regex/reV34.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v33_re_v33_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x2044;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV33.xsd",
        instance="msData/regex/reV33.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v32_re_v32_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x10323;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV32.xsd",
        instance="msData/regex/reV32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v31_re_v31_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#xB2;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV31.xsd",
        instance="msData/regex/reV31.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v30_re_v30_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#xB2;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV30.xsd",
        instance="msData/regex/reV30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v29_re_v29_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x3025;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV29.xsd",
        instance="msData/regex/reV29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v28_re_v28_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1034A;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV28.xsd",
        instance="msData/regex/reV28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v27_re_v27_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1034A;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV27.xsd",
        instance="msData/regex/reV27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v26_re_v26_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1D7FF;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV26.xsd",
        instance="msData/regex/reV26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v25_re_v25_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#xFF10;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV25.xsd",
        instance="msData/regex/reV25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v24_re_v24_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x20E2;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV24.xsd",
        instance="msData/regex/reV24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v23_re_v23_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x20DD;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV23.xsd",
        instance="msData/regex/reV23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v22_re_v22_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x20DD;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV22.xsd",
        instance="msData/regex/reV22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v21_re_v21_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1D172;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV21.xsd",
        instance="msData/regex/reV21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v20_re_v20_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x903;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV20.xsd",
        instance="msData/regex/reV20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v19_re_v19_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1D172;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV19.xsd",
        instance="msData/regex/reV19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v18_re_v18_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x903;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV18.xsd",
        instance="msData/regex/reV18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v17_re_v17_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1D1AD;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV17.xsd",
        instance="msData/regex/reV17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v16_re_v16_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x64B;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV16.xsd",
        instance="msData/regex/reV16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v15_re_v15_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x2FA1D;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV15.xsd",
        instance="msData/regex/reV15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v14_re_v14_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x5D0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV14.xsd",
        instance="msData/regex/reV14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v13_re_v13_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x5D0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV13.xsd",
        instance="msData/regex/reV13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v12_re_v12_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#xFF9F;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV12.xsd",
        instance="msData/regex/reV12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v11_re_v11_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x2B0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV11.xsd",
        instance="msData/regex/reV11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v10_re_v10_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x2B0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV10.xsd",
        instance="msData/regex/reV10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v9_re_v9_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1FFC;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV9.xsd",
        instance="msData/regex/reV9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v8_re_v8_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1C5;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV8.xsd",
        instance="msData/regex/reV8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v7_re_v7_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1C5;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV7.xsd",
        instance="msData/regex/reV7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v6_re_v6_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1D7C9;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV6.xsd",
        instance="msData/regex/reV6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v5_re_v5_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x61;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV5.xsd",
        instance="msData/regex/reV5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v4_re_v4_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x61;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV4.xsd",
        instance="msData/regex/reV4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v3_re_v3_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x1D7A8;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV3.xsd",
        instance="msData/regex/reV3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_v2_re_v2_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\W', value='#x41;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reV2.xsd",
        instance="msData/regex/reV2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u15_re_u15_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x2029;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU15.xsd",
        instance="msData/regex/reU15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u14_re_u14_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x2028;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU14.xsd",
        instance="msData/regex/reU14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u13_re_u13_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x0020;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU13.xsd",
        instance="msData/regex/reU13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u12_re_u12_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x0F04;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU12.xsd",
        instance="msData/regex/reU12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u11_re_u11_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x00BB;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU11.xsd",
        instance="msData/regex/reU11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u10_re_u10_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x201C;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU10.xsd",
        instance="msData/regex/reU10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u9_re_u9_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x007D;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU9.xsd",
        instance="msData/regex/reU9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u8_re_u8_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#xFE37;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU8.xsd",
        instance="msData/regex/reU8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u7_re_u7_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x2010;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU7.xsd",
        instance="msData/regex/reU7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_u6_re_u6_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x023F;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU6.xsd",
        instance="msData/regex/reU6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u5_re_u5_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x007F;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU5.xsd",
        instance="msData/regex/reU5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u4_re_u4_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#x070F;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU4.xsd",
        instance="msData/regex/reU4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_u3_re_u3_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\w', value='#xF8FF;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reU3.xsd",
        instance="msData/regex/reU3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t84_re_t84_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1D800;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT84.xsd",
        instance="msData/regex/reT84.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t83_re_t83_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#xFF1A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT83.xsd",
        instance="msData/regex/reT83.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t82_re_t82_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x181A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT82.xsd",
        instance="msData/regex/reT82.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t81_re_t81_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x17EA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT81.xsd",
        instance="msData/regex/reT81.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t80_re_t80_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1372;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT80.xsd",
        instance="msData/regex/reT80.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t79_re_t79_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x104A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT79.xsd",
        instance="msData/regex/reT79.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t78_re_t78_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0F2A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT78.xsd",
        instance="msData/regex/reT78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t77_re_t77_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0EDA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT77.xsd",
        instance="msData/regex/reT77.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t76_re_t76_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0E5A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT76.xsd",
        instance="msData/regex/reT76.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t75_re_t75_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0D70;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT75.xsd",
        instance="msData/regex/reT75.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t74_re_t74_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0CF0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT74.xsd",
        instance="msData/regex/reT74.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t73_re_t73_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0C70;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT73.xsd",
        instance="msData/regex/reT73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t72_re_t72_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0BF0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT72.xsd",
        instance="msData/regex/reT72.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t71_re_t71_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0B70;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT71.xsd",
        instance="msData/regex/reT71.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t70_re_t70_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0AF0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT70.xsd",
        instance="msData/regex/reT70.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t69_re_t69_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0A79;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT69.xsd",
        instance="msData/regex/reT69.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t68_re_t68_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x09F0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT68.xsd",
        instance="msData/regex/reT68.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t67_re_t67_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0970;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT67.xsd",
        instance="msData/regex/reT67.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t66_re_t66_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x06FA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT66.xsd",
        instance="msData/regex/reT66.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t65_re_t65_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x066A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT65.xsd",
        instance="msData/regex/reT65.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t64_re_t64_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x003A;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT64.xsd",
        instance="msData/regex/reT64.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t63_re_t63_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1D7CD;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT63.xsd",
        instance="msData/regex/reT63.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t62_re_t62_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#xFF09;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT62.xsd",
        instance="msData/regex/reT62.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t61_re_t61_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1809;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT61.xsd",
        instance="msData/regex/reT61.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t60_re_t60_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x17DF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT60.xsd",
        instance="msData/regex/reT60.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t59_re_t59_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1368;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT59.xsd",
        instance="msData/regex/reT59.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t58_re_t58_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1039;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT58.xsd",
        instance="msData/regex/reT58.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t57_re_t57_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0F19;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT57.xsd",
        instance="msData/regex/reT57.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t56_re_t56_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0ECF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT56.xsd",
        instance="msData/regex/reT56.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t55_re_t55_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0E49;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT55.xsd",
        instance="msData/regex/reT55.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t54_re_t54_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0D65;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT54.xsd",
        instance="msData/regex/reT54.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t53_re_t53_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0CE5;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT53.xsd",
        instance="msData/regex/reT53.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t52_re_t52_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0C65;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT52.xsd",
        instance="msData/regex/reT52.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t51_re_t51_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0BE6;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT51.xsd",
        instance="msData/regex/reT51.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t50_re_t50_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0B65;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT50.xsd",
        instance="msData/regex/reT50.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t49_re_t49_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0AE5;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT49.xsd",
        instance="msData/regex/reT49.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t48_re_t48_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0A65;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT48.xsd",
        instance="msData/regex/reT48.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t47_re_t47_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x09E5;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT47.xsd",
        instance="msData/regex/reT47.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t46_re_t46_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0965;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT46.xsd",
        instance="msData/regex/reT46.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t45_re_t45_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x06EE;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT45.xsd",
        instance="msData/regex/reT45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t44_re_t44_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0659;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT44.xsd",
        instance="msData/regex/reT44.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t43_re_t43_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0029;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT43.xsd",
        instance="msData/regex/reT43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t42_re_t42_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1D7FF;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT42.xsd",
        instance="msData/regex/reT42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t41_re_t41_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#xFF19;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT41.xsd",
        instance="msData/regex/reT41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t40_re_t40_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1819;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT40.xsd",
        instance="msData/regex/reT40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t39_re_t39_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x17E9;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT39.xsd",
        instance="msData/regex/reT39.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t38_re_t38_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1371;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT38.xsd",
        instance="msData/regex/reT38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t37_re_t37_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1049;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT37.xsd",
        instance="msData/regex/reT37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t36_re_t36_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0F29;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT36.xsd",
        instance="msData/regex/reT36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t35_re_t35_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0ED9;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT35.xsd",
        instance="msData/regex/reT35.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t34_re_t34_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0E59;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT34.xsd",
        instance="msData/regex/reT34.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t33_re_t33_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0D6F;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT33.xsd",
        instance="msData/regex/reT33.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t32_re_t32_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0CEF;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT32.xsd",
        instance="msData/regex/reT32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t31_re_t31_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0C6F;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT31.xsd",
        instance="msData/regex/reT31.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t30_re_t30_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0BEF;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT30.xsd",
        instance="msData/regex/reT30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t29_re_t29_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0B6F;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT29.xsd",
        instance="msData/regex/reT29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t28_re_t28_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0AEF;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT28.xsd",
        instance="msData/regex/reT28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t27_re_t27_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0A6F;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT27.xsd",
        instance="msData/regex/reT27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t26_re_t26_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x09EF;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT26.xsd",
        instance="msData/regex/reT26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t25_re_t25_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x096F;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT25.xsd",
        instance="msData/regex/reT25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t24_re_t24_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x06F9;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT24.xsd",
        instance="msData/regex/reT24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t23_re_t23_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0669;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT23.xsd",
        instance="msData/regex/reT23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t22_re_t22_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0039;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT22.xsd",
        instance="msData/regex/reT22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t21_re_t21_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1D7CE;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT21.xsd",
        instance="msData/regex/reT21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t20_re_t20_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#xFF10;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT20.xsd",
        instance="msData/regex/reT20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t19_re_t19_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1810;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT19.xsd",
        instance="msData/regex/reT19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t18_re_t18_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x17E0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT18.xsd",
        instance="msData/regex/reT18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_t17_re_t17_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1369;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT17.xsd",
        instance="msData/regex/reT17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t16_re_t16_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x1040;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT16.xsd",
        instance="msData/regex/reT16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t15_re_t15_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0F20;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT15.xsd",
        instance="msData/regex/reT15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t14_re_t14_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0ED0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT14.xsd",
        instance="msData/regex/reT14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t13_re_t13_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0E50;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT13.xsd",
        instance="msData/regex/reT13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t12_re_t12_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0D66;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT12.xsd",
        instance="msData/regex/reT12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t11_re_t11_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0CE6;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT11.xsd",
        instance="msData/regex/reT11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t10_re_t10_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0C66;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT10.xsd",
        instance="msData/regex/reT10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t9_re_t9_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0BE7;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT9.xsd",
        instance="msData/regex/reT9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t7_re_t7_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0AE6;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT7.xsd",
        instance="msData/regex/reT7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t5_re_t5_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x09E6;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT5.xsd",
        instance="msData/regex/reT5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t4_re_t4_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0966;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT4.xsd",
        instance="msData/regex/reT4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t3_re_t3_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x06F0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT3.xsd",
        instance="msData/regex/reT3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t2_re_t2_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0660;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT2.xsd",
        instance="msData/regex/reT2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_t1_re_t1_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\D', value='#x0030;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reT1.xsd",
        instance="msData/regex/reT1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s84_re_s84_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1D800;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS84.xsd",
        instance="msData/regex/reS84.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s83_re_s83_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#xFF1A;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS83.xsd",
        instance="msData/regex/reS83.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s82_re_s82_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x181A;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS82.xsd",
        instance="msData/regex/reS82.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s81_re_s81_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x17EA;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS81.xsd",
        instance="msData/regex/reS81.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s80_re_s80_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1372;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS80.xsd",
        instance="msData/regex/reS80.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s79_re_s79_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x104A;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS79.xsd",
        instance="msData/regex/reS79.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s78_re_s78_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0F2A;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS78.xsd",
        instance="msData/regex/reS78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s77_re_s77_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0EDA;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS77.xsd",
        instance="msData/regex/reS77.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s76_re_s76_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0E5A;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS76.xsd",
        instance="msData/regex/reS76.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s75_re_s75_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0D70;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS75.xsd",
        instance="msData/regex/reS75.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s74_re_s74_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0CF0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS74.xsd",
        instance="msData/regex/reS74.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s73_re_s73_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0C70;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS73.xsd",
        instance="msData/regex/reS73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s72_re_s72_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0BF0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS72.xsd",
        instance="msData/regex/reS72.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s71_re_s71_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0B70;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS71.xsd",
        instance="msData/regex/reS71.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s70_re_s70_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0AF0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS70.xsd",
        instance="msData/regex/reS70.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s69_re_s69_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0A79;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS69.xsd",
        instance="msData/regex/reS69.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s68_re_s68_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x09F0;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS68.xsd",
        instance="msData/regex/reS68.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s67_re_s67_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0970;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS67.xsd",
        instance="msData/regex/reS67.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s66_re_s66_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x06FA;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS66.xsd",
        instance="msData/regex/reS66.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s65_re_s65_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x066A;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS65.xsd",
        instance="msData/regex/reS65.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s64_re_s64_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x003A;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS64.xsd",
        instance="msData/regex/reS64.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s63_re_s63_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1D7CD;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS63.xsd",
        instance="msData/regex/reS63.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s62_re_s62_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#xFF09;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS62.xsd",
        instance="msData/regex/reS62.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s61_re_s61_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1809;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS61.xsd",
        instance="msData/regex/reS61.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s60_re_s60_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x17DF;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS60.xsd",
        instance="msData/regex/reS60.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s59_re_s59_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1368;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS59.xsd",
        instance="msData/regex/reS59.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s58_re_s58_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1039;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS58.xsd",
        instance="msData/regex/reS58.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s57_re_s57_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0F19;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS57.xsd",
        instance="msData/regex/reS57.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s56_re_s56_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0ECF;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS56.xsd",
        instance="msData/regex/reS56.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s55_re_s55_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0E49;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS55.xsd",
        instance="msData/regex/reS55.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s54_re_s54_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0D65;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS54.xsd",
        instance="msData/regex/reS54.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s53_re_s53_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0CE5;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS53.xsd",
        instance="msData/regex/reS53.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s52_re_s52_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0C65;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS52.xsd",
        instance="msData/regex/reS52.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s51_re_s51_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0BE6;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS51.xsd",
        instance="msData/regex/reS51.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s50_re_s50_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0B65;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS50.xsd",
        instance="msData/regex/reS50.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s49_re_s49_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0AE5;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS49.xsd",
        instance="msData/regex/reS49.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s48_re_s48_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0A65;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS48.xsd",
        instance="msData/regex/reS48.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s47_re_s47_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x09E5;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS47.xsd",
        instance="msData/regex/reS47.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s46_re_s46_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0965;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS46.xsd",
        instance="msData/regex/reS46.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s45_re_s45_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x06EE;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS45.xsd",
        instance="msData/regex/reS45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s44_re_s44_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0659;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS44.xsd",
        instance="msData/regex/reS44.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s43_re_s43_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0029;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS43.xsd",
        instance="msData/regex/reS43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s42_re_s42_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1D7FF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS42.xsd",
        instance="msData/regex/reS42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s41_re_s41_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#xFF19;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS41.xsd",
        instance="msData/regex/reS41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s40_re_s40_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1819;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS40.xsd",
        instance="msData/regex/reS40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s39_re_s39_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x17E9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS39.xsd",
        instance="msData/regex/reS39.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s38_re_s38_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1371;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS38.xsd",
        instance="msData/regex/reS38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s37_re_s37_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1049;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS37.xsd",
        instance="msData/regex/reS37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s36_re_s36_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0F29;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS36.xsd",
        instance="msData/regex/reS36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s35_re_s35_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0ED9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS35.xsd",
        instance="msData/regex/reS35.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s34_re_s34_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0E59;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS34.xsd",
        instance="msData/regex/reS34.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s33_re_s33_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0D6F;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS33.xsd",
        instance="msData/regex/reS33.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s32_re_s32_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0CEF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS32.xsd",
        instance="msData/regex/reS32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s31_re_s31_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0C6F;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS31.xsd",
        instance="msData/regex/reS31.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s30_re_s30_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0BEF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS30.xsd",
        instance="msData/regex/reS30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s29_re_s29_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0B6F;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS29.xsd",
        instance="msData/regex/reS29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s28_re_s28_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0AEF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS28.xsd",
        instance="msData/regex/reS28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s27_re_s27_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0A6F;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS27.xsd",
        instance="msData/regex/reS27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s26_re_s26_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x09EF;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS26.xsd",
        instance="msData/regex/reS26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s25_re_s25_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x096F;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS25.xsd",
        instance="msData/regex/reS25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s24_re_s24_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x06F9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS24.xsd",
        instance="msData/regex/reS24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s23_re_s23_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0669;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS23.xsd",
        instance="msData/regex/reS23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s22_re_s22_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0039;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS22.xsd",
        instance="msData/regex/reS22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_s21_re_s21_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1D7CE;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS21.xsd",
        instance="msData/regex/reS21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s20_re_s20_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#xFF10;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS20.xsd",
        instance="msData/regex/reS20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s19_re_s19_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1810;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS19.xsd",
        instance="msData/regex/reS19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s18_re_s18_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x17E0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS18.xsd",
        instance="msData/regex/reS18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s17_re_s17_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1369;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS17.xsd",
        instance="msData/regex/reS17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s16_re_s16_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x1040;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS16.xsd",
        instance="msData/regex/reS16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s15_re_s15_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0F20;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS15.xsd",
        instance="msData/regex/reS15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s14_re_s14_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0ED0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS14.xsd",
        instance="msData/regex/reS14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s13_re_s13_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0E50;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS13.xsd",
        instance="msData/regex/reS13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s12_re_s12_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0D66;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS12.xsd",
        instance="msData/regex/reS12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s11_re_s11_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0CE6;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS11.xsd",
        instance="msData/regex/reS11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s10_re_s10_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0C66;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS10.xsd",
        instance="msData/regex/reS10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s9_re_s9_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0BE7;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS9.xsd",
        instance="msData/regex/reS9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s8_re_s8_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0B66;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS8.xsd",
        instance="msData/regex/reS8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s7_re_s7_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0AE6;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS7.xsd",
        instance="msData/regex/reS7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s6_re_s6_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0A66;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS6.xsd",
        instance="msData/regex/reS6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s5_re_s5_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x09E6;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS5.xsd",
        instance="msData/regex/reS5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s3_re_s3_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x06F0;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS3.xsd",
        instance="msData/regex/reS3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_s1_re_s1_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\d', value='#x0030;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reS1.xsd",
        instance="msData/regex/reS1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r29_re_r29_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c\C?\c\C+\c\C*',
    value='a1b1c1a', type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR29.xsd",
        instance="msData/regex/reR29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r28_re_r28_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c\C?\c\C+\c\C*',
    value='1a2a2', type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR28.xsd",
        instance="msData/regex/reR28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r27_re_r27_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c\C?\c\C+\c\C*',
    value='ab12345', type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR27.xsd",
        instance="msData/regex/reR27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r26_re_r26_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c\C?\c\C+\c\C*',
    value='a12b1c1', type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR26.xsd",
        instance="msData/regex/reR26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r25_re_r25_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c\C?\c\C+\c\C*', value='aa2a',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR25.xsd",
        instance="msData/regex/reR25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r24_re_r24_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c\C?\c\C+\c\C*',
    value='a1a2a3', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR24.xsd",
        instance="msData/regex/reR24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r23_re_r23_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c\C?\c\C+\c\C*', value='',
    type='', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR23.xsd",
        instance="msData/regex/reR23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r22_re_r22_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\C', value='#x9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR22.xsd",
        instance="msData/regex/reR22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r21_re_r21_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\C', value='#xD;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR21.xsd",
        instance="msData/regex/reR21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r20_re_r20_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\C', value='#xA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR20.xsd",
        instance="msData/regex/reR20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r19_re_r19_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\C', value='#x20;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR19.xsd",
        instance="msData/regex/reR19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r18_re_r18_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\C', value='a', type='invalid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR18.xsd",
        instance="msData/regex/reR18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r17_re_r17_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\C', value=':', type='invalid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR17.xsd",
        instance="msData/regex/reR17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r16_re_r16_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\C', value='_', type='invalid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR16.xsd",
        instance="msData/regex/reR16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r15_re_r15_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c?\c+\c*', value='',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR15.xsd",
        instance="msData/regex/reR15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r14_re_r14_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c?\c+\c*',
    value='aaaaaaaaaaaaaaaaaaaaaaaaaa', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR14.xsd",
        instance="msData/regex/reR14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r13_re_r13_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c?\c+\c*', value='aa',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR13.xsd",
        instance="msData/regex/reR13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r12_re_r12_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c?\c+\c*', value='a',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR12.xsd",
        instance="msData/regex/reR12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r11_re_r11_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c?\?\d\s\c+', value='a?2#xa;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR11.xsd",
        instance="msData/regex/reR11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r10_re_r10_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c?\?\d\s\c+', value='aa?3 c',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR10.xsd",
        instance="msData/regex/reR10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r9_re_r9_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c?\?\d\s\c+',
    value='?0#xd;zzz', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR9.xsd",
        instance="msData/regex/reR9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r8_re_r8_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c?\?\d\s\c+', value='c?1 abc',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR8.xsd",
        instance="msData/regex/reR8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r7_re_r7_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c', value='#x9;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR7.xsd",
        instance="msData/regex/reR7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r6_re_r6_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c', value='#xD;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR6.xsd",
        instance="msData/regex/reR6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r5_re_r5_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c', value='#xA;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR5.xsd",
        instance="msData/regex/reR5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_r4_re_r4_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c', value='#x20;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR4.xsd",
        instance="msData/regex/reR4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r3_re_r3_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c', value='a', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR3.xsd",
        instance="msData/regex/reR3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r2_re_r2_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c', value=':', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR2.xsd",
        instance="msData/regex/reR2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_r1_re_r1_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c', value='_', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reR1.xsd",
        instance="msData/regex/reR1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q24_re_q24_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='a\I+\c', value='a123 123cc',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ24.xsd",
        instance="msData/regex/reQ24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q23_re_q23_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='a\I+\c', value='b123c',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ23.xsd",
        instance="msData/regex/reQ23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q22_re_q22_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='a\I+\c', value='a 123c',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ22.xsd",
        instance="msData/regex/reQ22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q21_re_q21_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\I*', value='1234',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ21.xsd",
        instance="msData/regex/reQ21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q20_re_q20_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\I', value='#x9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ20.xsd",
        instance="msData/regex/reQ20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q19_re_q19_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\I', value='#xD;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ19.xsd",
        instance="msData/regex/reQ19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q18_re_q18_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\I', value='#xA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ18.xsd",
        instance="msData/regex/reQ18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q17_re_q17_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\I', value='#x20;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ17.xsd",
        instance="msData/regex/reQ17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q16_re_q16_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\I', value='a', type='invalid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ16.xsd",
        instance="msData/regex/reQ16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q15_re_q15_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\I', value=':', type='invalid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ15.xsd",
        instance="msData/regex/reQ15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q14_re_q14_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\I', value='_', type='invalid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ14.xsd",
        instance="msData/regex/reQ14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q13_re_q13_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='[\s\i]*', value='1',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ13.xsd",
        instance="msData/regex/reQ13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q12_re_q12_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='[\s\i]*', value='a b c Z :_
    d#xd;y #x9;b #xa;#x20; ', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ12.xsd",
        instance="msData/regex/reQ12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q11_re_q11_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c\i*a', value='ab',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ11.xsd",
        instance="msData/regex/reQ11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q10_re_q10_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\c\i*a', value='zabcsdea',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ10.xsd",
        instance="msData/regex/reQ10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q9_re_q9_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\i+', value='a b',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ9.xsd",
        instance="msData/regex/reQ9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q8_re_q8_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\i*',
    value='_:abcdefghijklmnopqrstuvwxyzAZ:_', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ8.xsd",
        instance="msData/regex/reQ8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q7_re_q7_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\i', value='#x9;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ7.xsd",
        instance="msData/regex/reQ7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q6_re_q6_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\i', value='#xD;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ6.xsd",
        instance="msData/regex/reQ6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q5_re_q5_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\i', value='#xA;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ5.xsd",
        instance="msData/regex/reQ5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_q4_re_q4_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\i', value='#x20;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ4.xsd",
        instance="msData/regex/reQ4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q3_re_q3_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\i', value='a', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ3.xsd",
        instance="msData/regex/reQ3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q2_re_q2_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\i', value=':', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ2.xsd",
        instance="msData/regex/reQ2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_q1_re_q1_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\i', value='_', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reQ1.xsd",
        instance="msData/regex/reQ1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p30_re_p30_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S?\s?\S?\s+', value='ab',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP30.xsd",
        instance="msData/regex/reP30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p29_re_p29_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S?\s?\S?\s+', value=' a b',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP29.xsd",
        instance="msData/regex/reP29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p28_re_p28_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S?\s?\S?\s+', value='a b',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP28.xsd",
        instance="msData/regex/reP28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p27_re_p27_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S?\s?\S?\s+', value=' a #xD;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP27.xsd",
        instance="msData/regex/reP27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p26_re_p26_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S?\s?\S?\s+', value='a b#x9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP26.xsd",
        instance="msData/regex/reP26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p25_re_p25_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S*', value='', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP25.xsd",
        instance="msData/regex/reP25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p24_re_p24_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S+', value='a#x20;b',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP24.xsd",
        instance="msData/regex/reP24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p23_re_p23_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S', value='aa',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP23.xsd",
        instance="msData/regex/reP23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p22_re_p22_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S', value='#x9;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP22.xsd",
        instance="msData/regex/reP22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p21_re_p21_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S', value='#xD;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP21.xsd",
        instance="msData/regex/reP21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p20_re_p20_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S', value='#xA;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP20.xsd",
        instance="msData/regex/reP20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p19_re_p19_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S', value='#x20;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP19.xsd",
        instance="msData/regex/reP19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p18_re_p18_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\S', value='a', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP18.xsd",
        instance="msData/regex/reP18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p17_re_p17_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s', value='#x20;#xA;',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP17.xsd",
        instance="msData/regex/reP17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p16_re_p16_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s', value=' ', type='invalid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP16.xsd",
        instance="msData/regex/reP16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p15_re_p15_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='a\s{0,3}a', value='aa a',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP15.xsd",
        instance="msData/regex/reP15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p14_re_p14_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='a\s{0,3}a', value='a a',
    type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP14.xsd",
        instance="msData/regex/reP14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p13_re_p13_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='a\s{0,3}a', value='a a',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP13.xsd",
        instance="msData/regex/reP13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p12_re_p12_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='a\s{0,3}a', value='a a',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP12.xsd",
        instance="msData/regex/reP12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p11_re_p11_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='a\s{0,3}a', value='aa',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP11.xsd",
        instance="msData/regex/reP11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p10_re_p10_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s*\c\s?\c\s+\c\s*', value=' a
    aa ', type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP10.xsd",
        instance="msData/regex/reP10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p9_re_p9_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s*\c\s?\c\s+\c\s*',
    value='aaa', type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP9.xsd",
        instance="msData/regex/reP9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p8_re_p8_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s*\c\s?\c\s+\c\s*', value=' a
    a a', type='invalid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP8.xsd",
        instance="msData/regex/reP8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p7_re_p7_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s*\c\s?\c\s+\c\s*', value='aa
    a', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP7.xsd",
        instance="msData/regex/reP7.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p6_re_p6_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s*\c\s?\c\s+\c\s*', value='
    #x20;#x9;#xa;#xD;a c#xA;#x9;#xD;#x20;a#x20;#xA;#xD;#x9;
    #x20;#x20;#xD;#xa;', type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP6.xsd",
        instance="msData/regex/reP6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_p5_re_p5_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s', value='a', type='invalid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP5.xsd",
        instance="msData/regex/reP5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p4_re_p4_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s', value='#x9;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP4.xsd",
        instance="msData/regex/reP4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p3_re_p3_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s', value='#xD;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP3.xsd",
        instance="msData/regex/reP3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p2_re_p2_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s', value='#xA;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP2.xsd",
        instance="msData/regex/reP2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_p1_re_p1_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\s', value='#x20;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reP1.xsd",
        instance="msData/regex/reP1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_o4_re_o4_i(mode, save_output):
    """
    TEST :branch : base='string', pattern='.', value='', type='invalid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reO4.xsd",
        instance="msData/regex/reO4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_o3_re_o3_i(mode, save_output):
    """
    TEST :branch : base='string', pattern='.', value='aa', type='invalid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reO3.xsd",
        instance="msData/regex/reO3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_o2_re_o2_v(mode, save_output):
    """
    TEST :branch : base='string', pattern='.', value='#x20;',
    type='valid', RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reO2.xsd",
        instance="msData/regex/reO2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_o1_re_o1_v(mode, save_output):
    """
    TEST :branch : base='string', pattern='.', value='a', type='valid',
    RULE='37'
    """
    assert_bindings(
        schema="msData/regex/reO1.xsd",
        instance="msData/regex/reO1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n99_re_n99_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsPrivateUse}',
    value='#xFFFFD;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN99.xsd",
        instance="msData/regex/reN99.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n98_re_n98_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsPrivateUse}',
    value='#xE007F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN98.xsd",
        instance="msData/regex/reN98.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n97_re_n97_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsTags}', value='#x2FA1F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN97.xsd",
        instance="msData/regex/reN97.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n96_re_n96_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKCompatibilityIdeographsSupplement}',
    value='#x2A6D6;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN96.xsd",
        instance="msData/regex/reN96.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n95_re_n95_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKUnifiedIdeographsExtensionB}', value='#x1D7FF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN95.xsd",
        instance="msData/regex/reN95.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n94_re_n94_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsMathematicalAlphanumericSymbols}', value='#x1D1FF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN94.xsd",
        instance="msData/regex/reN94.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n93_re_n93_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMusicalSymbols}',
    value='#x1D0FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN93.xsd",
        instance="msData/regex/reN93.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n92_re_n92_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsByzantineMusicalSymbols}',
    value='#x1044F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN92.xsd",
        instance="msData/regex/reN92.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n91_re_n91_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsDeseret}',
    value='#x1034F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN91.xsd",
        instance="msData/regex/reN91.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n90_re_n90_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGothic}',
    value='#x1032F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN90.xsd",
        instance="msData/regex/reN90.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n89_re_n89_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsOldItalic}',
    value='#xFFFD;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN89.xsd",
        instance="msData/regex/reN89.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n88_re_n88_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSpecials}',
    value='#xFFEF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN88.xsd",
        instance="msData/regex/reN88.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n87_re_n87_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsHalfwidthandFullwidthForms}', value='#xFEFF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN87.xsd",
        instance="msData/regex/reN87.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n86_re_n86_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSpecials}',
    value='#xFEFE;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN86.xsd",
        instance="msData/regex/reN86.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n85_re_n85_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsArabicPresentationForms-B}', value='#xFE6F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN85.xsd",
        instance="msData/regex/reN85.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n84_re_n84_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSmallFormVariants}',
    value='#xFE4F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN84.xsd",
        instance="msData/regex/reN84.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n83_re_n83_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKCompatibilityForms}',
    value='#xFE2F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN83.xsd",
        instance="msData/regex/reN83.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n82_re_n82_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCombiningHalfMarks}',
    value='#xFDFF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN82.xsd",
        instance="msData/regex/reN82.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n81_re_n81_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsArabicPresentationForms-A}', value='#xFB4F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN81.xsd",
        instance="msData/regex/reN81.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n80_re_n80_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsAlphabeticPresentationForms}', value='#xFAFF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN80.xsd",
        instance="msData/regex/reN80.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n79_re_n79_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKCompatibilityIdeographs}', value='#xF8FF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN79.xsd",
        instance="msData/regex/reN79.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n75_re_n75_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHighSurrogates}',
    value='&#xD7A3;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN75.xsd",
        instance="msData/regex/reN75.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n74_re_n74_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHangulSyllables}',
    value='#xA4CF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN74.xsd",
        instance="msData/regex/reN74.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n73_re_n73_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsYiRadicals}',
    value='#xA48F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN73.xsd",
        instance="msData/regex/reN73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n72_re_n72_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsYiSyllables}',
    value='#x9FFF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN72.xsd",
        instance="msData/regex/reN72.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n71_re_n71_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKUnifiedIdeographs}',
    value='#x4DB5;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN71.xsd",
        instance="msData/regex/reN71.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n70_re_n70_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKUnifiedIdeographsExtensionA}', value='#x33FF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN70.xsd",
        instance="msData/regex/reN70.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n69_re_n69_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKCompatibility}',
    value='#x32FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN69.xsd",
        instance="msData/regex/reN69.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n68_re_n68_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsEnclosedCJKLettersandMonths}', value='#x31BF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN68.xsd",
        instance="msData/regex/reN68.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n67_re_n67_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBopomofoExtended}',
    value='#x319F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN67.xsd",
        instance="msData/regex/reN67.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n66_re_n66_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKanbun}', value='#x318F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN66.xsd",
        instance="msData/regex/reN66.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n65_re_n65_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHangulCompatibilityJamo}',
    value='#x312F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN65.xsd",
        instance="msData/regex/reN65.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n64_re_n64_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBopomofo}',
    value='#x30FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN64.xsd",
        instance="msData/regex/reN64.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n63_re_n63_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKatakana}',
    value='#x309F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN63.xsd",
        instance="msData/regex/reN63.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n62_re_n62_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHiragana}',
    value='#x303F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN62.xsd",
        instance="msData/regex/reN62.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n61_re_n61_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKSymbolsandPunctuation}', value='#x2FFF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN61.xsd",
        instance="msData/regex/reN61.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n60_re_n60_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsIdeographicDescriptionCharacters}', value='#x2FDF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN60.xsd",
        instance="msData/regex/reN60.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n59_re_n59_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKangxiRadicals}',
    value='#x2EFF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN59.xsd",
        instance="msData/regex/reN59.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n58_re_n58_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKRadicalsSupplement}',
    value='#x28FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN58.xsd",
        instance="msData/regex/reN58.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n57_re_n57_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBraillePatterns}',
    value='#x27BF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN57.xsd",
        instance="msData/regex/reN57.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n56_re_n56_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsDingbats}',
    value='#x26FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN56.xsd",
        instance="msData/regex/reN56.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n55_re_n55_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMiscellaneousSymbols}',
    value='#x25FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN55.xsd",
        instance="msData/regex/reN55.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n54_re_n54_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeometricShapes}',
    value='#x259F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN54.xsd",
        instance="msData/regex/reN54.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n53_re_n53_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBlockElements}',
    value='#x257F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN53.xsd",
        instance="msData/regex/reN53.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n52_re_n52_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBoxDrawing}',
    value='#x24FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN52.xsd",
        instance="msData/regex/reN52.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n51_re_n51_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsEnclosedAlphanumerics}',
    value='#x245F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN51.xsd",
        instance="msData/regex/reN51.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n50_re_n50_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsOpticalCharacterRecognition}', value='#x243F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN50.xsd",
        instance="msData/regex/reN50.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n49_re_n49_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsControlPictures}',
    value='#x23FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN49.xsd",
        instance="msData/regex/reN49.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n48_re_n48_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMiscellaneousTechnical}',
    value='#x22FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN48.xsd",
        instance="msData/regex/reN48.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n47_re_n47_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMathematicalOperators}',
    value='#x21FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN47.xsd",
        instance="msData/regex/reN47.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n46_re_n46_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsArrows}', value='#x218F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN46.xsd",
        instance="msData/regex/reN46.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n45_re_n45_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsNumberForms}',
    value='#x214F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN45.xsd",
        instance="msData/regex/reN45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n44_re_n44_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLetterlikeSymbols}',
    value='#x20FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN44.xsd",
        instance="msData/regex/reN44.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n43_re_n43_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCombiningMarksforSymbols}', value='#x20CF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN43.xsd",
        instance="msData/regex/reN43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n42_re_n42_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCurrencySymbols}',
    value='#x209F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN42.xsd",
        instance="msData/regex/reN42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n41_re_n41_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsSuperscriptsandSubscripts}', value='#x206F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN41.xsd",
        instance="msData/regex/reN41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n40_re_n40_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeneralPunctuation}',
    value='#x1FFF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN40.xsd",
        instance="msData/regex/reN40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n39_re_n39_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGreekExtended}',
    value='#x1EFF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN39.xsd",
        instance="msData/regex/reN39.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n38_re_n38_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatinExtendedAdditional}',
    value='#x18AF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN38.xsd",
        instance="msData/regex/reN38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n37_re_n37_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMongolian}',
    value='#x17FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN37.xsd",
        instance="msData/regex/reN37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n36_re_n36_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKhmer}', value='#x16FF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN36.xsd",
        instance="msData/regex/reN36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n35_re_n35_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsRunic}', value='#x169F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN35.xsd",
        instance="msData/regex/reN35.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n34_re_n34_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsOgham}', value='#x167F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN34.xsd",
        instance="msData/regex/reN34.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n33_re_n33_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsUnifiedCanadianAboriginalSyllabics}', value='#x13FF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN33.xsd",
        instance="msData/regex/reN33.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n32_re_n32_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCherokee}',
    value='#x137F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN32.xsd",
        instance="msData/regex/reN32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n31_re_n31_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsEthiopic}',
    value='#x11FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN31.xsd",
        instance="msData/regex/reN31.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n30_re_n30_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHangulJamo}',
    value='#x10FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN30.xsd",
        instance="msData/regex/reN30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n29_re_n29_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeorgian}',
    value='#x109F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN29.xsd",
        instance="msData/regex/reN29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n28_re_n28_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMyanmar}',
    value='#x0FFF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN28.xsd",
        instance="msData/regex/reN28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n27_re_n27_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsTibetan}',
    value='#x0EFF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN27.xsd",
        instance="msData/regex/reN27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n26_re_n26_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLao}', value='#x0E7F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN26.xsd",
        instance="msData/regex/reN26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n25_re_n25_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsThai}', value='#x0DFF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN25.xsd",
        instance="msData/regex/reN25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n24_re_n24_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSinhala}',
    value='#x0D7F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN24.xsd",
        instance="msData/regex/reN24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n23_re_n23_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMalayalam}',
    value='#x0CFF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN23.xsd",
        instance="msData/regex/reN23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n22_re_n22_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKannada}',
    value='#x0C7F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN22.xsd",
        instance="msData/regex/reN22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n21_re_n21_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsTelugu}', value='#x0BFF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN21.xsd",
        instance="msData/regex/reN21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n20_re_n20_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsTamil}', value='#x0B7F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN20.xsd",
        instance="msData/regex/reN20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n19_re_n19_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsOriya}', value='#x0AFF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN19.xsd",
        instance="msData/regex/reN19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n18_re_n18_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGujarati}',
    value='#x0A7F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN18.xsd",
        instance="msData/regex/reN18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n17_re_n17_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGurmukhi}',
    value='#x09FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN17.xsd",
        instance="msData/regex/reN17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n16_re_n16_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBengali}',
    value='#x097F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN16.xsd",
        instance="msData/regex/reN16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n15_re_n15_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsDevanagari}',
    value='#x07BF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN15.xsd",
        instance="msData/regex/reN15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n14_re_n14_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsThaana}', value='#x074F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN14.xsd",
        instance="msData/regex/reN14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n13_re_n13_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSyriac}', value='#x06FF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN13.xsd",
        instance="msData/regex/reN13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n12_re_n12_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsArabic}', value='#x05FF;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN12.xsd",
        instance="msData/regex/reN12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n11_re_n11_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHebrew}', value='#x058F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN11.xsd",
        instance="msData/regex/reN11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n10_re_n10_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsArmenian}',
    value='#x04FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN10.xsd",
        instance="msData/regex/reN10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n9_re_n9_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCyrillic}',
    value='#x03FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN9.xsd",
        instance="msData/regex/reN9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n8_re_n8_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGreek}', value='#x036F;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN8.xsd",
        instance="msData/regex/reN8.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n6_re_n6_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSpacingModifierLetters}',
    value='#x02AF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN6.xsd",
        instance="msData/regex/reN6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n5_re_n5_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsIPAExtensions}',
    value='#x024F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN5.xsd",
        instance="msData/regex/reN5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n4_re_n4_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatinExtended-B}',
    value='#x017F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN4.xsd",
        instance="msData/regex/reN4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n3_re_n3_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatinExtended-A}',
    value='#x00FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN3.xsd",
        instance="msData/regex/reN3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n2_re_n2_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatin-1Supplement}',
    value='#x007F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN2.xsd",
        instance="msData/regex/reN2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_n1_re_n1_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBasicLatin}',
    value='#x06FF;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reN1.xsd",
        instance="msData/regex/reN1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m99_re_m99_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsPrivateUse}?',
    value='#x007F;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM99.xsd",
        instance="msData/regex/reM99.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m98_re_m98_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsPrivateUse}?',
    value='#x100000;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM98.xsd",
        instance="msData/regex/reM98.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m97_re_m97_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsTags}?', value='#xF0000;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM97.xsd",
        instance="msData/regex/reM97.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m96_re_m96_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKCompatibilityIdeographsSupplement}?',
    value='#xE0000;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM96.xsd",
        instance="msData/regex/reM96.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m95_re_m95_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKUnifiedIdeographsExtensionB}?', value='#x2F800;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM95.xsd",
        instance="msData/regex/reM95.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m94_re_m94_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsMathematicalAlphanumericSymbols}?', value='#x20000;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM94.xsd",
        instance="msData/regex/reM94.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m93_re_m93_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMusicalSymbols}?',
    value='#x1D400;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM93.xsd",
        instance="msData/regex/reM93.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m92_re_m92_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsByzantineMusicalSymbols}?', value='#x1D100;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM92.xsd",
        instance="msData/regex/reM92.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m91_re_m91_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsDeseret}?',
    value='#x1D000;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM91.xsd",
        instance="msData/regex/reM91.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m90_re_m90_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGothic}?',
    value='#x10400;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM90.xsd",
        instance="msData/regex/reM90.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m89_re_m89_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsOldItalic}?',
    value='#x10330;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM89.xsd",
        instance="msData/regex/reM89.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m88_re_m88_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSpecials}?',
    value='#x10300;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM88.xsd",
        instance="msData/regex/reM88.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m87_re_m87_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsHalfwidthandFullwidthForms}?', value='#xFFF0;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM87.xsd",
        instance="msData/regex/reM87.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m86_re_m86_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSpecials}?',
    value='#xFF00;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM86.xsd",
        instance="msData/regex/reM86.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m84_re_m84_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSmallFormVariants}?',
    value='#xFE70;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM84.xsd",
        instance="msData/regex/reM84.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m83_re_m83_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKCompatibilityForms}?',
    value='#xFE50;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM83.xsd",
        instance="msData/regex/reM83.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m82_re_m82_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCombiningHalfMarks}?',
    value='#xFE30;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM82.xsd",
        instance="msData/regex/reM82.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m81_re_m81_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsArabicPresentationForms-A}?', value='#xFE20;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM81.xsd",
        instance="msData/regex/reM81.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m80_re_m80_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsAlphabeticPresentationForms}?', value='#xFB50;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM80.xsd",
        instance="msData/regex/reM80.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m79_re_m79_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKCompatibilityIdeographs}?', value='#xFB00;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM79.xsd",
        instance="msData/regex/reM79.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m78_re_m78_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsPrivateUse}?',
    value='#xF900;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM78.xsd",
        instance="msData/regex/reM78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m77_re_m77_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLowSurrogates}?',
    value='#xE000;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM77.xsd",
        instance="msData/regex/reM77.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m73_re_m73_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsYiRadicals}?',
    value='#xAC00;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM73.xsd",
        instance="msData/regex/reM73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m72_re_m72_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsYiSyllables}?',
    value='#xA490;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM72.xsd",
        instance="msData/regex/reM72.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m71_re_m71_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKUnifiedIdeographs}?',
    value='#xA000;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM71.xsd",
        instance="msData/regex/reM71.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m70_re_m70_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKUnifiedIdeographsExtensionA}?', value='#x4E00;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM70.xsd",
        instance="msData/regex/reM70.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m69_re_m69_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKCompatibility}?',
    value='#x3400;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM69.xsd",
        instance="msData/regex/reM69.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m68_re_m68_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsEnclosedCJKLettersandMonths}?', value='#x3300;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM68.xsd",
        instance="msData/regex/reM68.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m67_re_m67_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBopomofoExtended}?',
    value='#x3200;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM67.xsd",
        instance="msData/regex/reM67.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m66_re_m66_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKanbun}?',
    value='#x31A0;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM66.xsd",
        instance="msData/regex/reM66.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m65_re_m65_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsHangulCompatibilityJamo}?', value='#x3190;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM65.xsd",
        instance="msData/regex/reM65.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m64_re_m64_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBopomofo}?',
    value='#x3130;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM64.xsd",
        instance="msData/regex/reM64.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m63_re_m63_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKatakana}?',
    value='#x3100;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM63.xsd",
        instance="msData/regex/reM63.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m62_re_m62_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHiragana}?',
    value='#x30A0;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM62.xsd",
        instance="msData/regex/reM62.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m61_re_m61_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKSymbolsandPunctuation}?', value='#x3040;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM61.xsd",
        instance="msData/regex/reM61.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m60_re_m60_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsIdeographicDescriptionCharacters}?', value='#x3000;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM60.xsd",
        instance="msData/regex/reM60.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m59_re_m59_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKangxiRadicals}?',
    value='#x2FF0;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM59.xsd",
        instance="msData/regex/reM59.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m58_re_m58_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKRadicalsSupplement}?',
    value='#x2F00;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM58.xsd",
        instance="msData/regex/reM58.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m57_re_m57_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBraillePatterns}?',
    value='#x2E80;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM57.xsd",
        instance="msData/regex/reM57.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m56_re_m56_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsDingbats}?',
    value='#x2800;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM56.xsd",
        instance="msData/regex/reM56.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m55_re_m55_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMiscellaneousSymbols}?',
    value='#x2700;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM55.xsd",
        instance="msData/regex/reM55.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m54_re_m54_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeometricShapes}?',
    value='#x2600;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM54.xsd",
        instance="msData/regex/reM54.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m53_re_m53_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBlockElements}?',
    value='#x25A0;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM53.xsd",
        instance="msData/regex/reM53.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m52_re_m52_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBoxDrawing}?',
    value='#x2580;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM52.xsd",
        instance="msData/regex/reM52.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m51_re_m51_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsEnclosedAlphanumerics}?',
    value='#x2500;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM51.xsd",
        instance="msData/regex/reM51.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m50_re_m50_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsOpticalCharacterRecognition}?', value='#x2460;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM50.xsd",
        instance="msData/regex/reM50.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m49_re_m49_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsControlPictures}?',
    value='#x2440;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM49.xsd",
        instance="msData/regex/reM49.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m48_re_m48_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMiscellaneousTechnical}?',
    value='#x2400;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM48.xsd",
        instance="msData/regex/reM48.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m47_re_m47_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMathematicalOperators}?',
    value='#x2300;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM47.xsd",
        instance="msData/regex/reM47.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m46_re_m46_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsArrows}?',
    value='#x2200;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM46.xsd",
        instance="msData/regex/reM46.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m45_re_m45_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsNumberForms}?',
    value='#x2190;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM45.xsd",
        instance="msData/regex/reM45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m44_re_m44_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLetterlikeSymbols}?',
    value='#x2150;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM44.xsd",
        instance="msData/regex/reM44.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m43_re_m43_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCombiningMarksforSymbols}?', value='#x2100;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM43.xsd",
        instance="msData/regex/reM43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m42_re_m42_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCurrencySymbols}?',
    value='#x20D0;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM42.xsd",
        instance="msData/regex/reM42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m41_re_m41_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsSuperscriptsandSubscripts}?', value='#x20A0;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM41.xsd",
        instance="msData/regex/reM41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m40_re_m40_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeneralPunctuation}?',
    value='#x2070;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM40.xsd",
        instance="msData/regex/reM40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m39_re_m39_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGreekExtended}?',
    value='#x2000;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM39.xsd",
        instance="msData/regex/reM39.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m38_re_m38_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsLatinExtendedAdditional}?', value='#x1F00;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM38.xsd",
        instance="msData/regex/reM38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m37_re_m37_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMongolian}?',
    value='#x1E00;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM37.xsd",
        instance="msData/regex/reM37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m36_re_m36_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKhmer}?', value='#x1800;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM36.xsd",
        instance="msData/regex/reM36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m35_re_m35_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsRunic}?', value='#x1780;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM35.xsd",
        instance="msData/regex/reM35.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m34_re_m34_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsOgham}?', value='#x16A0;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM34.xsd",
        instance="msData/regex/reM34.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m33_re_m33_i(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsUnifiedCanadianAboriginalSyllabics}?', value='#x1680;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM33.xsd",
        instance="msData/regex/reM33.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m32_re_m32_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCherokee}?',
    value='#x1400;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM32.xsd",
        instance="msData/regex/reM32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m31_re_m31_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsEthiopic}?',
    value='#x13A0;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM31.xsd",
        instance="msData/regex/reM31.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m30_re_m30_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHangulJamo}?',
    value='#x1200;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM30.xsd",
        instance="msData/regex/reM30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m29_re_m29_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeorgian}?',
    value='#x1100;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM29.xsd",
        instance="msData/regex/reM29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m28_re_m28_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMyanmar}?',
    value='#x10A0;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM28.xsd",
        instance="msData/regex/reM28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m27_re_m27_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsTibetan}?',
    value='#x1000;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM27.xsd",
        instance="msData/regex/reM27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m26_re_m26_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLao}?', value='#x0F00;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM26.xsd",
        instance="msData/regex/reM26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m25_re_m25_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsThai}?', value='#x0E80;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM25.xsd",
        instance="msData/regex/reM25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m24_re_m24_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSinhala}?',
    value='#x0E00;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM24.xsd",
        instance="msData/regex/reM24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m23_re_m23_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMalayalam}?',
    value='#x0D80;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM23.xsd",
        instance="msData/regex/reM23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m22_re_m22_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKannada}?',
    value='#x0D00;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM22.xsd",
        instance="msData/regex/reM22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m21_re_m21_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsTelugu}?',
    value='#x0C80;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM21.xsd",
        instance="msData/regex/reM21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m20_re_m20_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsTamil}?', value='#x0C00;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM20.xsd",
        instance="msData/regex/reM20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m19_re_m19_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsOriya}?', value='#x0B80;',
    type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM19.xsd",
        instance="msData/regex/reM19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m18_re_m18_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGujarati}?',
    value='#x0B00;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM18.xsd",
        instance="msData/regex/reM18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m17_re_m17_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGurmukhi}?',
    value='#x0A80;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM17.xsd",
        instance="msData/regex/reM17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m16_re_m16_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBengali}?',
    value='#x0A00;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM16.xsd",
        instance="msData/regex/reM16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m15_re_m15_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsDevanagari}?',
    value='#x0980;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM15.xsd",
        instance="msData/regex/reM15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m14_re_m14_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsThaana}?',
    value='#x0900;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM14.xsd",
        instance="msData/regex/reM14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m13_re_m13_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSyriac}?',
    value='#x0780;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM13.xsd",
        instance="msData/regex/reM13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m12_re_m12_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsArabic}?',
    value='#x0700;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM12.xsd",
        instance="msData/regex/reM12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m11_re_m11_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHebrew}?',
    value='#x0600;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM11.xsd",
        instance="msData/regex/reM11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m10_re_m10_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsArmenian}?',
    value='#x0590;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM10.xsd",
        instance="msData/regex/reM10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m9_re_m9_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCyrillic}?',
    value='#x0530;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM9.xsd",
        instance="msData/regex/reM9.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m6_re_m6_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSpacingModifierLetters}?',
    value='#x0300;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM6.xsd",
        instance="msData/regex/reM6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m5_re_m5_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsIPAExtensions}?',
    value='#x02B0;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM5.xsd",
        instance="msData/regex/reM5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m4_re_m4_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatinExtended-B}?',
    value='#x0250;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM4.xsd",
        instance="msData/regex/reM4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m3_re_m3_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatinExtended-A}?',
    value='#x0180;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM3.xsd",
        instance="msData/regex/reM3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m2_re_m2_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatin-1Supplement}?',
    value='#x0100;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM2.xsd",
        instance="msData/regex/reM2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_m1_re_m1_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBasicLatin}?',
    value='#x0080;', type='invalid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reM1.xsd",
        instance="msData/regex/reM1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_l99_re_l99_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsPrivateUse}+',
    value='#x100000;#x10FFFD;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL99.xsd",
        instance="msData/regex/reL99.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_l98_re_l98_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsPrivateUse}+',
    value='#xF0000;#xFFFFD;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL98.xsd",
        instance="msData/regex/reL98.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l88_re_l88_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSpecials}+',
    value='#xFFF0;#xFFFD;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL88.xsd",
        instance="msData/regex/reL88.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l87_re_l87_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsHalfwidthandFullwidthForms}+', value='#xFF00;#xFFEF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL87.xsd",
        instance="msData/regex/reL87.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l85_re_l85_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsArabicPresentationForms-B}+', value='#xFE70;#xFEFE;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL85.xsd",
        instance="msData/regex/reL85.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l84_re_l84_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSmallFormVariants}+',
    value='#xFE50;#xFE6F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL84.xsd",
        instance="msData/regex/reL84.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l83_re_l83_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKCompatibilityForms}+',
    value='#xFE30;#xFE4F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL83.xsd",
        instance="msData/regex/reL83.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l82_re_l82_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCombiningHalfMarks}+',
    value='#xFE20;#xFE2F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL82.xsd",
        instance="msData/regex/reL82.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l81_re_l81_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsArabicPresentationForms-A}+', value='#xFB50;#xFDFF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL81.xsd",
        instance="msData/regex/reL81.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l80_re_l80_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsAlphabeticPresentationForms}+', value='#xFB00;#xFB4F;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL80.xsd",
        instance="msData/regex/reL80.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l79_re_l79_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKCompatibilityIdeographs}+', value='#xF900;#xFAFF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL79.xsd",
        instance="msData/regex/reL79.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l78_re_l78_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsPrivateUse}+',
    value='#xE000;#xF8FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL78.xsd",
        instance="msData/regex/reL78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l74_re_l74_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHangulSyllables}+',
    value='#xAC00;#xD7A3;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL74.xsd",
        instance="msData/regex/reL74.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l73_re_l73_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsYiRadicals}+',
    value='#xA490;#xA4CF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL73.xsd",
        instance="msData/regex/reL73.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l72_re_l72_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsYiSyllables}+',
    value='#xA000;#xA48F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL72.xsd",
        instance="msData/regex/reL72.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l71_re_l71_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKUnifiedIdeographs}+',
    value='#x4E00;#x9FFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL71.xsd",
        instance="msData/regex/reL71.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l70_re_l70_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKUnifiedIdeographsExtensionA}+',
    value='#x3400;#x4DB5;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL70.xsd",
        instance="msData/regex/reL70.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l69_re_l69_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKCompatibility}+',
    value='#x3300;#x33FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL69.xsd",
        instance="msData/regex/reL69.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l68_re_l68_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsEnclosedCJKLettersandMonths}+', value='#x3200;#x32FF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL68.xsd",
        instance="msData/regex/reL68.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l67_re_l67_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBopomofoExtended}+',
    value='#x31A0;#x31BF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL67.xsd",
        instance="msData/regex/reL67.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l66_re_l66_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKanbun}+',
    value='#x3190;#x319F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL66.xsd",
        instance="msData/regex/reL66.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l65_re_l65_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsHangulCompatibilityJamo}+', value='#x3130;#x318F;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL65.xsd",
        instance="msData/regex/reL65.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l64_re_l64_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBopomofo}+',
    value='#x3100;#x312F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL64.xsd",
        instance="msData/regex/reL64.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l63_re_l63_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKatakana}+',
    value='#x30A0;#x30FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL63.xsd",
        instance="msData/regex/reL63.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l62_re_l62_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHiragana}+',
    value='#x3040;#x309F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL62.xsd",
        instance="msData/regex/reL62.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l61_re_l61_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCJKSymbolsandPunctuation}+', value='#x3000;#x303F;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL61.xsd",
        instance="msData/regex/reL61.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l60_re_l60_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsIdeographicDescriptionCharacters}+',
    value='#x2FF0;#x2FFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL60.xsd",
        instance="msData/regex/reL60.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l59_re_l59_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKangxiRadicals}+',
    value='#x2F00;#x2FDF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL59.xsd",
        instance="msData/regex/reL59.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l58_re_l58_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCJKRadicalsSupplement}+',
    value='#x2E80;#x2EFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL58.xsd",
        instance="msData/regex/reL58.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l57_re_l57_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBraillePatterns}+',
    value='#x2800;#x28FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL57.xsd",
        instance="msData/regex/reL57.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l56_re_l56_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsDingbats}+',
    value='#x2700;#x27BF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL56.xsd",
        instance="msData/regex/reL56.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l55_re_l55_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMiscellaneousSymbols}+',
    value='#x2600;#x26FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL55.xsd",
        instance="msData/regex/reL55.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l54_re_l54_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeometricShapes}+',
    value='#x25A0;#x25FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL54.xsd",
        instance="msData/regex/reL54.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l53_re_l53_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBlockElements}+',
    value='#x2580;#x259F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL53.xsd",
        instance="msData/regex/reL53.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l52_re_l52_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBoxDrawing}+',
    value='#x2500;#x257F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL52.xsd",
        instance="msData/regex/reL52.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l51_re_l51_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsEnclosedAlphanumerics}+',
    value='#x2460;#x24FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL51.xsd",
        instance="msData/regex/reL51.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l50_re_l50_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsOpticalCharacterRecognition}+', value='#x2440;#x245F;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL50.xsd",
        instance="msData/regex/reL50.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l49_re_l49_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsControlPictures}+',
    value='#x2400;#x243F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL49.xsd",
        instance="msData/regex/reL49.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l48_re_l48_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMiscellaneousTechnical}+',
    value='#x2300;#x23FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL48.xsd",
        instance="msData/regex/reL48.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l47_re_l47_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMathematicalOperators}+',
    value='#x2200;#x22FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL47.xsd",
        instance="msData/regex/reL47.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l46_re_l46_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsArrows}+',
    value='#x2190;#x21FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL46.xsd",
        instance="msData/regex/reL46.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l45_re_l45_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsNumberForms}+',
    value='#x2150;#x218F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL45.xsd",
        instance="msData/regex/reL45.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l44_re_l44_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLetterlikeSymbols}+',
    value='#x2100;#x214F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL44.xsd",
        instance="msData/regex/reL44.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l43_re_l43_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsCombiningMarksforSymbols}+', value='#x20D0;#x20FF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL43.xsd",
        instance="msData/regex/reL43.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l42_re_l42_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCurrencySymbols}+',
    value='#x20A0;#x20CF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL42.xsd",
        instance="msData/regex/reL42.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l41_re_l41_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsSuperscriptsandSubscripts}+', value='#x2070;#x209F;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL41.xsd",
        instance="msData/regex/reL41.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l40_re_l40_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeneralPunctuation}+',
    value='#x2000;#x206F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL40.xsd",
        instance="msData/regex/reL40.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l39_re_l39_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGreekExtended}+',
    value='#x1F00;#x1FFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL39.xsd",
        instance="msData/regex/reL39.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l38_re_l38_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsLatinExtendedAdditional}+', value='#x1E00;#x1EFF;',
    type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL38.xsd",
        instance="msData/regex/reL38.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l37_re_l37_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMongolian}+',
    value='#x1800;#x18AF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL37.xsd",
        instance="msData/regex/reL37.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l36_re_l36_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKhmer}+',
    value='#x1780;#x17FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL36.xsd",
        instance="msData/regex/reL36.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l35_re_l35_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsRunic}+',
    value='#x16A0;#x16FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL35.xsd",
        instance="msData/regex/reL35.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l34_re_l34_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsOgham}+',
    value='#x1680;#x169F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL34.xsd",
        instance="msData/regex/reL34.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l33_re_l33_v(mode, save_output):
    r"""
    TEST :branch : base='string',
    pattern='\p{IsUnifiedCanadianAboriginalSyllabics}+',
    value='#x1400;#x167F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL33.xsd",
        instance="msData/regex/reL33.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l32_re_l32_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsCherokee}+',
    value='#x13A0;#x13FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL32.xsd",
        instance="msData/regex/reL32.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l31_re_l31_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsEthiopic}+',
    value='#x1200;#x137F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL31.xsd",
        instance="msData/regex/reL31.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l30_re_l30_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHangulJamo}+',
    value='#x1100;#x11FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL30.xsd",
        instance="msData/regex/reL30.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l29_re_l29_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGeorgian}+',
    value='#x10A0;#x10FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL29.xsd",
        instance="msData/regex/reL29.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l28_re_l28_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMyanmar}+',
    value='#x1000;#x109F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL28.xsd",
        instance="msData/regex/reL28.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l27_re_l27_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsTibetan}+',
    value='#x0F00;#x0FFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL27.xsd",
        instance="msData/regex/reL27.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l26_re_l26_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLao}+',
    value='#x0E80;#x0EFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL26.xsd",
        instance="msData/regex/reL26.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l25_re_l25_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsThai}+',
    value='#x0E00;#x0E7F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL25.xsd",
        instance="msData/regex/reL25.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l24_re_l24_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSinhala}+',
    value='#x0D80;#x0DFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL24.xsd",
        instance="msData/regex/reL24.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l23_re_l23_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsMalayalam}+',
    value='#x0D00;#x0D7F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL23.xsd",
        instance="msData/regex/reL23.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l22_re_l22_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsKannada}+',
    value='#x0C80;#x0CFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL22.xsd",
        instance="msData/regex/reL22.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l21_re_l21_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsTelugu}+',
    value='#x0C00;#x0C7F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL21.xsd",
        instance="msData/regex/reL21.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l20_re_l20_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsTamil}+',
    value='#x0B80;#x0BFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL20.xsd",
        instance="msData/regex/reL20.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l19_re_l19_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsOriya}+',
    value='#x0B00;#x0B7F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL19.xsd",
        instance="msData/regex/reL19.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l18_re_l18_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGujarati}+',
    value='#x0A80;#x0AFF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL18.xsd",
        instance="msData/regex/reL18.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l17_re_l17_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsGurmukhi}+',
    value='#x0A00;#x0A7F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL17.xsd",
        instance="msData/regex/reL17.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l16_re_l16_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBengali}+',
    value='#x0980;#x09FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL16.xsd",
        instance="msData/regex/reL16.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l15_re_l15_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsDevanagari}+',
    value='#x0900;#x097F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL15.xsd",
        instance="msData/regex/reL15.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l14_re_l14_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsThaana}+',
    value='#x0780;#x07BF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL14.xsd",
        instance="msData/regex/reL14.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l13_re_l13_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSyriac}+',
    value='#x0700;#x074F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL13.xsd",
        instance="msData/regex/reL13.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l12_re_l12_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsArabic}+',
    value='#x0600;#x06FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL12.xsd",
        instance="msData/regex/reL12.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l11_re_l11_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsHebrew}+',
    value='#x0590;#x05FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL11.xsd",
        instance="msData/regex/reL11.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l10_re_l10_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsArmenian}+',
    value='#x0530;#x058F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL10.xsd",
        instance="msData/regex/reL10.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l6_re_l6_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsSpacingModifierLetters}+',
    value='#x02B0;#x02FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL6.xsd",
        instance="msData/regex/reL6.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l5_re_l5_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsIPAExtensions}+',
    value='#x0250;#x02AF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL5.xsd",
        instance="msData/regex/reL5.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l4_re_l4_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatinExtended-B}+',
    value='#x0180;#x024F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL4.xsd",
        instance="msData/regex/reL4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l3_re_l3_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatinExtended-A}+',
    value='#x0100;#x017F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL3.xsd",
        instance="msData/regex/reL3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l2_re_l2_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsLatin-1Supplement}+',
    value='#x0080;#x00FF;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL2.xsd",
        instance="msData/regex/reL2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_l1_re_l1_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsBasicLatin}+',
    value='#x9;#xA;#xD;#x20;#x007F;', type='valid', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reL1.xsd",
        instance="msData/regex/reL1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_k88_re_k88_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\p{IsaA0-a9}', value='',
    type='error', RULE='25,36'
    """
    assert_bindings(
        schema="msData/regex/reK88.xsd",
        instance="msData/regex/reK88.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_k85_re_k85_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\\\p{L}*', value='a',
    type='invalid', RULE='25,26'
    """
    assert_bindings(
        schema="msData/regex/reK85.xsd",
        instance="msData/regex/reK85.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_k84_re_k84_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\\\p{L}*', value='\a',
    type='valid', RULE='25,26'
    """
    assert_bindings(
        schema="msData/regex/reK84.xsd",
        instance="msData/regex/reK84.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_k78_re_k78_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\P{Co}*', value='#x2044;',
    type='valid', RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK78.xsd",
        instance="msData/regex/reK78.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_k77_re_k77_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\P{Co}*',
    value='#xE000;#x100000;#xF0000;#xFFFFD;#x10FFFD;', type='invalid',
    RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK77.xsd",
        instance="msData/regex/reK77.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_k76_re_k76_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\P{Cf}*', value='#xE000;',
    type='valid', RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK76.xsd",
        instance="msData/regex/reK76.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_re_k75_re_k75_i(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\P{Cf}*',
    value='#x70F;#xE0078;', type='invalid', RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK75.xsd",
        instance="msData/regex/reK75.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )


def test_re_k74_re_k74_v(mode, save_output):
    r"""
    TEST :branch : base='string', pattern='\P{Cc}*', value='#x070F;',
    type='valid', RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK74.xsd",
        instance="msData/regex/reK74.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
    )
