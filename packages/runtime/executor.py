import logging
from .types import TrendAgentError

class TrendAgentExecutor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def execute(self, agent: Any) -> None:
        try:
            agent.execute()
        except Exception as e:
            self.logger.error(f"Error executing agent: {e}")
            raise TrendAgentError("Error executing agent") from e
