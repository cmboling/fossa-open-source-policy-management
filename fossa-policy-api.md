# FOSSA Policy API Usage Guide

This guide provides instructions on how to update FOSSA policies using two specific API endpoints: moving a license to a category and deleting a license from a category.

## Prerequisites

- A valid FOSSA account
- Access to your FOSSA API `accessToken`
- The `policyId` of the policy you want to update
- The `licenseId` of the license you want to move or delete

## API Endpoints

### 1. Move a License to a Category

This endpoint moves a specified license to a designated category within a policy.

#### Endpoint

```
POST https://app.fossa.com/api/policies/{{policyId}}/rules
```

#### Request Headers

- `Content-Type: application/json`
- `Authorization: Bearer {{accessToken}}`

#### Request Body

```json
{
    "licenseId": "AAL",
    "type": "approved_license",
    "notes": "",
    "nameCondition": null,
    "depthCondition": null,
    "linkingCondition": null
}
```

- `licenseId`: The ID of the license you want to move.
- `type`: The type of license category (e.g., `approved_license`, `flagged_license`, `denied_license`).
- `notes`: Any notes related to the license (optional).
- `nameCondition`, `depthCondition`, `linkingCondition`: Conditions for the license (optional).

#### cURL Command

```sh
curl --location 'https://app.fossa.com/api/policies/{{policyId}}/rules' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{accessToken}}' \
--data '{
    "licenseId": "AAL",
    "type": "approved_license",
    "notes": "",
    "nameCondition": null,
    "depthCondition": null,
    "linkingCondition": null
}'
```

### 2. Delete a License from a Category

This endpoint deletes a specified license from a designated category within a policy.

#### Endpoint

```
DELETE https://app.fossa.com/api/policies/{{policyId}}/rules/{{uncategorized-license-id}}
```

#### Request Headers

- `Authorization: Bearer {{accessToken}}`

#### cURL Command

```sh
curl --location --globoff --request DELETE 'https://app.fossa.com/api/policies/{{policyId}}/rules/{{uncategorized-license-id}}' \
--header 'Authorization: Bearer {{accessToken}}'
```

Replace `{{policyId}}`, `{{accessToken}}`, and `{{uncategorized-license-id}}` with your actual policy ID, access token, and license ID, respectively.

## Example Usage

### Moving a License to a Category

If you want to move a license with ID `AAL` to the `approved_license` category in a policy with ID `12345`, your cURL command will look like this:

```sh
curl --location 'https://app.fossa.com/api/policies/12345/rules' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
    "licenseId": "AAL",
    "type": "approved_license",
    "notes": "",
    "nameCondition": null,
    "depthCondition": null,
    "linkingCondition": null
}'
```

### Deleting a License from a Category

If you want to delete a license with ID `AAL` from a policy with ID `12345`, your cURL command will look like this:

```sh
curl --location --globoff --request DELETE 'https://app.fossa.com/api/policies/12345/rules/AAL' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

## Conclusion

By following the instructions in this guide, you should be able to move licenses to categories and delete licenses from categories in your FOSSA policies using the provided API endpoints. Ensure that you replace placeholders with your actual `policyId`, `accessToken`, and `licenseId` values. If you encounter any issues, refer to the FOSSA API documentation for further assistance.
