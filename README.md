# Document Retrieval Pipeline

## Overview

This project implements a document retrieval pipeline that evaluates the quality of retrieval using chunking strategies and embedding models. The pipeline is built using the **State of the Union** dataset and utilizes the **FixedTokenChunker** algorithm for chunking and the **MiniLM** embedding model to process and retrieve relevant document excerpts.

The project evaluates the precision and recall of retrieved excerpts based on a set of predefined queries and their ground-truth references.

---

## Installation

Before running the pipeline, ensure that the following dependencies are installed:

1. **Python 3.x**: Ensure that Python 3.6+ is installed on your machine.
2. **Required Libraries**: Install the required Python libraries using `pip`.

```bash
pip install -r requirements.txt
```

## How to run
**Run the Pipeline** : The primary script is contained in the Jupyter notebook pipeline.ipynb. This script will execute the chunking, embedding, retrieval, and evaluation processes.\
\
To run the pipeline, open `pipeline.ipynb` in Jupyter Notebook and run all cells. Make sure the necessary files (such as `state_of_the_union.md` and `questions_state.csv`) are present in the data directory. Cell with `run_pipeline` is currently commented out, as in the next cell there is code to test pipline with multiplme parameters, and it is done in more time efficient way, for the task.

--- 
## Report
The report that summarizes the methodology, experiments, results, and key insights can be found in the **Jupyter Notebook** file `report.ipynb`.
