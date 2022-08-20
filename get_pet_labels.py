
# Imports python modules
from os import listdir

#       Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    results_dic = {}
    images = [image for image in listdir(image_dir) if image[0]!='.']
    for image in images:
        results_dic[image] = [' '.join([value for value in (
            image.split('.')[0].split('_')) if value.isalpha()]).lower()]
    return results_dic


if __name__ == '__main__':
    from print_functions_for_lab_checks import *
    check_creating_pet_image_labels(get_pet_labels('pet_images'))
