from caesar_cipher import __version__
import pytest
from caesar_cipher.cipher import encrypt,decrypt,crack

def test_version():
    assert __version__ == '0.1.0'



    # encrypt a string with a given shift
    # encryption should handle upper and lower case letters
def test_ncrypt_a_string_with_a_given_shift():
    actual=encrypt("Sara",4)
    expected="Weve"
    assert actual==expected

    # decrypt a previously encrypted string with the same shift
def test_decrypt_previously_encrypted_string_with_the_same_shift():
    actual=decrypt("Weve",4)
    expected="Sara"
    assert actual==expected
  
    # encryption should allow non-alpha characters but ignore them, including white space
def test_encryption_should_allow_non_alpha_characters():
    actual=encrypt("Sara like python 3",3)
    expected="Vdud olnh sbwkrq 3"
    assert actual==expected

    # decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
def test_crack_without_shift():
    encrypt_text=encrypt("It was the best of times, it was the worst of times",3)
    actual=crack(encrypt_text)
    expected="It was the best of times, it was the worst of times"
    assert actual==expected