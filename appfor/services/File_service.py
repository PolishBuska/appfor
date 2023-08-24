from django.core.files import uploadedfile
from abc import ABC,abstractmethod
class FileInterface(ABC):
    def __init__(self):
        self.path = None,
        self.file = None,
        self.filename = None,
    @abstractmethod
    def __hashfilename__(self):
        raise NotImplementedError
    @abstractmethod
    def accept_file_data(self):
        raise NotImplementedError
