import os
import shutil
import zipfile

source_dir = r"C:\Users\Admin\Desktop\StatIQ"
team_folder_name = "TeamNexus"
dest_dir = os.path.join(r"C:\Users\Admin\Desktop", team_folder_name)
zip_file_name = r"C:\Users\Admin\Desktop\TEAM_NEXUS_STATATHON2025.zip"

if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)
os.makedirs(dest_dir)

# Create the folder structure
project_dir = os.path.join(dest_dir, "project")
src_dir = os.path.join(project_dir, "src")
assets_dir = os.path.join(project_dir, "assets")

os.makedirs(project_dir)
os.makedirs(src_dir)
os.makedirs(assets_dir)

# Copy files and folders
for item in os.listdir(source_dir):
    if item in ['.git', '.idx', '.coverage', '__pycache__', 'create_zip.py']:
        continue
    
    s = os.path.join(source_dir, item)
    
    # Files that should go to teamname_psid/ or teamname_psid/project/
    # According to image:
    # teamname_psid/
    #   project/
    #     src/
    #     assets/
    #     requirements.txt / package.json / etc.
    # team_info.txt and README.md usually go in teamname_psid/ or project/
    
    if item in ['team_info.txt', 'README.md']:
        # Put in the root of team folder
        d = os.path.join(dest_dir, item)
        shutil.copy2(s, d)
    elif item in ['requirements.txt', 'docker-compose.yml', 'pytest.ini', 'Dockerfile', '.env.example', '.gitignore']:
        # Put in project/
        d = os.path.join(project_dir, item)
        shutil.copy2(s, d)
    elif os.path.isdir(s):
        # Move directories into src/
        d = os.path.join(src_dir, item)
        shutil.copytree(s, d)
    else:
        # Move any other files into project/
        d = os.path.join(project_dir, item)
        shutil.copy2(s, d)

# Now create the ZIP file
shutil.make_archive(r"C:\Users\Admin\Desktop\TEAM_NEXUS_STATATHON2025", 'zip', r"C:\Users\Admin\Desktop", team_folder_name)

print("ZIP file created successfully!")
