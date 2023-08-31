import os
import subprocess
import shutil



def repoyu_al(repo_url, clone_dir):
    subprocess.run(["git", "clone", repo_url, clone_dir])

def desire_commit(commit_id, repo_dir):
    subprocess.run(["git", "checkout", commit_id], cwd=repo_dir)

def doxyy(repo_dir, output_dir):
    doxyfile_content = f"""
    PROJECT_NAME     = "MyProject"
    OUTPUT_DIRECTORY = {output_dir}
    EXTRACT_ALL      = YES
    CALL_GRAPH       = YES
    HAVE_DOT         = YES
    INPUT            = {repo_dir}
    """
    with open(os.path.join(repo_dir, "Doxyfile"), "w") as doxyfile:
        doxyfile.write(doxyfile_content)

def calis_doxy(repo_dir):
    subprocess.run(["doxygen", "Doxyfile"], cwd=repo_dir)

def main():
    repo_url = "https://github.com/Py-Contributors/AlgorithmsAndDataStructure.git"
    clone_dir = "/Users/ahmethaskoylu/desktop/repoo"
    output_dir = "/Users/ahmethaskoylu/desktop/repo/sonuc"
    commit_id = "6b9b8b0dfe4543ec2ca191a5290415e36ae06dbd"


    repoyu_al(repo_url, clone_dir)
    desire_commit(commit_id, clone_dir)
    doxyy(clone_dir, output_dir)
    calis_doxy(clone_dir)


if __name__ == "__main__":
    main()
