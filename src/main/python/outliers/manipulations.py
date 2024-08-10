import outliers.type.work as work_utils
import outliers.type.hunger as hunger_utils
import outliers.type.social as social_utils
import outliers.type.interest as interest_utils
import outliers.type.combined as combined_utils
import utils.loops  as loop_utils

import outliers.json as json_utils

def get_method_manipulations_json(agent_ids, steps=8064, actor = "PERSON", method_name='setInitialOutlier', parameters=None):
    manipulations = []
    for agent_id in agent_ids:
        manipulations.append(json_utils.get_method_manipulations_json(agent_id, steps, method_name, parameters, actor=actor))

    return manipulations

def get_method_manipulations_json_by_options(parameters_options, agent_ids, actor, steps, method_name):
    output_json = []
    for p in loop_utils.product(*parameters_options):
        temp_json = get_method_manipulations_json(agent_ids, actor=actor, steps=steps, method_name=method_name, parameters=[e for e in p])
        output_json += temp_json
    return output_json
def get_hunger_outliers_json(outlier_agents_dict, outlier_start_tick, outlier_end_tick=None):
    results = hunger_utils.get_manipulation_json(outlier_agents_dict, outlier_start_tick, outlier_end_tick)
    return results
    
def get_work_outliers_json(outlier_agents_dict, outlier_start_tick, outlier_end_tick=None):
    results = work_utils.get_manipulation_json(outlier_agents_dict, outlier_start_tick, outlier_end_tick)
    return results

def get_social_outliers_json(outlier_agents_dict, outlier_start_tick, outlier_end_tick=None):
    results = social_utils.get_manipulation_json(outlier_agents_dict, outlier_start_tick, outlier_end_tick)
    return results
    
def get_interest_outliers_json(outlier_agents_dict, outlier_start_tick, outlier_end_tick=None):
    results = interest_utils.get_manipulation_json(outlier_agents_dict, outlier_start_tick, outlier_end_tick)
    return results

def get_combined_outliers_json(outlier_agents_dict, outlier_start_tick, outlier_end_tick=None):
    results, meta = combined_utils.get_manipulation_json(outlier_agents_dict, outlier_start_tick, outlier_end_tick)
    return results, meta