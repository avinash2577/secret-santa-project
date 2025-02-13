class SecretSantaError(Exception):
    """Base exception class for Secret Santa application"""
    pass

class FileError(SecretSantaError):
    """Raised when there are issues with file operations"""
    pass

class AssignmentError(SecretSantaError):
    """Raised when there are issues with assignments"""
    pass

class ValidationError(SecretSantaError):
    """Raised when there are validation issues"""
    pass