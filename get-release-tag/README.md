# get-release-tag

Get the latest release tag from the repository.

# inputs

| parameter         | description                                           |
| ----------------- | ----------------------------------------------------- |
| github_token      | access token for github api                           |
| github_repo_owner | owner of the repository                               |
| github_repo_name  | name of the repository                                |
| prerelease        | if set to `true` then prerelease tag will be returned |

# outputs

| parameter   | description |
| ----------- | ----------- |
| release_tag | release tag |
