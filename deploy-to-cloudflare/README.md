# deploy-to-cloudflare

Builds and deploys a Next.js application to Cloudflare.

It assumes the host project has a `package.json` at its root and it defines the node version, e.g.

```jsonc
{
  // ...
  "engines": {
    "node": "20.x"
  }
}
```

## Inputs

- `application_path`
  - **required**
  - The path of the application you want to deploy within its repository.
- `branch`:
  - **optional**
  - The branch name to pass along to Cloudflare.
  - This value is needed to publish to production upon tagging as Cloudflare uses the branch name to
    figure out whether it should deploy to preview or production.
  - Additionally, in preview environments, Cloudflare will deploy the codebase to a subdomain based on the branch name.
    If you push to a branch called `example`, Cloudflare will deploy to `https://example.<project name in CF>.pages.dev`.
    Using this input you can override this default behavior and have Cloudflare deploy to a different subdomain.
- `cloudflare_project_name`
  - **required**
  - The name of the project in Cloudflare.

### Secrets

Actions, contrary to workflows, can't access secrets directly.
As a result, the following secrets need to be passed as inputs:

- `cloudflare_account_id`
  - **required**
  - The Cloudflare account ID the given project belongs to.
- `cloudflare_api_token`
  - **required**
  - A Cloudflare API token.
- `github_token`
  - **required**
  - GitHub token with the `packages:read` permission.

## Outputs

N/A

## Environment variables

The variables passed using the `env` property will be made available to the action as a whole.
These are especially useful for the application build step, see example below.

## Example

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: tailor-inc/github-actions/deploy-to-cloudflare@main
        with:
          application_path: apps/dashboard
          cloudflare_project_name: console
          cloudflare_account_id: ${{secrets.CLOUDFLARE_ACCOUNT_ID}}
          cloudflare_api_token: ${{secrets.CLOUDFLARE_API_TOKEN}}
          github_token: ${{secrets.GITHUB_TOKEN}}
        env:
          NEXT_PUBLIC_API_URL: https://api.tailor.tech
```
