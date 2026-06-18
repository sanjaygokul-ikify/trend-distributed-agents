import unittest
from packages.core import Engine, Agent, Task

class TestCore(unittest.TestCase):
    def test_register_agent(self):
        engine = Engine()
        agent_id = engine.register_agent(Agent('Test Agent', ['capability1', 'capability2']))
        self.assertIsNotNone(agent_id)

    def test_assign_task(self):
        engine = Engine()
        agent_id = engine.register_agent(Agent('Test Agent', ['capability1', 'capability2']))
        task_id = engine.assign_task(agent_id, Task('Test Task', 'Test Description', 'test_data_id'))
        self.assertIsNotNone(task_id)

    def test_retrieve_data(self):
        engine = Engine()
        engine.memory_system = Engine.MemorySystem()
        engine.memory_system.store_data('test_data_id', {'key': 'value'})
        agent_id = engine.register_agent(Agent('Test Agent', ['capability1', 'capability2']))
        task_id = engine.assign_task(agent_id, Task('Test Task', 'Test Description', 'test_data_id'))
        data = engine.retrieve_data(task_id)
        self.assertEqual(data, {'key': 'value'})

    def test_perform_inference(self):
        engine = Engine()
        engine.memory_system = Engine.MemorySystem()
        engine.memory_system.store_data('test_data_id', {'key': 'value'})
        engine.reasoning_engine = Engine.ReasoningEngine()
        agent_id = engine.register_agent(Agent('Test Agent', ['capability1', 'capability2']))
        task_id = engine.assign_task(agent_id, Task('Test Task', 'Test Description', 'test_data_id'))
        inference_result = engine.perform_inference(task_id)
        self.assertEqual(inference_result, {'result': 'inference performed'})