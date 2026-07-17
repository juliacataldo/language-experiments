MASKED PRIMING: LOCAL + GITHUB PAGES + DATAPIPE
====================================================

FILES IN THIS PACKAGE
---------------------
- index.html
  Use this name in the root of a GitHub Pages repository so the experiment
  opens at the repository's main Pages URL.

- lexicaldecision_masked_priming_datapipe.html
  An identical copy with a descriptive filename.

- main_stimuli.csv
  Main-experiment stimuli. Edit this file in Excel and save it as:
  CSV UTF-8 (Comma delimited) (.csv)

The HTML still expects your existing local files:
- jspsych/jspsych.js
- jspsych/jspsych.css
- jspsych/plugin-html-keyboard-response.js
- jspsych/saveData.js
- serve.py

REQUIRED CSV COLUMNS
--------------------
item_id,block,condition,prime,target,lexicality,correct_response

Rules:
- item_id must be unique.
- block must be 1, 2, 3, or 4.
- lexicality must be word or nonword.
- correct_response must be f or j.
- Additional columns are allowed. They will automatically be included as
  columns in each main_target row of the result file.

ONE REQUIRED HTML EDIT FOR ONLINE COLLECTION
--------------------------------------------
Find:

var DATAPIPE_EXPERIMENT_ID =
  "PASTE_YOUR_DATAPIPE_EXPERIMENT_ID_HERE";

Replace only the placeholder text with the Experiment ID shown by DataPipe.
Do not paste an OSF Personal Access Token into the HTML or GitHub repository.

LOCAL MODE
----------
The HTML automatically chooses local mode when the hostname is localhost,
127.0.0.1, or 0.0.0.0.

1. Put index.html and main_stimuli.csv in FOFC_experiment.
2. Keep serve.py and the jspsych folder there too.
3. In Terminal:

   cd /Users/juliacataldo/Library/CloudStorage/OneDrive-Personal/FOFC_experiment
   python3 serve.py

4. Open:

   http://localhost:8000/index.html

5. At the end, serve.py writes the CSV into FOFC_experiment/data/.

Do not double-click index.html. Browser file:// pages cannot reliably fetch the
external main_stimuli.csv file.

ONLINE MODE
-----------
Every non-local hostname, including GitHub Pages, automatically uses DataPipe.

1. Create an OSF project.
2. Create an OSF Personal Access Token with the scope required by DataPipe.
3. Store that token only in DataPipe Account Settings.
4. Create a DataPipe experiment linked to the OSF project.
5. Enable data collection in DataPipe.
6. Paste the DataPipe Experiment ID into index.html.
7. Upload to the root of the GitHub repository:
   - index.html
   - main_stimuli.csv
   - the jspsych/ folder
8. Do not upload serve.py or the local data/ folder; they are not needed online.
9. In GitHub: Settings > Pages > Deploy from a branch > main > /(root).
10. Open the GitHub Pages URL and complete a full test. Confirm that a CSV
    appears in the OSF component before recruiting participants.

AUTOMATIC MODE SELECTION
------------------------
http://localhost:8000/...          -> local saveData.js + serve.py
https://USERNAME.github.io/...     -> jsPsychPipe + DataPipe + OSF

The same HTML and main_stimuli.csv are used in both modes.

PARTICIPANT IDS
---------------
The file checks for either of these URL parameters:

?participant_id=P001
?PROLIFIC_PID=your_prolific_id

When neither is present, jsPsych generates a random 10-character ID. Result
filenames also contain a UTC timestamp to avoid overwriting repeated sessions.


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
