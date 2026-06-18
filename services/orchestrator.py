from packages.core import Engine

class Orchestrator:
    def __init__(self):
        self.engine = Engine()

    def register_agent(self, agent):
        return self.engine.register_agent(agent)

    def assign_task(self, agent_id, task):
        return self.engine.assign_task(agent_id, task)

    def retrieve_data(self, task_id):
        return self.engine.retrieve_data(task_id)

    def perform_inference(self, task_id):
        return self.engine.perform_inference(task_id)