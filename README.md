### How to Use

### NOTE : Run `sudo apt-get install libicu-dev libpango1.0-dev libcairo2-dev` and `sudo apt-get install automake ca-certificates g++ git libtool libleptonica-dev make pkg-config` first to make the training tools. Also install tesseract-ocr with `sudo apt-get install tesseract-ocr`

#### Note: Please Remove the .gitignore files from data/fonts and data/output before using this repository

#### Step 1: Setting Up The Structure for the Repository

    .
    ├── data
    |     ├── fonts
    |     ├── lang_data
    |     ├── output
    |     └── tess_data
    └── generate_training_data.sh
  
  
#### Note: if you're training an english font, you can skip step 2.

#### Step 2: Downloading Relavent Data
- Place the font you want to train in the fonts folder.
- download from link: https://github.com/tesseract-ocr/langdata and place the data inside the lang_data.
- go to link: https://github.com/tesseract-ocr/ download one specific language from either tessdata_best or tessdata_fast based on your application requirement and place that inside the tessdata folder.
- Updating the variables in script, now since the scripts were written taking english language into consideration you'll have to update those variables to reflect
your language you need to train the system on. the scripts that require updation are as following
    - `evaluate.sh where (eng.*) needs to be changed to required (lang.*)`
    - `extract_model.sh where (eng.*) needs to be changed to required (lang.*)`
    - `generate_training_data.sh has a variable called --lang eng is where the eng would be replcaed with your lang`
    - `train.sh where (eng.*) needs to be changed to required (lang.*)`

#### Step 3: Changing the parameters in the generate_training_data.sh and train.sh
1. In generate_training_data.sh
- Rename the font list to the name of your font
- change the page from 10 (which was used for testing) to 250 which seems to be a good number to avoid overfitting
2. In train.sh
- change --max_iterations to anything that you think would be suitable for your font

#### Step 4: Running the pipeline
run the command: `execute_train_pipeline.sh`

The pipeline will do the following things:
1. Construct the data from the font
2. Extract the Model for further fine tuning
3. train the model on the new font, the new model will be saved in finetuned_model

#### Step 4: Run `combine.sh` to get .traineddata from your output

#### Step 5 (Optional): Run `evaluate.sh` to evaluate how accurate your new .traineddata is

Thanks to : https://github.com/UYousafzai/easy_train_tesseract/tree/fonts
