#!/bin/bash

PROJECT_NAME=$1
GITHUB_USERNAME="rocky190295"
TARGET_DIR="$PROJECT_NAME-export"

# 1. Clone the current repo into a temporary directory
git clone . $TARGET_DIR

cd $TARGET_DIR

# 2. Remove everything except the project folder
find . -mindepth 1 -maxdepth 1 ! -name "$PROJECT_NAME" -exec rm -rf {} +

# 3. Move the project folder contents to root
mv $PROJECT_NAME/* .
rm -r $PROJECT_NAME

# 4. Reinitialize Git history (optional clean start)
rm -rf .git
git init
git add .
git commit -m "Initial commit - extracted $PROJECT_NAME from monorepo"

# 5. Create GitHub repo URL
REMOTE_REPO="git@github.com:$GITHUB_USERNAME/$PROJECT_NAME.git"

# 6. Add remote and push
git remote add origin $REMOTE_REPO
git branch -M main
git push -u origin main

# 7. Cleanup
cd ..
rm -rf $TARGET_DIR
