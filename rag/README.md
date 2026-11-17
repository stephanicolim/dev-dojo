# go to folder
```bash
cd dev-dojo
```
# create application with virtual environment
```bash
uv init rag
```
# set up documents
```bash
cd docs
```
# make sure it is using the right venv
```bash
deactivate
source .venv/activate
```
# add chromadb - db for vector embedding
```bash
uv add ollama chromadb 
or
uv add ollama chromadb  "onnxruntime<=1.23.2"
```
# add dynaconf
```bash
uv add dynaconf
```
# pull models
```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```
