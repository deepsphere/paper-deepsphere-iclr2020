# ICLR'20 rebuttal

## General comment about revised manuscript

We uploaded an improved manuscript thanks to the reviewers' comments.
The following has been updated:
* New proof

A link to a public git repository containing all the code will be added to the camera-ready version.

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
Dear Jialin Liu,
Thank you for your interest and questions.

1. First of all, the operator needs to be a Laplacian (why?), excluding the single-parameter variant of GCN. The two-parameter variant is ChebNet with a polynomial order of K=1. The method scales linearly with K, which is an hyper-parameter to be set (analogous to the kernel size in classical CNNs).
For the theory
{nati version} : Practically, we believe that any graph neural network variant may work and some might even slightly beat ChebyNet. 
However, our equivariance theory utilizes the graph Laplacian as a base building block. 
Hence, we do not know the theoretical properties of other GCNs such as the single parameter variant from T.K. Kipf. 
Note that the two-parameter variant from T.K. Kipf is ChebNet with a polynomial order of K=1. 
Eventually, the method we use scales linearly with K, which is an hyper-parameter to be set (analogous to the kernel size in classical CNNs).

TODO{mdeff}: check GCN paper for the variants

2. TODO{mdeff}: Don't understand the question. Read the CCN paper.

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

We thank the reviewer for their time assessing our work and their constructive feedback.

"The theoretical analysis and discussion of sampling is interesting, though should be more clearly stated throughout and potentially visualized in figures."
TODO{mdeff}: What should we do? 
{nati}: I think we should say that it is beyond the scope of this paper… We already have a loooot of appendices.

We deliberately excluded experiments on omnidirectional imagery. In our opinion, those don't possess full spherical symmetries as gravity is orienting the objects. We encourage the reviewer to check the work of Khasanova and Frossard, who explicitly designed graph-based spherical CNNs for omnidirectional imaging. In [1], they designed a graph that yields an equivariant convolution to a subgroup of SO(3). Longitudinal rotations are equivariant by construction of the equiangular sampling, and they optimized the graph for latitudinal equivariance. Their scheme is presented in section 3.2 of our paper. While their convolution is not equivariant to the whole of SO(3), that is not an issue for this application as gravity prevents objects from rotating around the third axis. It may even be beneficial. Moreover, the orientation given by gravity allows factorizing the spherical graph and design anisotropic filters [2].

Radius or kNN graphs are means to get a sparse graph for O(n) matrix multiplication, instead of O(n²) for the full distance-based similarity graph. We believe that the choice of one or the other doesn't really matter. Sparsification can be seen as a numerical approximation that replaces small values by zeroes. The kNN scheme is often preferred in practice as the choice of k is directly linked to the computational cost, while the choice of a radius large enough to avoid disconnected vertices might include many more edges than necessary on denser areas.

"A figure detailing the parameters and setup for theorem 3.1 and figure 2 would be useful."
TODO{mdeff): What does it mean? 
nati: I am not sure. We might just want to ask him?
I think he wants the value of t that we used... Hence, we should make it clear that we did not use directly theorem 3.1 to make figure 2, but that we selected value for t that lead to good results.

We fixed the statement about the dispersion of the sampling sequence. Thanks for pointing it out.
TODO{mdeff): Nath, is he correct?
{nati}: I think our original version is correct. Given a small surface sigma_i and its corresponding point x_i, d_i defines the biggest distance to the center. Hence, we do not care if the ball contains other points surfaces. However, we should add that the ball needs to be centered in x_i. (Can you just check with Martino to be on the safe side?)

[1] Renata Khasanova and Pascal Frossard. Graph-based classification of omnidirectional images. In Proceedings of the IEEE International Conference on Computer Vision, 2017.
[2] Renata Khasanova and Pascal Frossard. Geometry Aware Convolutional Filters for Omnidirectional Images Representation. In International Conference on Machine Learning. 2019.

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

We thank the reviewer for their time assessing our work and their constructive feedback.

While novelty might be limited (although we'd argue that designing a good graph is not trivial), potential impact is certainly not. Researchers working with large spherical maps, in multiple fields, will benefit from the possibility to tackle their problems with a neural network.

Which other baselines would you like to see? We compared with previous works that tackled the same tasks. It is difficult (and probably unfair) to adapt baselines not designed to solve those tasks.

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

We thank the reviewer for their time assessing our work and their constructive feedback.

"the theoretical result is not strong enough"
Since the first submission of the paper, we have made some progress with respect of the theoretical contributions. 
In the new version of the paper, we add a new theorem that shows equivariance at the limit where the sampling is infinite. This new result is a pointwise convergence, meaning that for a fixed function f, RLf(x) -> LRf(x). 
To answer the last point of the reviewer, thanks to this new result, we know that there does not exist any counterexample where Theorem 3.1 holds while having no rotational equivariance.
(Check with Martino to be on the safe side)

TODO{mdeff}: Nath, is it true? Do we have spectral convergence? Or uniform is sufficient? Can you complete the answer?
{nati}: I would not speak about spectral convergence as it is complicated...
