from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(Exception):
        encrypt_message(78, "caleidoscopio")
    assert encrypt_message("caleidoscopio", 78) == "oipocsodielac"
    assert encrypt_message("caleidoscopio", 12) == "o_ipocsodielac"
    assert encrypt_message("caleidoscopio", 3) == "lac_oipocsodie"
