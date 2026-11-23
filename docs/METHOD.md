# Method

Written 2026-11-23. This describes how version 0.1.0 of the table was built.

Nothing in the table is medical advice.

## Inclusion rule

A trial gets a row when all five points hold.

1. **A trial in humans.** It is interventional. It is on a trial registry, or
   published, or announced by its sponsor. Trials that were withdrawn before
   enrolment, or announced and not yet started, are included: a trial that
   never ran is information too. Animal and laboratory studies are out.
2. **People with MS.** The participants have MS, or a first demyelinating
   event such as acute optic neuritis or clinically isolated syndrome. A
   healthy-volunteer study gets a row only when it is the only human trial of
   that agent so far, so that every agent that has reached people appears once.
3. **A stated repair aim.** The trial's paper, protocol or registry record
   names remyelination or myelin repair as an aim of the treatment, or as an
   outcome used to test it. A trial of an agent that was developed for repair
   counts even when that one trial was a safety study (for example the phase 1
   studies of opicinumab, elezanumab and rHIgM22). Neural stem cell and neural
   progenitor cell products count: they are given to repair.
4. **Not an approved immune therapy.** Interferons, natalizumab, alemtuzumab,
   cladribine and the like are left out, even where a study measures repair on
   MRI. They are given to control inflammation, and less new damage can look
   like repair on those measures.
5. **One row per trial.** Two trials in one paper get two rows. A follow-up
   study gets its own row only when it reports its own comparison between the
   original groups (RENEWED; the CCMR-One follow-up). Open-label extensions do
   not get a row.

Any kind of treatment can qualify: drugs, antibodies, cells, devices,
exercise.

### Judgement calls

The rule does not settle every case. These were decided by hand.

- **Mesenchymal stem cells are out; neural progenitor products are in.** The
  mesenchymal stem cell records name remyelination only as background, and
  the trials test safety and immune effects. The two New York trials use
  cells turned into neural progenitors and state repair as the purpose.
- **Octopus (metformin arm) is in.** Octopus tests nerve protection in
  progressive MS, not repair. It is kept because the trial's own page
  discusses what the result means for metformin as a myelin repair drug.
- **All three biotin trials are in.** Only the SPI2 abstract names repair. The
  other two are the same agent and the same programme.
- **Phenytoin is in.** Its registry record names remyelination as a secondary
  aim. Its primary outcome measures nerve fibre loss, and the row says so.
- **Two metformin add-on trials from Egypt are in.** Their primary outcomes
  are immune and blood markers, but each lists an MRI "degree of
  remyelination" as an outcome.
- **PIPE-791 is in for now.** Neither source read states a repair aim for the
  PET study. It is kept from the first version of the table and flagged.
- **Temelimab and nicotinamide riboside are out.** Neither registry record
  names a repair aim or outcome. See `EXCLUDED.md`.

## Where the rows came from

1. **A seed of 29 rows** from one literature pass on 2026-11-23.
2. **Searches by agent name** on ClinicalTrials.gov (API v2) and PubMed
   (E-utilities) on 2026-11-23, for agents the seed lacked.
3. **A registry cross-check.** One ClinicalTrials.gov query for MS with the
   terms remyelination, remyelinating or "myelin repair". It returned 66
   records on 2026-11-23. All 66 are accounted for in `EXCLUDED.md`: 37 in
   the table, 29 excluded with a reason.
4. **A name checklist.** The intervention names in the 2025 systematic review
   in the European Journal of Neurology (PMID 41216863) were used to see
   whether any agent was missing. Only the names were used. That review is
   under a no-derivatives licence, so none of its tables, wording or
   supplement is reproduced, and every row was built from the trial's own
   paper or registry record.

## How a row is checked

For each row:

1. **Fetch the source.** The PubMed record for a paper. The ClinicalTrials.gov
   or ANZCTR record for a registry row. The page itself for a conference
   report or company statement.
2. **Read it and compare.** Agent, phase, number enrolled, population, primary
   outcome, result and every number in the `effect` cell.
3. **Fix what does not match.** The `check_note` then starts its account of
   the change with "Changed:".
4. **Remove what the source does not say.** A value that could not be found in
   the source read is taken out, not kept from memory.
5. **Match the numbers by script.** Every number in `n`, `population`,
   `primary_outcome` and `effect` is searched for in the saved text of the
   source. A number that is not found is looked at by hand.
6. **Record the check.** `second_check` is set to `yes`, `checked_on` to the
   date, and `check_note` to what was read: abstract, full text or registry
   record.

A row stays at `second_check=no` when its source could not be read in full or
there was nothing independent to check it against. The note gives the reason.

### What the first check found

The 29 seed rows became 33 rows once merged trials were split. 24 of those 33
carry a change. The main kinds of change:

- A review was cited in place of the trial. Fixed for domperidone (2 rows),
  biotin, CNM-Au8 and BIIB061.
- Two or three trials shared a row. Biotin became three rows, liothyronine
  two, and RENEW and its follow-up two.
- A number did not match the source. PIPE-307 VISTA has 182 participants on
  the registry, not 168. The 375 in the Octopus row was the size of stage 1
  across all arms, not of the metformin arm.
- A status was out of date or missing. RESTORE's reason for stopping is on
  the registry. ReINFORCE is not yet recruiting.
- A claim was not in the source. Removed from eight rows.

### Limits of the check

- For 30 of 31 paper rows only the abstract was read.
- One reader, one day, no second reviewer.
- The script matches numbers, not meaning. It cannot tell that a number is
  attached to the right arm or outcome. That part rests on the reading.
- Step 5 could not be run for rows whose source is a web page that was not
  saved as text (CCMR-Two, VISIONARY-MS, Octopus, PTD802, and the phase 2
  rTMS trial). Those were compared by eye only.

## Keeping it current

The table is edited by hand in `data/trials.csv`. Nothing generates it. After
any edit, run `repairmap check` and `pytest`. When a row's source is re-read,
update `checked_on` and `check_note`. When a trial is left out on purpose, add
it to `EXCLUDED.md` with the reason.
