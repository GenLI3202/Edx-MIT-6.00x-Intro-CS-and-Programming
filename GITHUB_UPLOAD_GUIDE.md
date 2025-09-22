# GitHub Upload Instructions

## How to Upload This Repository to GitHub

### Prerequisites
1. Make sure you have a GitHub account (create one at https://github.com if needed)
2. Install Git (already done - you have it working!)

### Steps to Upload

#### Method 1: Using GitHub Web Interface (Recommended for beginners)
1. Go to https://github.com and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Fill in the repository details:
   - **Repository name**: `MIT-6.00-Introduction-to-CS-and-Programming`
   - **Description**: `Coursework and solutions for MIT 6.00 Introduction to Computer Science and Programming (6.00.1x and 6.00.2x)`
   - **Visibility**: Choose Public or Private based on your preference
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click "Create repository"

#### Method 2: Using Command Line
After creating the repository on GitHub, run these commands in the terminal:

```powershell
# Add the GitHub repository as a remote
git remote add origin https://github.com/YOUR_USERNAME/MIT-6.00-Introduction-to-CS-and-Programming.git

# Push your code to GitHub
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### Alternative: Using GitHub CLI (if installed)
```powershell
# Create repository and push in one command
gh repo create MIT-6.00-Introduction-to-CS-and-Programming --public --push
```

### Repository Features

Your repository will include:
- ✅ **README.md** - Comprehensive project description
- ✅ **LICENSE** - MIT License with educational content notice
- ✅ **gitignore** - Properly configured for Python projects
- ✅ **Organized structure** - Clear folder hierarchy by week/topic
- ✅ **Clean commit history** - Professional initial commit

### Recommended Repository Settings

After uploading, consider:
1. **Add topics/tags**: `python`, `mit`, `computer-science`, `education`, `coursework`
2. **Enable issues**: For discussion or questions about the code
3. **Add a description**: Brief summary visible on your profile
4. **Consider adding a website**: Link to MIT's course page

### Security Notes
- No sensitive information is included
- Video files (.mp4) are excluded via .gitignore to save space
- Large zip files are excluded - they can be re-downloaded if needed

### What's Next?
After uploading, you can:
- Share the repository link on your portfolio/resume
- Continue adding more coursework or projects
- Use it as a reference for future learning
- Contribute to the open-source community

### Troubleshooting
If you encounter issues:
1. Make sure you're in the correct directory: `h:\TUM-PC\TUM\edX\CS\MIT CS6.00`
2. Check your GitHub credentials are set up correctly
3. Verify the remote URL is correct: `git remote -v`
4. For authentication issues, consider using a Personal Access Token instead of password

---

**Note**: Remember to respect academic integrity policies when sharing coursework publicly. This repository includes appropriate disclaimers in the README and LICENSE files.