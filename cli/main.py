import argparse
from services.orchestrator import Orchestrator

orchestrator = Orchestrator()

parser = argparse.ArgumentParser(description='Distributed Agents CLI')
parser.add_argument('--action', type=str, help='Action to perform')
args = parser.parse_args()

if args.action == 'register_agent':
    agent = Agent('Test Agent', ['capability1', 'capability2'])
    print(orchestrator.register_agent(agent))
elif args.action == 'assign_task':
    agent_id = orchestrator.register_agent(Agent('Test Agent', ['capability1', 'capability2']))
    task = Task('Test Task', 'Test Description', 'test_data_id')
    print(orchestrator.assign_task(agent_id, task))
elif args.action == 'retrieve_data':
    task_id = orchestrator.assign_task(orchestrator.register_agent(Agent('Test Agent', ['capability1', 'capability2'])), Task('Test Task', 'Test Description', 'test_data_id'))
    print(orchestrator.retrieve_data(task_id))
elif args.action == 'perform_inference':
    task_id = orchestrator.assign_task(orchestrator.register_agent(Agent('Test Agent', ['capability1', 'capability2'])), Task('Test Task', 'Test Description', 'test_data_id'))
    print(orchestrator.perform_inference(task_id))