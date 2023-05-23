This project’s goal was to create a service for product recommendation to customers. This is based on their prior purchases as well as the (disclosable) information that the business has gathered and disseminated (H&M).
With about 1,250,000 client entries and 1,362,281 unique transactions, there are around 45,000 unique products.

The corpus consists of images of articles. We use this information to predict purchases of customers based on their previous purchases by finding article-article similarity using images.


Approach:

Here we use a pre-trained MobilenetV2 model as a standalone feature extractor to pre-process images and extract relevant features. It was selected based on its applications in this domain and its small size which is useful for fast training. The feature extractor was run for our corpus of over 100,000 images on GPU NVIDIA V100 for nearly 1 hour. There was also dimensionality reduction done for noise removal and size reduction.

Once the features were extracted, we used a clustering algorithm by Spotify to calculate similarity score. Annoy (Approximate Nearest Neighbor Oh Yeah), is an open-sourced library for approximate nearest neighbor implementation. We use it to find the image feature vectors in a given set that are closest to a feature vector. For each image, we generate 20 closest neighbors based on their cosine distance. ANNOY creates an index which is a forest of many trees whose nodes are individual feature vectors. The index creation and subsequent forest traversal to get similar nodes for each node takes a whopping 8 hours on GPU! At the end of this we get similar articles for each article. The similarity results seem pretty good. PFA visual results of similarity solution here.

We use this as a tell for future purchases for each customer. Future product purchase is not exactly dependent on product similarity, but is a common indicator as the task of recommendation is not straight- forward. We use the article similarity to recommend users more products based on their past purchases. This model gets a decent score of 0.013% recommendation accuracy which is decent in this field.

Once clustering was complete the recommendations were made. Mean Average Precision @k for this method was 0.101 which is quite high for NN-based techniques. To put into perspective, the Kaggle competition winners achieved Mean Precision 0.0348 for the entire dataset. Ours is comparable to that given the scale.

Results:
![](http://url/to/img.png)

![]([img/Screen Shot 2023-05-22 at 10.11.10 PM.png]([https://github.com/ayushi3004/product-recommendation/blob/main/img/Screen%20Shot%202023-05-22%20at%2010.11.10%20PM.png](https://github.com/ayushi3004/product-recommendation/blob/main/img/Screen%20Shot%202023-05-22%20at%2010.11.10%20PM.png)))
