# ICLR'20 rebuttal

## Two Questions about Rotation Equivariance

Jialin Liu
07 Nov 2019ICLR 2020 Conference Paper2413 Public CommentReaders: Everyone

Comment: Really interesting work.
I've got 2 questions:
1, As for efficiency, why not use GCN proposed by T.K. Kipf, the successor of ChebNet?
2. As for rotation equivariance, CCN states that "It is, however, possible to construct a CNN in which the activations transform in a predictable and reversible way," I understand what is reversible(invertible) in this work is what CCN calls activation, what is reversible in CCN is the rotation operator in this work, are they same?

Thanks.

Ref.
1. Semi-Supervised Classification with Graph Convolutional Networks. ICLR'17.
2. Covariant Compositional Networks For Learning Graphs. ICLR'18

### Answer

1) need to be a Laplacian (not their single-parameter variant), Kipf's two-parameter variant is ChebNet with a  polynomial order K=1. The method scales linearly with K, which is an hyper-parameter to be set (analogous to the kernel size in classical CNNs)
2) don't understand the question

## Official Blind Review #2

ICLR 2020 Conference Paper2413 AnonReviewer2
24 Oct 2019 (modified: 05 Nov 2019)ICLR 2020 Conference Paper2413 Official ReviewReaders: Everyone
Experience Assessment: I have read many papers in this area.
Rating: 8: Accept
Review Assessment: Thoroughness In Paper Reading: I read the paper at least twice and used my best judgement in assessing the paper.
Review Assessment: Checking Correctness Of Experiments: I assessed the sensibility of the experiments.
Review Assessment: Checking Correctness Of Derivations And Theory: I assessed the sensibility of the derivations and theory.

Review:
The paper presents DeepSphere, a method for learning over spherical data via a graphical representation and graph-convolutions. The primary goal is to develop a method that encodes equivariance to rotations, cheaply. The graph is formed by sampling the surface of the sphere and connecting neighbors according to a distance-based similarity measure. The equivariance of the representation is demonstrated empirically and theoretical background on its convergence properties are shown. DeepSphere is then demonstrated on several problems as well as shown how it applies to non-uniform data.

The paper is interesting and clear. The projection of structured data to graphical representations is both efficient in utilizing existing algorithmic techniques for graph convolutions and useful for approaching the spherical structure of the data. The theoretical analysis and discussion of sampling is interesting, though should be more clearly stated throughout and potentially visualized in figures.

The experiments performed are thorough and interesting. The approach both outperforms baselines in inference time and accuracy. However, one wonders the performance on the well-researched tasks such as the performance on 3D imagery, e.g., Su & Grauman, 2017; Coors et al., 2018. 

The unevenly sampled data is a nice extension showing the generality of the approach. How does the approach work for data connected within a radius rather than a k-nearest approach?

Minor:
- A figure detailing the parameters and setup for theorem 3.1 and figure 2 would be useful.
- The statement on the dispersion of the sampling sequence states “the smallest ball in \R^3 containing \sigma_i”, but I believe it should be “containing only \sigma_i”.

### Answer

* "The theoretical analysis and discussion of sampling is interesting, though should be more clearly stated throughout and potentially visualized in figures."
* "How does the approach work for data connected within a radius rather than a k-nearest approach?" => that shouldn't change much rigth? Especially on HEALPix.

Minor issues have been addressed. Thanks for pointing them out.

## Official Blind Review #3

ICLR 2020 Conference Paper2413 AnonReviewer3
23 Oct 2019 (modified: 05 Nov 2019)ICLR 2020 Conference Paper2413 Official ReviewReaders: Everyone
Experience Assessment: I have published one or two papers in this area.
Rating: 6: Weak Accept
Review Assessment: Thoroughness In Paper Reading: I read the paper thoroughly.
Review Assessment: Checking Correctness Of Experiments: I carefully checked the experiments.
Review Assessment: Checking Correctness Of Derivations And Theory: I carefully checked the derivations and theory.

Review: The paper studies the problem of designing a convolution for a spherical neural network. The authors use the existing graph CNN formulation and a pooling strategy that exploits hierarchical pixelations of the sphere to learn from the discretized sphere. The main idea is to model the discretized sphere as a graph of connected pixels: the length of the shortest path between two pixels is an approximation of the geodesic distance between them. To show the computational efficiency, sampling flexibility and rotation equivariance, extensive experiments are conducted, including 3D object recognition, cosmological mode classification, climate event segmentation and uneven sampling.
Pros: 
1. The application and combination of different techniques in this paper are smart.
2. The experiments show that the proposed method outperforms other baseline methods.
3. The paper is well organized and written. 
Cons:
1. It is a good application of known techniques, but the novelty is limited.
2. It is suggested to add more baselines in the experiments.

[1] Michael Defferrard, Xavier Bresson, and Pierre Vandergheynst. Convolutional neural networks on graphs with fast localized spectral filtering. In Advances in Neural Information ProcessingSystems, 2016

### Answer

Thanks for your review.

Baselines: I don't think so.

## Official Blind Review #1

ICLR 2020 Conference Paper2413 AnonReviewer1
22 Oct 2019 (modified: 05 Nov 2019)ICLR 2020 Conference Paper2413 Official ReviewReaders: Everyone
Rating: 6: Weak Accept
Experience Assessment: I do not know much about this area.
Review Assessment: Checking Correctness Of Derivations And Theory: I assessed the sensibility of the derivations and theory.
Review Assessment: Checking Correctness Of Experiments: I did not assess the experiments.
Review Assessment: Thoroughness In Paper Reading: I made a quick assessment of this paper.

Review: In this paper, CNNs specialized for spherical data are studied. The proposed architecture is a combination of existing frameworks based on the discretization of a sphere as a graph. As a main result, the paper shows a convergence result, which is related to the rotation equivalence on a sphere. The experiments show the proposed model achieves a good tradeoff between the prediction performance and the computational cost. 
Although the theoretical result is not strong enough, the empirical results show the proposed approach is promising. Therefore I vote for acceptance. 

The paper is overall clearly written. It is nice that the authors try to mitigate from overclaiming of the analysis. 

As a non-expert of spherical CNN, I don't understand clearly the gap between the result Theorem 3.1 and showing the rotation equivalence. It would be nice to add some counterexample (i.e., in what situation the proposed approach does not have rotational equivalence while Theorem 3.1 holds).

### Answer

We have a stronger theorem that [...]. No more gap.We have a stronger theorem that [...]. No more gap.