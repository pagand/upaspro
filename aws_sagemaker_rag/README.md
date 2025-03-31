# sagemaker-workshop-cloud-seminar

Run the notebook medical-question-answering-rag.ipynb

Step 1 : Index documents in the vector store
Before being able to answer the questions, the documents must be processed and a stored in a document store index. Load the documents. Process and split them into smaller chunks to create a numerical vector representation of each chunk using BGE model. Create an index using the chunks and the corresponding embeddings.

Step 2 : Conversation with users with a large language model and an existing knowledge base
When the documents index has been prepared, you are ready to ask the questions and relevant documents will be fetched based on the question being asked. The following steps will be executed:
1.	Create an embedding of the input question.
2.	Compare the question embedding with the FAISS vector store embeddings for the (top N) relevant document chunks.
3.	Add those chunks as part of the context in the prompt.
4.	Send the prompt to the model at the Amazon SageMaker endpoint using the contextual answer based on the documents retrieved
