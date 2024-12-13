#!/bin/bash

# Variables
FOLDER_PATH="C:\Users\mithu\Downloads\Mini_project"          # Path to the folder you want to add
REPO_PATH="https://github.com/Mithun103/verba-vision-pro.git"         # Path to the local clone of your existing repo
COMMIT_MESSAGE="Add subfolder"

# Navigate to the existing repository
cd "$REPO_PATH" || exit

# Copy the folder to the repository
cp -r "$FOLDER_PATH" "$REPO_PATH"

# Stage, commit, and push changes
git add .
git commit -m "$COMMIT_MESSAGE"
git push origin main

echo "Subfolder successfully added to the repository!"
