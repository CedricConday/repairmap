# RepairMap

A checked, machine-readable table of clinical trials of myelin repair
(remyelination) therapies in multiple sclerosis (MS). One row per trial.

The table is one file: `data/trials.csv`. It holds 64 trials
of 39 agents as of 2026-11-23.

**Nothing here is medical advice.** This is a research table for people who
design and run trials. It says what was tested and what was reported. It does
not say what anyone should take. Several agents in it are prescription drugs
with real harms, and one trial arm in it was stopped for harm.

## What it is for

MS trial groups ask the same questions when they plan a repair trial. Which
agents have been tried? In whom? Against which outcome? What happened? The
answers sit in papers, registry records, conference talks and company
statements. This table puts them in one place, with the source of each row
and the date it was checked.

## How a row gets in

A trial gets a row when all of these hold. The full rule, with the judgement
calls, is in `docs/METHOD.md`.

1. It is an interventional trial in humans. It is on a trial registry, or
   published, or announced by its sponsor.
2. The participants have MS or a first demyelinating event such as optic
   neuritis. A healthy-volunteer study gets a row only when it is the only
   human trial of that agent so far.
3. The trial's paper, protocol or registry record names remyelination or
   myelin repair as an aim of the treatment, or as an outcome used to test it.
   Trials of an agent that was developed for repair also count.
4. The treatment is not an approved immune therapy for MS. Those are given to
   control inflammation, and they are left out even when a study measures
   repair on MRI.
5. One row per trial. A follow-up study gets its own row only when it reports
   its own comparison between the original groups.

Trials that were looked at and left out are listed, each with a reason, in
`docs/EXCLUDED.md`.

## Headline counts

Output of `repairmap summary` on 2026-11-23:

```
rows: 64   agents: 39
with a result on the primary outcome: 27
  biomarker primary: positive 4, mixed 1, negative 8
  functional primary: positive 1, mixed 1, negative 9
  safety primary: harm 1
  target_engagement primary: positive 1, mixed 1
without one: 37
  unclear 3, safety_only 11, ongoing 9, not_started 4, stopped 5, not_reported 5
checked a second time: 63 of 64
```

How to read this:

- 27 of the 64 trials have a result on their primary outcome. The other 37 are
  safety studies, are still running, were stopped, or never reported.
- "Positive" means the trial met its own primary outcome. It does not mean the
  treatment repairs myelin, and it does not mean patients felt better.
- The four trials with a positive biomarker result are small. Three measured
  the speed of the visual pathway (VEP latency): clemastine (ReBUILD),
  metformin plus clemastine (CCMR-Two) and the bexarotene follow-up. Their
  effects were 1.7 ms, 1.2 ms and 7.79 ms. The fourth, phenytoin in optic
  neuritis, measured nerve fibre loss in the retina, which is a sign of nerve
  protection and not of myelin repair.
- The one positive result on a functional outcome is the first biotin trial
  (MS-SPI, 154 patients). The larger trial that followed (SPI2, 642 patients)
  was negative.
- Nine trials with a functional primary outcome were negative. They include
  the four large antibody trials (opicinumab: SYNERGY and AFFINITY;
  elezanumab: RADIUS-R and RADIUS-P) and the selective M1 antagonist PIPE-307
  (VISTA).
- The one harm result is the clemastine arm of TRAP-MS in progressive MS.

## The columns

| Column | Meaning |
|---|---|
| `id` | Short name for the row. Lower-case words joined by hyphens. Stable. |
| `agent` | The drug, cell product, device or other treatment tested. |
| `trial` | The trial's own name or acronym. Empty when it has none. |
| `registry_id` | Registry number: NCT (ClinicalTrials.gov), ISRCTN, ACTRN or EudraCT. Empty when none was found. |
| `mechanism` | How the agent is thought to act, as the source describes it. "Not checked" when the source read does not say. |
| `phase` | Trial phase as the source gives it. `n/a` for device and exercise trials. |
| `n` | Number enrolled or randomised. For a trial that has not finished, the planned number; the `effect` cell then says "n is planned". Empty when not reported. |
| `population` | Who took part. |
| `primary_outcome` | The primary outcome as the source states it. |
| `outcome_class` | Kind of primary outcome: `biomarker` (a measurement such as VEP latency or an MRI measure), `functional` (disability, vision, walking), `safety`, or `target_engagement` (does the drug reach and act on its target). |
| `result` | See the list below. |
| `effect` | The numbers behind the result, and the caveats. |
| `source` | Where the row comes from: PMID, registry number, or a named page. |
| `source_type` | `paper`, `registry`, `conference` or `company`. |
| `source_date` | Date of the source: publication date, or the registry's last update. |
| `second_check` | `yes` when the source was read on `checked_on` and the row matches it. Otherwise `no`. |
| `checked_on` | Date of that check. |
| `check_note` | What was read (abstract, full text, registry record), and what was changed. |

Values of `result`:

| Value | Meaning |
|---|---|
| `positive` | Met its primary outcome. |
| `mixed` | Co-primary outcomes disagreed, or the result held only in one analysis set. |
| `negative` | Did not meet its primary outcome. |
| `harm` | Stopped or reported for harm. |
| `unclear` | Results exist but allow no call: no control group, or no test between groups. |
| `safety_only` | A safety study that reported safety and no efficacy result. |
| `ongoing` | Recruiting or running. |
| `not_started` | Registered or announced, not yet recruiting. |
| `stopped` | Withdrawn, suspended or terminated without a result. |
| `not_reported` | Finished, or status unknown, and no result was found. |

## Using it

Open `data/trials.csv` in any spreadsheet, or load it in code. The command
line tool needs Python 3.10 or later and nothing else.

```
pip install repairmap
repairmap check
repairmap summary
repairmap show clemastine-rebuild
repairmap list --result positive --outcome-class biomarker
repairmap list --agent metformin --format csv
```

`repairmap list --result positive --outcome-class biomarker` printed this on
2026-11-23:

```
4 of 64 trials
id                          agent                   phase  n   outcome_class  result    second_check
clemastine-rebuild          clemastine              2      50  biomarker      positive  yes
metformin-clemastine-ccmr2  metformin + clemastine  2a     70  biomarker      positive  yes
bexarotene-followup         bexarotene              2a     20  biomarker      positive  yes
phenytoin-optic-neuritis    phenytoin               2      86  biomarker      positive  yes
```

In Python:

```python
from repairmap import load, select

rows = load()
negative = select(rows, result="negative", outcome_class="functional")
```

## What is not verified

As of 2026-11-23:

- **Most paper rows were checked against the abstract only.** 30 of the 31
  paper rows rest on the PubMed abstract. One (the TRAP-MS clemastine arm) was
  checked against the full text. Each `check_note` says which. Numbers that
  appear only in the full paper are not in the table.
- **Three results come from conference reports, not papers:** CCMR-Two,
  ReWRAP (bazedoxifene) and VISIONARY-MS (CNM-Au8). No results paper was found
  on PubMed for any of them. The ReWRAP report read gives no numbers.
- **Four rows rest on company or trial-site statements:** PIPE-307 (VISTA),
  PIPE-791, the Octopus metformin arm and PTD802. None gives numbers. PTD802
  is the one row with `second_check` set to `no`.
- **The Octopus row is thin.** The arm size, the interim outcome measure, the
  phase and the registry number were not found on the page read.
- **Mechanism was not checked** for ifenprodil, olesoxime, EHP-101, PRO-1562
  and BIIB061. The cell says so.
- **PIPE-791:** neither source read states a remyelination aim for the trial.
  The row is kept from the first version of the table until a source settles it.
- **Registry numbers** for five rows were matched by title and size and are
  not stated in the paper abstract: both RADIUS trials, MS-SPI, the first
  rHIgM22 study and the liothyronine phase 1b study. The notes say so.
- **Every check was done once, by one reader, on one day.** The numbers in
  each row were then matched back to the saved source text by a script. Nobody
  else has reviewed the table.
- **Coverage is not proven complete.** The registry cross-check used
  ClinicalTrials.gov only. Trials registered only elsewhere (EU, UK, Japan,
  China, Iran, Australia) are in the table only if a name search or PubMed
  found them.
- **Registry records go stale.** A row marked `ongoing` reflects the record on
  its `source_date`.

## Reporting an error

Open an issue in this repository. Give the row `id`, the column, what it
should say, and the source that shows it (PMID, registry number or link). A
correction without a source cannot be applied.

## Licence

MIT. See `LICENSE`. The facts in the table come from the cited
papers and registry records; no table or text was copied from any review.
