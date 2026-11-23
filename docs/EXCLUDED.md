# What was left out, and why

Checked on 2026-11-23. The rules referred to here are in [METHOD.md](METHOD.md).

## 1. ClinicalTrials.gov cross-check

Query, run on 2026-11-23 against the ClinicalTrials.gov API v2:

    https://clinicaltrials.gov/api/v2/studies
        ?query.cond=multiple sclerosis
        &query.term=remyelination OR remyelinating OR "myelin repair"

The registry returned 66 records. Each one is listed below: 37 are in the
table and 29 are excluded. The last column gives the row id or the reason.

| Registry id | Title | Status here | Row id or reason |
|---|---|---|---|
| NCT00127075 | POPART'MUS: Prevention of Post Partum Relapses With Progestin and Estradiol in Multiple Sclerosis | excluded | Sex hormones after childbirth, to prevent relapses. Remyelination is a background remark only. |
| NCT00559702 | Safety Study of Natalizumab to Treat Multiple Sclerosis (MS) | excluded | Approved immune therapy. Rule 4: repair is measured during treatment, but the drug is given to control inflammation. (natalizumab pharmacokinetics; MTR is a secondary measure.) |
| NCT00781872 | Mesenchymal Stem Cells for the Treatment of MS | excluded | Mesenchymal stem cells given to modulate immunity. The record names remyelination only as background, not as an aim or outcome of the trial. |
| NCT00937677 | Effect of Tysabri in Patients With Relapsing-Remitting Multiple Sclerosis: A Follow-up Magnetization Transfer Imaging (MTI) Study | excluded | Imaging or observational study. No intervention is tested for repair. (Observational follow-up on natalizumab.) |
| NCT00986960 | Effect of Adrenocorticotropin Injection With Weekly Interferon Beta in Patients With Relapsing Remitting Multiple Sclerosis (MS) | in the table | `acth-avonex` |
| NCT01037907 | A Study of Orally Administered BGC20-0134 (Structured Lipid) in Patients With Relapsing Remitting Multiple Sclerosis (RRMS) | excluded | Structured lipid tested against new enhancing lesions. 'Remyelination' appears only as a keyword. |
| NCT01085318 | Rebif Advanced Magnetic Resonance Imaging (MRI) and Immunology Pilot Trial | excluded | Approved immune therapy. Rule 4: repair is measured during treatment, but the drug is given to control inflammation. (interferon beta-1a.) |
| NCT01220830 | Cytotron® Delivered Rotational Field Quantum Nuclear Magnetic Resonance Therapy for Multiple Sclerosis | in the table | `cytotron-rfqmr` |
| NCT01244139 | Safety Study of BIIB033 in Subjects With Multiple Sclerosis | in the table | `opicinumab-phase1-ms` |
| NCT01307332 | Advanced MRI Measures of Repair in Alemtuzumab Treated Patients | excluded | Approved immune therapy. Rule 4: repair is measured during treatment, but the drug is given to control inflammation. (alemtuzumab.) |
| NCT01395316 | Alemtuzumab on Surrogate Markers of Disease Activity and Repair Using Advanced MRI Measures in Subjects With Relapsing Remitting Multiple Sclerosis | excluded | Approved immune therapy. Rule 4: repair is measured during treatment, but the drug is given to control inflammation. (alemtuzumab.) |
| NCT01451593 | Neuroprotection With Phenytoin in Optic Neuritis | in the table | `phenytoin-optic-neuritis` |
| NCT01772199 | Study to Assess Whether GSK239512 Can Remyelinate Lesions in Subjects With Relapsing Remitting Multiple Sclerosis | in the table | `gsk239512` |
| NCT01805986 | Investigation of GM Pathology Using Ultra High Field (7T) MRI Scanner | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT01808885 | Safety Study of Olesoxime in Patients With Stable Relapsing Remitting Multiple Sclerosis Treated With Interferon Beta. | in the table | `olesoxime-msrepair` |
| NCT01918501 | Testing Mitochondria Activity and Blood Lipid Content of Multiple Sclerosis Patients | excluded | Imaging or observational study. No intervention is tested for repair. (Blood test study.) |
| NCT02035514 | Phase I-II Clinical Trial With Autologous Bone Marrow Derived Mesenchymal Stem Cells for the Therapy of Multiple Sclerosis | excluded | Mesenchymal stem cells given to modulate immunity. The record names remyelination only as background, not as an aim or outcome of the trial. |
| NCT02040298 | Assessment of Clemastine Fumarate as a Remyelinating Agent in Multiple Sclerosis | in the table | `clemastine-rebuild` |
| NCT02087631 | Safety and Tolerability of Quetiapine in Multiple Sclerosis | in the table | `quetiapine` |
| NCT02308137 | Domperidone in Secondary Progressive Multiple Sclerosis (SPMS) | in the table | `domperidone-spms` |
| NCT02403947 | MEsenchymal StEm Cells for Multiple Sclerosis | excluded | Mesenchymal stem cells given to modulate immunity. The record names remyelination only as background, not as an aim or outcome of the trial. Terminated with 1 participant. |
| NCT02446886 | Adrenocorticotropic Hormone (ACTH) Effects on Myelination in Subjects With MS | in the table | `acth-mwf` |
| NCT02493049 | Pilot Trial of Domperidone in Relapsing-Remitting Multiple Sclerosis (RRMS) | in the table | `domperidone-rrms` |
| NCT02506751 | Open-label Study of Liothyronine in MS | in the table | `liothyronine-phase1b` |
| NCT02521311 | Assessment of Clemastine Fumarate as a Remyelinating Agent in Acute Optic Neuritis (ReCOVER) | in the table | `clemastine-recover` |
| NCT02521545 | Single-Dose Study of a New Formulation of BIIB061 | excluded | Pharmacokinetics of a new BIIB061 formulation in 8 healthy volunteers. No MS participants, and BIIB061 already has a row (rule 2). |
| NCT02760056 | Thyroid Hormone for Remyelination in Multiple Sclerosis (MS): A Safety and Dose Finding Study | in the table | `liothyronine-mst3k` |
| NCT03087136 | A Multicenter Observational Study to Evaluate Pediatric Multiple Sclerosis in Brazil | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT03222973 | Efficacy and Safety of BIIB033 (Opicinumab) as an Add-on Therapy to Disease-Modifying Therapies (DMTs) in Relapsing Multiple Sclerosis (MS) | in the table | `opicinumab-affinity` |
| NCT03536559 | Nanocrystalline Gold to Treat Remyelination Failure in Chronic Optic Neuropathy In Multiple Sclerosis | in the table | `cnmau8-visionary` |
| NCT03600779 | Application of ihMT MRI in Multiple Sclerosis | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT03774407 | Vaginal Estriol in Multiple Sclerosis | in the table | `estriol-vaginal` |
| NCT03910738 | TOTEM RRMS : TestOsterone TreatmEnt on Neuroprotection and Myelin Repair in Relapsing Remitting Multiple Sclerosis | in the table | `testosterone-totem` |
| NCT04002934 | Bazedoxifene Acetate as a Remyelinating Agent in Multiple Sclerosis | in the table | `bazedoxifene-rewrap` |
| NCT04042363 | Effect of Transorbital Electrical STIMulation of Optic Nerve on Remyelination After an Acute Optic Neuritis | in the table | `onstim` |
| NCT04079088 | Study to Evaluate Oral BIIB061 Added to Interferon-beta1 (IFN-β1) or Glatiramer Acetate in Relapsing Multiple Sclerosis (RMS) | in the table | `biib061` |
| NCT04121468 | A Phase I Double Blind Study of Metformin Acting on Endogenous Neural Progenitor Cells in Children and Young Adults With Multiple Sclerosis | in the table | `metformin-paediatric` |
| NCT04532944 | The Energetic Origin of Neurodegeneration in MS | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT04539002 | Aerobic Exercise for Remyelination in Multiple Sclerosis | in the table | `aerobic-exercise` |
| NCT04626921 | A Multi-Center, Open-Label Long-Term Extension Study of CNM-Au8 In Patients With Stable Relapsing Multiple Sclerosis | excluded | Open-label extension of VISIONARY-MS, which has a row. Completed, no results posted. |
| NCT04909502 | Evaluation of Safety, Tolerability and Preliminary Efficacy of EHP-101 in Relapsing Forms of Multiple Sclerosis | in the table | `ehp101` |
| NCT04977622 | Gray Matter Demyelination in Primary Progressive MS at 7T | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT05131828 | CCMR Two: A Phase IIa, Randomised, Double-blind, Placebo-controlled Trial of the Ability of the Combination of Metformin and Clemastine to Promote Remyelination in People With Relapsing-remitting Multiple Sclerosis Already on Disease-modifying Therapy | in the table | `metformin-clemastine-ccmr2` |
| NCT05147532 | Remyelination in Multiple Sclerosis: a PET-MR Longitudinal Study Investigating Individual Profiles of Myelin Repair and the Contribution of Neuroinflammation | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT05177523 | Imaging the Interplay Between Axonal Damage and Repair in Multiple Sclerosis | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT05258396 | Exploring Cortical Remyelination in Children With Multiple Sclerosis | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT05298670 | Drug Repurposing Using Metformin for Improving the Therapeutic Outcome in Multiple Sclerosis Patients | in the table | `metformin-interferon-80` |
| NCT05338450 | Clemastine Fumarate as Remyelinating Treatment in Internuclear Ophthalmoparesis and Multiple Sclerosis | in the table | `clemastine-restore` |
| NCT05359653 | Assessing Changes in Multi-parametric MRI in MS Patients Taking Clemastine Fumarate as a Myelin Repair Therapy | in the table | `clemastine-revive` |
| NCT05418010 | Natalizumab for the Treatment of People With Inflammatory Demyelination Suggestive of Multiple Sclerosis, or Definite Multiple Sclerosis, at First Presentation (AttackMS) | excluded | Approved immune therapy. Rule 4: repair is measured during treatment, but the drug is given to control inflammation. (natalizumab at first presentation; the primary outcome is lesion MTR. Recruiting, primary completion 2027-10-31.) |
| NCT05532943 | Evaluate the Safety and Efficacy of Allogeneic Umbilical Cord Mesenchymal Stem Cells in Patients With Multiple Sclerosis | excluded | Mesenchymal stem cells given to modulate immunity. The record names remyelination only as background, not as an aim or outcome of the trial. |
| NCT05633875 | Multimodal Imaging Signatures of the Biological Mechanisms Underlying Neurodegeneration in Multiple Sclerosis | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT05783934 | Demyelination and Remyelination in Multiple Sclerosis (MS) Detected by Brain Amyloid PET-CT | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT05893225 | Metformin Add-on Clinical Study in Multiple Sclerosis to Evaluate Brain Remyelination And Neurodegeneration | in the table | `metformin-macsimise` |
| NCT05902429 | Effects of Oral Cladribine on Remyelination and Inflammation in Multiple Sclerosis Patients | excluded | Approved immune therapy. Rule 4: repair is measured during treatment, but the drug is given to control inflammation. (cladribine; primary outcome is remyelinated lesions on a myelin map. Status unknown.) |
| NCT06065670 | Assessing Changes in Multi-parametric MRI in Patients With Acute Demyelinating Lesions Taking Clemastine Fumarate as a Myelin Repair Therapy | in the table | `clemastine-reinforce` |
| NCT06171334 | Remote Ischemic Conditioning in PPMS | in the table | `remote-ischaemic-conditioning` |
| NCT06330077 | Ifenprodil as a ReMyelinating repurpOsed Drug in Multiple Sclerosis | in the table | `ifenprodil-modif` |
| NCT06641271 | Study to Investigate Vagus Nerve Stimulation Paired With Motor Task for Remyelination and Functional Recovery | in the table | `vagus-stimulation-auricular` |
| NCT06683612 | PET Study of PIPE-791 in Healthy Volunteers and Volunteers With PrMS and IPF | in the table | `pipe791-pet` |
| NCT06796504 | The SetPoint System as a Pro-Remyelination Therapy for Relapsing-Remitting Multiple Sclerosis: A Pilot Study | in the table | `vagus-stimulation-setpoint` |
| NCT06812585 | The Effect of Metformin As an Adjuvant Therapy on Immunological Parameters in Egyptian Patients with RRMS: a Pilot Study | in the table | `metformin-interferon-30` |
| NCT07222618 | "Selfie" Videos: A Novel, Patient-centered, Comprehensive Approach to Measuring Function in MS | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT07645703 | MS and Health Cohort | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT07723599 | Combating Age-related Failure of Myelination in Multiple Sclerosis: An Exploratory Study | excluded | Imaging or observational study. No intervention is tested for repair. |
| NCT07826689 | A Phase 1/2a Study of Oral PRO-1562 in Healthy Subjects and Patients With Relapsing Multiple Sclerosis | in the table | `pro1562` |

The table holds more rows than these 37. The other rows came from searches by
agent name, from PubMed, or from registries other than ClinicalTrials.gov
(ISRCTN for CCMR-One, ANZCTR for the two rTMS trials).

## 2. Trials found by name and left out

These did not come up in the query above. They were looked up by agent name
on ClinicalTrials.gov or PubMed on 2026-11-23, because a review or a
colleague might expect to see them.

| Agent or trial | Identifier | Reason |
|---|---|---|
| Temelimab (GNbAC1): CHANGE-MS, ANGEL-MS, ProTEct-MS, extension, phase 2a | NCT02782858, NCT03239860, NCT04480307, NCT05049161, NCT01639300 | Rule 3. The registry records name no remyelination aim or outcome. The CHANGE-MS paper (PMID 34240656, abstract) has enhancing lesions as the primary endpoint and reports MTR as a sign of 'possible anti-neurodegenerative effects'. Only abstracts and registry records were read. |
| Nicotinamide riboside (Norseman) | NCT05740722 | Rule 3. The record names no remyelination aim or outcome. Primary outcome is disability progression. Recruiting. |
| Thyromimetics (thyroid hormone receptor agonists other than liothyronine) | none found | No trial in people with MS found on ClinicalTrials.gov or PubMed. The two liothyronine trials are in the table. |
| Metformin in progressive MS (early phase 1) | NCT05349474 | Rule 3. The record names no remyelination aim or outcome. |
| Phenytoin, second optic neuritis trial | NCT02939937 | Rule 3. Retinal layer thickness only; no remyelination aim or outcome in the record. |
| Mesenchymal stem cells, other trials | not enumerated | Rule 3, as for the four mesenchymal stem cell records in section 1. Mesenchymal stem cell trials were not searched for one by one. |
| N-acetyl cysteine (NACPMS) | NCT05122559 | Rule 3. Neuroprotection trial; no remyelination aim or outcome in the record. |
| MIND diet | NCT06992115 | Rule 3. Primary outcome is plasma neurofilament; no remyelination aim or outcome in the record. |
| Alpha-lipoic acid | NCT03161028, NCT01188811 | Rule 3. Neuroprotection trials; no remyelination aim or outcome in the records. |
| Anti-Nogo-A antibody GSK1223249 | NCT01424423, NCT01435993 | Rule 3. Two phase 1 studies, each terminated with 3 participants; no remyelination aim or outcome in the records. |
| Erythropoietin in optic neuritis and progressive MS | NCT00355095, NCT01962571, NCT01144117 | Rule 3. Neuroprotection trials; no remyelination aim or outcome in the records. |
| OCS-05 (BN201) in optic neuritis | NCT04762017, NCT07623668 | Rule 3. No remyelination aim or outcome in the records. |
| Recombinant IGF-1 pilot | NCT00001669, PMID 11936485 | Rule 3. Primary outcome was enhancing lesions; MTR was one of several secondary MRI measures and the abstract does not name remyelination. |
| Guanabenz | NCT02423083 | Rule 3. Terminated with 2 participants; no remyelination aim or outcome in the record. |
| ACTH, other trials | 17 further records on ClinicalTrials.gov | Rule 3. Relapse, fatigue or neuroprotection trials. Only the two ACTH records that name remyelination or myelin water fraction are in the table. |
| PIPE-307 and PIPE-791 phase 1 studies in healthy volunteers | NCT04725175, NCT04941781, NCT05983939 | Rule 2. Healthy volunteers only, and each agent already has a row. |
| Opicinumab and elezanumab studies in healthy volunteers | NCT02641041, NCT02833142, and the healthy-volunteer parts of PMID 25340070 and PMID 36093738 | Rule 2. Healthy volunteers only, and each agent already has rows. |
| GSK239512 drug interaction study | NCT01802931 | Rule 2 and rule 3. Not a trial of repair. |

## 3. Names from the 2025 systematic review

The intervention names in the 2025 systematic review in the European Journal
of Neurology (PMID 41216863) were used as a checklist of names only. No text,
table or supplement from that review is reproduced here, and every row in the
table was built from the trial's own paper or registry record.

Every name on that checklist is either in the table or in the lists above.
Names it has that this table leaves out: mesenchymal stem cells, the MIND
diet, N-acetyl cysteine, and the approved immune therapies. Trials this table
has that are not on that checklist include the biotin trials, the elezanumab
trials, rHIgM22, the two neural progenitor trials from New York, the
intracerebroventricular neural stem cell trial, and the phase 1 programmes
PRO-1562, PTD802 and FTX-101.
