import os
from typing import Optional, Tuple, Union
import hashlib


class SHA3:
    @staticmethod
    def salt_hash(
        input_str: str, salt: Optional[bytes] = None
    ) -> Tuple[Union[str, bytes], bytes]:
        """
        Generate a salted hash of the input string using PBKDF2 HMAC-SHA256.
        """
        if salt is None:
            salt = SHA3.generate_salt(size=32, isHex=True)
        encoded_str = str(input_str).encode("utf-8")
        hashed = hashlib.pbkdf2_hmac("sha256", encoded_str, salt, 100000)
        return salt, hashed

    @staticmethod
    def hash_256(input_str: str) -> str:
        """
        Generate a SHA-256 hash of the input string.
        """
        encoded_str = str(input_str).encode("utf-8")
        return hashlib.sha3_256(encoded_str).hexdigest()

    @staticmethod
    def hash_384(input_str: str) -> str:
        """
        Generate a SHA-384 hash of the input string.
        """
        encoded_str = str(input_str).encode("utf-8")
        return hashlib.sha3_384(encoded_str).hexdigest()

    @staticmethod
    def hash_512(input_str: str) -> str:
        """
        Generate a SHA-512 hash of the input string.
        """
        encoded_str = str(input_str).encode("utf-8")
        return hashlib.sha3_512(encoded_str).hexdigest()

    @staticmethod
    def hash_224(input_str: str) -> str:
        """
        Generate a SHA-224 hash of the input string.
        """
        encoded_str = str(input_str).encode("utf-8")
        return hashlib.sha3_224(encoded_str).hexdigest()

    @staticmethod
    def generate_salt(size: int = 32, isHex: bool = True) -> Union[str, bytes]:
        """
        Generate a random salt of the specified size.
        """
        salt = os.urandom(size).hex() if hex else os.urandom(size)
        return salt

    @staticmethod
    def compare_hash_to_salted(
        stored_salt: bytes, salted_and_hashed: bytes, hashed: str
    ) -> bool:
        """
        Compare a salted hash to a stored salted hash.
        """
        _, new_hash = SHA3.salt_hash(hashed, stored_salt)
        return new_hash == salted_and_hashed
