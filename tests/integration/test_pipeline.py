import unittest
from services.orchestrator import Orchestrator

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.orchestrator = Orchestrator()

    def test_full_pipeline(self):
        agent_id = self.orchestrator.register_agent(Agent('Test Agent', ['capability1', 'capability2']))
        task_id = self.orchestrator.assign_task(agent_id, Task('Test Task', 'Test Description', 'test_data_id'))
        data = {'key': 'value'}
        self.orchestrator.engine.memory_system = Engine.MemorySystem()
        self.orchestrator.engine.memory_system.store_data('test_data_id', data)
        retrieved_data = self.orchestrator.retrieve_data(task_id)
        self.assertEqual(retrieved_data, data)
        self.orchestrator.engine.reasoning_engine = Engine.ReasoningEngine()
        inference_result = self.orchestrator.perform_inference(task_id)
        self.assertEqual(inference_result, {'result': 'inference performed'})