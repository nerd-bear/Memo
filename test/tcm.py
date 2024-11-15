class TCM_FILE_NOT_LOADED(Exception):
    def __init__(self):
        error_message = '\nThe value you are getting is not available as the TCM_FILE object does not contain a loaded cache file. To load a cache file, please run load_tcm("./your_file_name.tcm", your_file_object)\n'

        super().__init__(error_message)
        self.message = error_message

    def __str__(self) -> str:
        return self.message


class TCM_FILE:
    def __init__(self, decoding: str = "utf-8"):
        """
        Initialize a new TCM_FILE object.

        This constructor sets up the initial state of the TCM_FILE object,
        including the decoding format and various attributes to store file data.

        Args:
            decoding (`str`, optional): The character encoding to be used for decoding the file content.
                                    Defaults to "utf-8".

        Attributes:
            decoding (`str`): The character encoding used for the file.
            loaded (`bool`): Flag indicating whether a file has been loaded.
            chars (`list`): List of characters from the decoded file content. (None by default and needs to be loaded)
            content (`list`): List of bytes representing the file content. (None by default and needs to be loaded)
            cache_state (`int`): The cache state of the file. (None by default and needs to be loaded)
            raw (`bytes`): The raw byte data of the file. (None by default and needs to be loaded)
        """
        self.decoding = decoding
        self.loaded = False
        self.chars = None
        self.content = None
        self.cache_state = None
        self.raw = None

    @property
    def text(self):
        return self.chars

    def __repr__(self) -> str:
        return str(self.content)

    def __str__(self) -> str:
        return str(self.content)

    def __getattribute__(self, name):
        if super().__getattribute__("loaded") == False and name in [
            "chars",
            "cache_state",
            "raw",
            "content",
        ]:
            raise TCM_FILE_NOT_LOADED

        return super().__getattribute__(name)


def load_tcm(_path: str, _tcm_file: TCM_FILE) -> bool:
    """
    Load a TCM file and populate the TCM_FILE object with its contents.

    This function reads a TCM file from the specified path, processes its contents,
    and updates the provided TCM_FILE object with the extracted information.

    Args:
        _path (`str`): The file path of the TCM file to be loaded.
        _tcm_file (`TCM_FILE`): The TCM_FILE object to be populated with the file contents.

    Returns:
        `bool` True if the file was successfully loaded and processed, False otherwise.
    """
    try:
        with open(_path, "rb") as _file:
            _tcm_file.raw = _file.read()
    except:
        return False

    _tcm_file.loaded = True

    _tokens: bytes = []

    for __byte in _tcm_file.raw:
        _tokens.append(__byte)

    _tcm_file.content = _tokens[70:-1]
    _tcm_file.cache_state = _tokens[66]
    _tcm_file.chars = [chr(i) for i in _tcm_file.content]
    return True


def write_tcn(_path: str, _tcm_file: TCM_FILE):
    """
    Write the contents of a TCM_FILE object to a file.

    This function attempts to write the raw data from a TCM_FILE object to a file
    at the specified path.

    Args:
        _path (`str`): The file path where the TCM file should be written.
        _tcm_file (`TCM_FILE`): The TCM_FILE object containing the data to be written.

    Returns:
        `bool` True if the file was successfully written, False if an error occurred.
    """
    try:
        with open(_path, "wb") as _file:
            _file.write(_tcm_file.raw)
    except:
        return False
    return True


file = TCM_FILE()
load_tcm("./test/test.tcm", file)

print(f"Decoding format: {file.decoding}")
print(f"Decoded file body/content: {file.chars}")
print(f"Cache state: {file.cache_state}")
print(f"Raw data: {file.raw}")
