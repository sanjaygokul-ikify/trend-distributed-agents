import logging
from typing import List, Dict
import uuid
from .types import Agent, Task, MemorySystem, ReasoningEngine
from .exceptions import RegistrationError, TaskAssignmentError

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
        self.tasks: Dict[str, Task] = {}
        self.memory_system: MemorySystem = None
        self.reasoning_engine: ReasoningEngine = None

    def register_agent(self, agent: Agent) -> str:
        agent_id = str(uuid.uuid4())
        if agent_id in self.agents:
            raise RegistrationError(f"Agent with id {agent_id} already exists")
        self.agents[agent_id] = agent
        logger.info(f"Registered agent with id {agent_id}")
        return agent_id

    def assign_task(self, agent_id: str, task: Task) -> str:
        if agent_id not in self.agents:
            raise TaskAssignmentError(f"Agent with id {agent_id} does not exist")
        task_id = str(uuid.uuid4())
        self.tasks[task_id] = task
        logger.info(f"Assigned task with id {task_id} to agent with id {agent_id}")
        return task_id

    def retrieve_data(self, task_id: str) -> Dict:
        if task_id not in self.tasks:
            raise TaskAssignmentError(f"Task with id {task_id} does not exist")
        task = self.tasks[task_id]
        if not self.memory_system:
            raise ValueError("Memory system is not initialized")
        data = self.memory_system.retrieve_data(task.data_id)
        logger.info(f"Retrieved data for task with id {task_id}")
        return data

    def perform_inference(self, task_id: str) -> Dict:
        if task_id not in self.tasks:
            raise TaskAssignmentError(f"Task with id {task_id} does not exist")
        task = self.tasks[task_id]
        if not self.memory_system:
            raise ValueError("Memory system is not initialized")
        if not self.reasoning_engine:
            raise ValueError("Reasoning engine is not initialized")
        data = self.retrieve_data(task_id)
        inference_result = self.reasoning_engine.perform_inference(data)
        logger.info(f"Performed inference for task with id {task_id}")
        return inference_result