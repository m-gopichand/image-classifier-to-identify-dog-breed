
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the classroom Item XX Calculating Results for details
                     on how to calculate the counts and statistics.
    """

    results_stats_dic = {'n_images': len(results_dic),
                         'n_dogs_img': sum(list(zip(*[value for value in results_dic.values()]))[3]),
                         'n_notdogs_img': 0,
                         'n_match': sum(list(zip(*[value for value in results_dic.values()]))[2]),
                         'n_correct_dogs': 0,
                         'n_correct_notdogs': 0,
                         'n_correct_breed': 0,
                         'pct_match': 0,
                         'pct_correct_dogs': 0,
                         'pct_correct_breed': 0,
                         'pct_correct_notdogs': 0}
    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']
    
    for result in results_dic.values():
        if result[3] and result[4]:
            results_stats_dic['n_correct_dogs'] += 1
        elif (not result[3]) and (not result[4]):
            results_stats_dic['n_correct_notdogs'] += 1
        if result[3] and result[2]:
            results_stats_dic['n_correct_breed'] += 1

    results_stats_dic['pct_match'] = results_stats_dic['n_match'] / results_stats_dic['n_images']*100
    results_stats_dic['pct_correct_dogs'] = results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']*100
    results_stats_dic['pct_correct_breed'] = results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']*100
    results_stats_dic['pct_correct_notdogs'] = results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']*100

    return results_stats_dic