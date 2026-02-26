class ChatMemory:
    def __init__(self, max_messages: int = 10):
        """
        max_messages: total messages (user + assistant pairs * 2)
        """
        self.history = []
        self.max_messages = max_messages

    def add_user_message(self, message: str):
        self.history.append(("user", message))
        self._trim()

    def add_ai_message(self, message: str):
        self.history.append(("assistant", message))
        self._trim()

    def get_messages(self):
        """
        Returns messages in LangChain-compatible format
        """
        return self.history

    def get_formatted_history(self) -> str:
        """
        Returns history as string (useful for prompt injection)
        """
        return "\n".join(
            [f"{role}: {content}" for role, content in self.history]
        )

    def clear(self):
        self.history = []

    def _trim(self):
        """
        Keeps only last N messages
        """
        if len(self.history) > self.max_messages:
            self.history = self.history[-self.max_messages:]