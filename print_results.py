
#       Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
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
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    print('\n\nResults for {} CNN model architecture.\n'.format(model.title()))
    print('Number of images: {}'.format(results_stats_dic['n_images']))
    print('Number of dog images: {}'.format(results_stats_dic['n_dogs_img']))
    print('Number of not dog images: {}\n'.format(
        results_stats_dic['n_notdogs_img']))

    for key, value in results_stats_dic.items():
        if key[0] == "p":
            print('{}: {}'.format(key, value))

    if (print_incorrect_dogs and ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
                                  != results_stats_dic['n_images'])):
        print("\nIncorrectly Classified Dogs:")

        for value in results_dic.values():
            if value[3] != value[4]:
                print("Real: {:20}, Classifier: {}".format(value[0], value[1]))

    if (print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\nIncorrectly Classified Breeds:")

        for value in results_dic.values():
            if value[3] and value[4] and (not value[2]):
                print("Real: {:20}, Classifier: {}".format(value[0], value[1]))
