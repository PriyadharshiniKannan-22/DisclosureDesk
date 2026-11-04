class StreamResult:
    """Collects usage while a stream is consumed (filled in by the provider)."""
    def __init__(self) -> None:
    self.usage = Usage()
    self.model = "" # added for Session 5: which model actually answered
    self.fallback_used = False # added for Session 5

# ... LLMProvider and LLMError stay as they are ...

class LLMUnavailable(LLMError):
    """Added for Session 5: the provider was down, slow or rate-limited after every retry.
    Only this error switches to the fallback model; a bad key (401) or wrong model (404)
    is a configuration bug that the fallback must not hide."""