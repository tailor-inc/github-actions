# get-ghe-access-token

Obtain a GHE access token.

# inputs

| parameter           | description                |
| ------------------- | -------------------------- |
| app-id              | GitHub app ID              |
| app-installation-id | GitHub app installation ID |
| app-private-key     | GitHub app private key     |

# outputs

| parameter    | description         |
| ------------ | ------------------- |
| access_token | GitHub access token |


# Example usage

```yml
steps:
  - name: Get github access token
    id: get_access_token
    uses: tailor-inc/github-actions/get-ghe-access-token@main
    with:
      app-id: ${{ secrets.TAILOR_GITHUB_APP_ID }}
      app-installation-id: ${{ secrets.TAILOR_GITHUB_APP_INSTALLATION_ID }}
      app-private-key: ${{ secrets.TAILOR_GITHUB_APP_PRIVATE_KEY }}

  - name: Do something interesting with token
    uses: some/action@version
    with:
      token: ${{ steps.get_access_token.outputs.access_token }}
```
