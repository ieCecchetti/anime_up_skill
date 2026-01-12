# Anime Up - Alexa Skill

This is the Alexa Skill "Anime Up", used to track and get updates about anime episodes.

## 🚀 Deployment to Alexa

This project uses **Alexa Hosted Skills** with the `@ask-cli/hosted-skill-deployer`. This means:
- ✅ **Yes, the Lambda function is automatically deployed!** The code in the `lambda/` directory is automatically packaged and deployed when you deploy the skill.
- The Lambda function, skill manifest, and interaction models are all deployed together.

### Understanding Stages

**Stages are Lambda function aliases/versions** that represent different deployment environments:
- **`development`** - Development/test environment (for testing and development)
- **`live`** - Production environment (the version available to end-users)

When you deploy to a stage, the Lambda function gets a new version and the alias points to it. The skill manifest references these Lambda aliases (e.g., `:Release_0` in your `skill.json`).

### Prerequisites

1. Install the ASK CLI:
   ```bash
   npm install -g ask-cli
   ```

2. Configure ASK CLI (if not already done):
   ```bash
   ask configure
   ```
   This will prompt you to log in with your Amazon/Alexa Developer account.

3. Ensure `ask-resources.json` is configured with your skill ID (already done in this project).

### Deploying the Skill

To deploy both the skill package AND the Lambda function to Alexa:

```bash
ask deploy
```

This command will:
- Deploy the skill manifest (`skill-package/skill.json`)
- Deploy the interaction models (`skill-package/interactionModels/`)
- **Deploy the Lambda function** from the `lambda/` directory (including dependencies from `requirements.txt`)

### Deploying to Different Stages

- Deploy to **development** stage (for testing):
  ```bash
  ask deploy --stage development
  ```

- Deploy to **live/production** stage:
  ```bash
  ask deploy --stage live
  ```

### Deploying Only Specific Components

- Deploy only the skill package (manifest + interaction models):
  ```bash
  ask deploy --target skill
  ```

- Deploy only the Lambda function:
  ```bash
  ask deploy --target lambda
  ```

### Alternative: Git-based Deployment

If you prefer using Git (as mentioned in your setup):

1. Push to the `dev` branch which points to AWS CodeCommit:
   ```bash
   git push origin dev
   ```

2. Then deploy from the Alexa Developer Console or use:
   ```bash
   ask deploy
   ```

## 🔄 Git Remotes

This project uses **two remotes**:

- `git push origin dev`: Points to **AWS CodeCommit**, which is used by the Alexa Developer Console to update the live skill.
- `git push origin main` or `git push`: Points to the **GitHub repository**, used for version control, collaboration, and backup.

To check remotes:
```bash
git remote -v
```

## 🤖 Automated Deployment with GitHub Actions

This project includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that automatically deploys your skill when you push to specific branches:

- **`develop` branch** → Deploys to **`development`** stage (test/dev environment)
- **`main` branch** → Deploys to **`live`** stage (production environment)

### Setting Up GitHub Actions

1. **Get your ASK CLI tokens:**
   
   **Option A: Find existing tokens (if ASK CLI is already configured):**
   
   If you've already run `ask configure` on your local machine, your tokens are stored in:
   ```bash
   ~/.ask/cli_config
   ```
   
   To view them:
   ```bash
   cat ~/.ask/cli_config
   ```
   
   Look for the `access_token` and `refresh_token` values in the JSON file under `profiles.default.token`.
   
   **Option B: Generate new tokens:**
   
   If you don't have tokens or want to generate fresh ones:
   ```bash
   ask util generate-lwa-tokens
   ```
   
   This command will:
   - Open a browser for you to log in to your Amazon Developer account
   - Generate and display your `access_token` and `refresh_token`
   - Copy these values - you'll need them for the next step
   
   **Note:** Make sure you have the `ask-resources.json` file in your repository (already included) with your skill ID configured.

   **Important about token expiration:**
   - `access_token` expires in **1 hour** - but this is OK! 
   - `refresh_token` is **long-lived (30-90 days)** and is what matters
   - The ASK CLI **automatically uses the refresh_token to get a new access_token** when it expires
   - You only need to update GitHub Secrets when the **refresh_token expires** (every 30-90 days), not every hour!

2. **Add secrets to GitHub:**
   - Go to your GitHub repository
   - Navigate to **Settings** → **Secrets and variables** → **Actions**
   - Add the following secrets:
     - `ASK_ACCESS_TOKEN` - Your ASK CLI access token
     - `ASK_REFRESH_TOKEN` - Your ASK CLI refresh token

3. **Push to trigger deployment:**
   - Push to `develop` branch → automatically deploys to development stage
   - Push to `main` branch → automatically deploys to live/production stage

The workflow will:
- ✅ Install ASK CLI
- ✅ Configure authentication
- ✅ Deploy the skill manifest, interaction models, **and Lambda function** to the appropriate stage

## 📁 Project Structure

- `lambda/` - Lambda function code (automatically deployed)
  - `lambda_function.py` - Main handler
  - `requirements.txt` - Python dependencies
  - `airing_anime.json` - Anime data
  - `constants.py`, `utils.py` - Helper modules
- `skill-package/` - Skill configuration
  - `skill.json` - Skill manifest
  - `interactionModels/` - Intent and utterance definitions
- `.github/workflows/` - GitHub Actions workflows
  - `deploy.yml` - Automated deployment workflow
- `ask-resources.json` - ASK CLI configuration (contains skill ID)