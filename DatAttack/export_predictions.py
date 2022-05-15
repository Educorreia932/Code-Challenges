""" 
This is a reference script for exporting predictions with the expected format for submission.
In this example, predictions are randomly generated.
Participants should customize the `export_predictions` method to get the predictions from their model.
"""

import os
import random
import pandas as pd

TEAM_NAME = "TriceraTOP"
TEST_DIR = "dataset/test"

def export_predictions(images_dir: str, team_name: str, *args) -> None:
    """
    Go through all images, get the predicted strings and export them to .csv

    Args:
        images_dir (str): the path to the images' folder
        team_name (str): the name of the team to include in the exported .csv file
    """
    
    predictions = []

    for image in os.listdir(images_dir):
        
        # get predictions
        predicted_string_1 = str(random.randint(1e9, 1e10))
        predicted_string_2 = str(random.randint(1e8, 1e9))
        
        # store predictions
        predictions.append({"image_name": image, 
                            "string_1_prediction": predicted_string_1, 
                            "string_2_prediction": predicted_string_2})

    # export predictions
    results_df = pd.DataFrame(predictions)
    results_df.to_csv(f"submissions/{team_name}.csv", index=False, header=True)


if __name__ == "__main__":
    
    export_predictions(TEST_DIR, TEAM_NAME)

