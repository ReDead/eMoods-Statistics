# eMoods-Statistics

## Setup

1. Clone the github repository.
2. Go to your emoods app. Navigate to `Settings > Manual Backup > Generate Backup File`. This should give you a `.emoods` file.
3. Get the backup file onto your computer. You can email it to yourself, put it in google drive, etc.
4. Move the `.emoods` file into the root directory of the cloned repository.
5. Extract the file.
    - **For Windows Users:** Run the `extract.bat` file.
    - **For Linux Users:** Run the `extract.sh` file.
    - **If that doesn't work:** Rename the file from `filename.emoods` to `filename.zip` and unzip it like any other zip file into the folder `eMoods-data` within the repository.

## Execution

To run the program, simply run the `main.py` file with python3.

## Configuration

This project includes a `constants.py` file which you can modify to alter the behavior of the program. It mostly just affects the output of the program. You can change certain styling aspects and where the output files are sent. However, **DO NOT** modify the variables below the `DO NOT MODIFY` line. These variables are used to make the program run correctly and interact with eMoods data correctly.