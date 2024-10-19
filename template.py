import os
from pathlib import Path

package_name = "LLMOps"

list_of_files = [
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/exception.py", 
   f"src/{package_name}/ingestion.py", 
   f"src/{package_name}/rag.py", 
   f"src/{package_name}/utils.py", 
   f"src/{package_name}/data_ingestion/graphDB/__init__.py",
   f"src/{package_name}/data_ingestion/relationalDB/__init__.py",
   f"src/{package_name}/data_ingestion/vectorDB/__init__.py",
   f"src/{package_name}/data_ingestion/vectorDB/chunking/__init__.py",
   f"src/{package_name}/data_ingestion/vectorDB/chunking/data_splitting.py",
   f"src/{package_name}/data_ingestion/vectorDB/embedding/__init__.py",
   f"src/{package_name}/data_ingestion/vectorDB/embedding/data_embeddings.py",
   f"src/{package_name}/data_ingestion/vectorDB/indexing/__init__.py",
   f"src/{package_name}/data_ingestion/vectorDB/indexing/data_indexing.py",
   f"src/{package_name}/data_ingestion/vectorDB/loading/__init__.py",
   f"src/{package_name}/data_ingestion/vectorDB/loading/data_loading.py",
   f"src/{package_name}/data_source_routing/__init__.py",
   f"src/{package_name}/document_retrieval/__init__.py",
   f"src/{package_name}/document_retrieval/document_retrieval.py",
   f"src/{package_name}/query_transformation/__init__.py",
   f"src/{package_name}/query_transformation/prompts.py",
   f"src/{package_name}/query_transformation/query_transformation.py",
   f"src/{package_name}/response_generation/__init__.py",
   f"src/{package_name}/response_generation/response_prompts_template.py",
   f"src/{package_name}/response_generation/response_generation.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/unit.py",
   "tests/integration/__init__.py",
   "tests/integration/int.py",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiment.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file