import os
from repo.helper import bfs_folder_search, find_readme, get_readme_summary
from store.helper import get_or_create_knowledge_from_repo

class Repo:
    code_repo_dir = "./code_repo"

    def __init__(self, repo_name):
        self.repo_name = repo_name
        self.repo_root = os.path.join(self.code_repo_dir, repo_name)
        pass

    @property
    def readme_path(self):
        return find_readme(self.repo_root)
    
    @property
    def readme_summary(self):
        return get_readme_summary(self.readme_path)
    
    @property
    def repo_structure(self, text_length_limit=4000):
        return bfs_folder_search(folder_path=self.repo_root, text_length_limit=text_length_limit)
    
    @property
    def store(self):
        return get_or_create_knowledge_from_repo(dir_path=self.repo_root)

