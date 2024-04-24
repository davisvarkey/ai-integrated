# Vector Search

In order to process text or image for various purpose, it has to be converted to a vector representation. There are mainly two types of vector representation: Sparse Vectors and Dense Vectors.

## Sparse Vectors
Sparse vectors are like the Marie Kondo of data—keeping only what sparks joy (or relevance, in this case).

Consider a simplified example of 2 documents, each with 200 words. A dense vector would have several hundred non-zero values, whereas a sparse vector could have, much fewer, say only 20 non-zero values.

In this example: We assume it selects only 2 words or tokens from each document. The rest of the values are zero. This is why it’s called a sparse vector.

```
dense = [0.2, 0.3, 0.5, 0.7, ...]  # several hundred floats
sparse = [{331: 0.5}, {14136: 0.7}]  # 20 key value pairs
```
The numbers 331 and 14136 map to specific tokens in the vocabulary e.g. ['chocolate', 'icecream']. The rest of the values are zero. This is why it’s called a sparse vector.

The tokens aren’t always words though, sometimes they can be sub-words: ['ch', 'ocolate'] too.
