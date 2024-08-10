import utils.files.check as check_utils
import utils.files.search as search_utils
import utils.files.basics as file_basics
import utils.files.path as path_utils
import utils.data.list as list_utils

if __name__ == '__main__':
    
    # files_needed = search_utils.get_matching_files('.','DiseaseReports.tsv',regex=False)
    # # copy them to temp directory witht he same structure and directory name
    # for file in files_needed:
    #     folder_name = file.split('/')[-2]
    #     file_name = '/'.join(file.split('/')[-5:])
    #     des = f'DiseaseReports/{folder_name}/{file_name}'
    #     file_basics.copy(file, des)
        

    folders_all = path_utils.get_folders(['city_centralized_1','city_infectious_1','city_location_1'], path=True)
    # remove the folders that has /meta in them
    filter_strings = ['meta','brln','interest_outliers','combined_outliers','infectPopularPub','0.01','0.1']
    filtered_folders = list_utils.filter(folders_all, filter_strings, verbose=True)
    print('\n'.join(filtered_folders))
    
    
    print(f'all folders: {len(folders_all)} and filtered folders: {len(filtered_folders)}')