# Anime Up - Alexa Skill

This is the Alexa Skill "Anime Up", used to track and get updates about anime episodes.

## 🔄 Git Remotes

This project uses **two remotes**:

- `git push origin dev`: Points to **AWS CodeCommit**, which is used by the Alexa Developer Console to update the live skill.
- `git push origin main` or `git push`: Points to the **GitHub repository**, used for version control, collaboration, and backup.

To check remotes:
```bash
git remote -v
