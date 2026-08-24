# Continuous lexical-decision version

## Files

- `exp2_continuous_lexical_decision.html`: modified experiment.
- `main_stimuli_continuous.csv`: spreadsheet template loaded by the HTML.

Keep the CSV, HTML, `consent.pdf`, and the `jspsych` folder in the same experiment folder.

## Spreadsheet structure

Each CSV row is one complete prime-target pair. The required columns are:

- `pair_id`: unique identifier for the pair.
- `condition`: priming condition for the pair.
- `prime_item_id`: unique identifier for the prime item.
- `prime`: exact prime string displayed.
- `prime_lexicality`: `word` or `nonword`.
- `prime_correct_response`: `j` for word or `f` for nonword.
- `target_item_id`: unique identifier for the target item.
- `target`: exact target string displayed.
- `target_lexicality`: `word` or `nonword`.
- `target_correct_response`: `j` for word or `f` for nonword.

Extra columns are allowed and are copied to both the prime and target data rows.

## Trial order

The program shuffles complete pairs, divides them into four blocks, and expands each pair into two adjacent lexical-decision trials:

1. prime trial
2. target trial

The target is therefore always at lag 1 from its prime.

## Default timing

- fixation: 500 ms
- blank before stimulus: 200 ms
- stimulus display: 550 ms
- response deadline: 2000 ms from stimulus onset
- blank interval after response: randomly 650, 700, or 750 ms

These values are constants near the beginning of the HTML file.

## Main output columns

Each lexical-decision row includes:

- `pair_id`
- `condition`
- `pair_role` (`prime` or `target`)
- `pair_trial_position` (`1` or `2`)
- `item_id`
- `stimulus_item`
- `lexicality`
- `correct_response`
- `response`
- `correct`
- `rt`
- `paired_item_id`
- `paired_stimulus`
- `experimental_block`
- `block_pair_position`
- `randomized_pair_order`
- `block_trial`
- `randomized_trial_order`
- `iti_duration_ms`

Target rows additionally include the immediately preceding prime's response information:

- `preceding_prime_item_id`
- `preceding_prime_stimulus`
- `preceding_prime_response`
- `preceding_prime_correct`
- `preceding_prime_rt`
- `prime_target_pair_verified`
