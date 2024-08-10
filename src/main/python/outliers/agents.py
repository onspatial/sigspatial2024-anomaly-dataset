import random
import utils.constants as constants_utils
import utils.data.list as list_utils
import utils.debug as debug_utils

def get_random_agent_ids(max_agent_id, num_agents):
    seed = constants_utils.get_seed()
    random.seed(seed)
    agent_ids =  random.sample(range(0, max_agent_id), num_agents)
    return agent_ids

def get_labeled_agent_ids(agent_ids, labels=['RED', 'ORANGE', 'YELLOW']):
    results = {}
    start = 0
    end = 0
    for label in labels:
        end = end + len(agent_ids)//len(labels)
        results[label] = agent_ids[start:end]
        start = end
    return results

def print_labeled_agent_ids(labeled_agent_ids):
    for label, ids in labeled_agent_ids.items():
        print(f'{label}:\t{ids}')

def check_labeled_agent_ids(agent_ids,labeled_agent_ids):
    length = 0
    for ids in labeled_agent_ids.values():
        length = length + len(ids)
        for id in ids:
            if id not in agent_ids:
                print(f'Error: {id} not in agent_ids')
                return False
    if length != len(agent_ids):
        print(f'Error: length of labeled_agent_ids is not equal to length of agent_ids: {length} != {len(agent_ids)}')
        return False
    return True
    
def get_centralized_outliers_info(max_agent_id, total_outliers, labels=['RED', 'ORANGE', 'YELLOW'], test=True, verbose=False) -> dict:
    agent_ids  = get_random_agent_ids(max_agent_id, total_outliers)
    labeled_agent_ids = get_labeled_agent_ids(agent_ids,labels=labels)
    if test:
        assert check_labeled_agent_ids(agent_ids, labeled_agent_ids)
    if verbose:
        print_labeled_agent_ids(labeled_agent_ids)
    return labeled_agent_ids

def get_outliers_agents(max_agent_id, count):
    list_of_agents = list(range(0,max_agent_id))
    hunger_agents = list_utils.get_random_elements(list_of_agents, count)
    work_agents = list_utils.get_random_elements(list_of_agents, count)
    social_agents = list_utils.get_random_elements(list_of_agents, count)
    interest_agents = list_utils.get_random_elements(list_of_agents, count)
    combined_agents = hunger_agents + work_agents + social_agents + interest_agents
    agents ={
        'hunger_agents': hunger_agents,
        'work_agents': work_agents,
        'social_agents': social_agents,
        'interest_agents': interest_agents,
        'combined_agents': combined_agents
    }

    return agents
