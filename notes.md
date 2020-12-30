# Todo

## Links

* git <https://github.com/nperraud/deepsphere_v2_paper>
* overleaf <https://www.overleaf.com/project/5d31d2fbd6859d54cb707212>
* openreview <https://openreview.net/forum?id=B1e3OlStPB>
* arxiv

## Summary

story: there are tradeoffs when designing a spherical CNN $\Rightarrow$ DS strikes a controllable balance between efficiency / cost and exactitude / equivariance
* method development: tool that solve a need (balance btw the desiderata: equiv vs cost)
* research question: anisotropy (highlight from the start or leave it as a dangling question at the end)

contributions:
* theory $\Rightarrow$ convergence (better graph)
* experiments on relevant problems (not spherical MNIST) $\Rightarrow$ check the desiderata
* surprising: anisotropy doesn't seem useful

## Todo

* Unify vocabulary and avoid synonyms.
	* Sampling, grid, discretization, pixelization $\Rightarrow$ sampling (sampling schemes when not a particular set of vertices?)
	* Signal, maps, fields, functions.
	* Irregular, uneven, non-uniform.
	* Coarsening, down-sampling.
	* Sample, vertex, node, pixel, point $\Rightarrow$ vertex
* put all the code (learning experiments from Frédérick and equivariance experiments from Martino) in a common reproducible git repository to be linked from the paper
* update pygsp and merge sphere branch
* Compute the invariance error of the whole NNs (before and after training, invariance can be learned). Add it with equivariance error of the convolution to \tabref{cosmo}. \nati{I guess we are not doing that}
* insert \citet{jiang2019sphericalcnn} in intro: Need a global coordinate system (ok for planets, not projections like cosmo)
* mention that \citep{esteves2018sphericalcnn} and \citep{cohen2018sphericalcnn} computed equivariance error
* add somewhere (intro?): exploit symmetries to reduce sample cost $\Rightarrow$ we don't discuss symmetries much
* \citet{mudigonda2017climateevents} use Integrated Water Vapor (IWV) only. That most probably is the same as our TMQ, which is most probably the most informative feature. TODO: run ours with TMQ alone.
* better abstract (Friday's talk abstract?)
* abstract: tackle impactful / important problems in cosmology and climatology (Earth sciences)
* conclusion: less speculation?
* check feedback from ICLR'20 LTS2 reading group
* \mdeff{check my Telegram notes}
* argue against more generality
* figure that shows the three samplings? (suggested by reviewer \#2)
* add the eigenfunction alignment in the appendix
* Shouldn't theorem 3.2 be a corollary?
* Experiments: organize per problem or desideratum?
	* per desideratum is better to show that we check them
	* per problem is better to emphasize their relevance (climate, cosmo)
* Articulate the story around the desiderata. Add "most general / powerful" as one (for isotropy).
* Better motivate the method (i.e., don't present our work as just the analysis of one method). Why is it a good method? It allows for a linear time implementation of operators on scalar fields. Need to show that functions of the Laplace-Beltrami $h(\Delta)$ can indeed implement any equivariant (gauge invariant \citep{cohen2019gauge}) linear operations on scalar fields.
* Restructure the method section to show how the cost is reduced to $\bO(pkn)$: (i) discretization ($n$ vertices), (ii) sparsification ($k$ neighbors), (iii) reduction of the class of operators / filters (polynomial order $p$).
* A filter operating on scalar fields has to be isotropic / directionless to be equivariant \citep{cohen2019gauge}) [Kondor CCN]
	* A cheap solution: if the domain can be globally oriented (e.g., by gravity for 2D or omnidirectional images), then the spatial dimension can be factorized (think of the up, down, right, left directions in 2D images). The sphere could be factorized as two oriented lines for the vertical axis, and a circle horizontally. That is exploited by Khasanova to create anisotropic filters on the sphere for omnidirectional imaging. That of course reduces the symmetry group the NN is to be equivariant to.
	* Otherwise there is a price to pay.
	* If not but the domain has global symmetries, activations can be lifted to the symmetry group \citep{cohen2018sphericalcnn} [Kondor CCN]. That is however memory and computationally expensive, as the activations must have the size of the symmetry group.
	* Without global symmetries, tensor activations are needed \citep{cohen2019gauge}.
* Write why we don't tackle omnidirectional imaging. Same reason as images. Factor the manifold. For some samplings their graph discretization can be factored, yielding anisotropic filters. (c.f. answer to reviewer 1)

last pass:
* figure placement
* check footnotes

## Not done

* Do the experiments on the icosahedral sampling with the pooling as defined in the paper (i.e., not Jiang's specialty of taking the value of a pre-chosen sub-pixel). \nati{I guess we are not doing that.} \mdeff{I'm not sure what is the state of this, and Frédérick is not with us anymore. It's quite minor.}
* Check results for ModelNet40 and integrate in text. \nati{I would drop this.} \mdeff{Yeah, those results are not mature enough.}
* Add \citet{bruna2013gnn} in equivariance? They were the first to do a spherical CNN with graphs. Graph is built from a uniform random sampling of the sphere. \nati{Where do you want to add them?} \mdeff{They don't write how their Laplacian was built. Also, they only did MNIST on the sphere...}
