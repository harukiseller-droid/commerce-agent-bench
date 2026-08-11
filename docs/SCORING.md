# Scoring model

The deterministic scanner is intentionally binary: a fixture passes only when the actual rule-ID set equals the expected rule-ID set.

Future agent-output scoring should be separate from deterministic rule checks. Suggested dimensions:

- evidence accuracy;
- unsupported-claim rate;
- issue recall;
- false-positive rate;
- patch minimality;
- test/verification quality.

Do not combine these into a single vanity score until the rubric and sample size are public and reproducible.
