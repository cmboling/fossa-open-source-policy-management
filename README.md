# FOSSA OSS Policy Management Workflow

## Purpose

This repository is designed to manage open-source license policies using FOSSA's policy management system. The container policy YML file categorizes licenses into different types such as approved, flagged, and denied to ensure compliance with the organization's open-source policy.

## How to Update the Policy

### Important Guidelines

- **Do NOT modify the first 8 lines** of the policy's `yml` file. These lines contain essential metadata and configurations for the policy file.

### Categorizing a License

To categorize a license, follow these steps:

1. **Remove the licenseId** from the `uncategorizedLicense` section.
2. **Add the license details** under the appropriate section (`approved_license`, `flagged_license`, or `denied_license`) with the following format:

    ```yaml
    - type: flagged_license
      licenseId: zsh
      linkingCondition: null
      nameCondition: null
      depthCondition: null
      notes: ''
    ```

    - `type`: Required field. Set it to `flagged_license`, `approved_license`, or `denied_license`.
    - `licenseId`: Required field. Specify the license ID.
    - `linkingCondition`, `nameCondition`, `depthCondition`, and `notes`: Optional fields. Set these fields as necessary.

### Moving a License Between Categories

To move a license from one category to another:

1. **Copy the license entry** from its current section.
2. **Paste the license entry** into the desired section and update the `type` field accordingly.
3. **Update optional fields** as necessary.
4. **Remove the license entry** from its original section.

### Moving a Categorized License to Uncategorized

To move a license back to the `uncategorizedLicense` section:

1. **Copy the licenseId** from the current category.
2. **Add the licenseId** to the `uncategorizedLicense` section in alphabetical order.
3. **Remove the license entry** (including all associated fields) from its former section (`approved`, `flagged`, or `denied`).

## Limitations
As of June 13, 2024, the workflow currently doesn't account for moving a cateogorized license to be uncategorized. The next release will have this functionality based on diffing the changes more granularly.

## Reference

For more detailed information on managing policies with FOSSA, refer to the official [FOSSA documentation](https://docs.fossa.com/docs/policies).
