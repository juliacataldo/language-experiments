WORD–SENTENCE FIVE-POINT RATING TASK
=====================================

WHAT THIS VERSION DOES
----------------------
Each trial displays:
1. A word
2. A sentence
3. A five-point rating scale

Participants may respond by:
- clicking one of the visible buttons numbered 1–5; or
- pressing the corresponding number key 1–5.

EXPERIMENT STRUCTURE
--------------------
1. Brief explanation and consent
2. Full instructions
3. Tree practice trials with confirmation of the chosen rating
4. Option to continue or repeat practice
5. Four main blocks
6. Three pauses
7. Language survey
7. Final screen
8. Local or DataPipe saving

REQUIRED FILES
--------------
Place these files in your experiment folder:

FOFC_experiment/
├── exp1.html
├── main_stimuli.csv
├── serve.py
├── data/
└── jspsych/
    ├── jspsych.js
    ├── jspsych.css
    ├── plugin-html-keyboard-response.js
    └── saveData.js

EDITING THE MAIN STIMULI
------------------------
Required columns:
- item_id: unique item identifier
- block: 1, 2, 3, or 4
- condition: condition name or label
- word: word shown at the top
- sentence: sentence shown beneath the word

You may add any additional columns. Every additional column is automatically
preserved in the output CSV.

Because sentences may contain commas, save the file from Excel as:
CSV UTF-8 (Comma delimited) (.csv)

Do not change the filename unless you also change:
var MAIN_STIMULI_FILE = "main_stimuli.csv";
inside index.html.

EDITING THE QUESTION AND LABELS
-------------------------------
Near the top of index.html, edit:

var RATING_QUESTION =
  "How well does the sentence describe the meaning of the word?";

var LOW_ENDPOINT_LABEL = "1 — Very poorly";
var HIGH_ENDPOINT_LABEL = "5 — Very well";

LOCAL TESTING
-------------
In Terminal:

cd /Users/juliacataldo/Library/CloudStorage/OneDrive-Personal/FOFC_experiment
python3 serve.py

Open:
http://localhost:8000/index.html

Local results are written into:
FOFC_experiment/data/

Do not double-click index.html because the browser must fetch main_stimuli.csv.

GITHUB PAGES + DATAPIPE + OSF
-----------------------------
1. In index.html, replace:
   PASTE_YOUR_DATAPIPE_EXPERIMENT_ID_HERE

   with the Experiment ID shown in DataPipe.

2. Do not put your OSF token in index.html or GitHub. Store it only in your
   private DataPipe account settings.

3. Upload these to the GitHub repository:
   - index.html
   - main_stimuli.csv
   - jspsych/jspsych.js
   - jspsych/jspsych.css
   - jspsych/plugin-html-keyboard-response.js
   - jspsych/saveData.js

4. Do not upload serve.py or the local data folder unless you intentionally
   want them in the repository.

5. Enable GitHub Pages from the repository's main branch and root folder.

MODE SELECTION
--------------
The HTML selects its saving mode automatically:

localhost / 127.0.0.1 / 0.0.0.0
    -> saveData.js + serve.py -> local data folder

GitHub Pages or another online hostname
    -> jsPsychPipe -> DataPipe -> OSF

RESULT COLUMNS
--------------
Important trial-level columns include:
- participant_id
- run_mode
- item_id
- block
- condition
- word
- sentence
- rating
- response
- response_method
- rt
- task
- phase

response_method is either:
- keyboard
- button


LANGUAGE-BACKGROUND QUESTIONNAIRE
---------------------------------
A one-page language-background and dominance questionnaire now appears after
the four experimental blocks and before the data-saving trial.

Its answers are stored in the same participant CSV on a row with:
task = language_background_survey

Questionnaire columns begin with language_, including:
language_gender
language_age
language_education
language_daily_languages
language_home_other_language
language_home_languages
language_home_exposure_years
language_home_relative_use
language_school_work_other_language
language_school_work_languages
language_school_work_exposure_years
language_school_work_relative_use
language_brazil_growing_up_years
language_current_country
language_current_country_years
language_lived_other_language_places
language_other_language_places
language_language_background_comments
