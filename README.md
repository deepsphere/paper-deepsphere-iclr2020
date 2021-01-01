# DeepSphere: a graph-based spherical CNN

[Michaël Defferrard](https://deff.ch),
[Martino Milani](https://www.linkedin.com/in/martino-milani-11258350),
[Frédérick Gusset](https://www.linkedin.com/in/frédérick-gusset-a42485191),
[Nathanaël Perraudin](https://perraudin.info) \
International Conference on Learning Representations (ICLR), 2020

> Designing a convolution for a spherical neural network requires a delicate tradeoff between efficiency and rotation equivariance.
> DeepSphere, a method based on a graph representation of the discretized sphere, strikes a controllable balance between these two desiderata.
> This contribution is twofold.
> First, we study both theoretically and empirically how equivariance is affected by the underlying graph with respect to the number of pixels and neighbors.
> Second, we evaluate DeepSphere on relevant problems.
> Experiments show state-of-the-art performance and demonstrates the efficiency and flexibility of this formulation.
> Perhaps surprisingly, comparison with previous work suggests that anisotropic filters might be an unnecessary price to pay.
> Our code is available at https://github.com/deepsphere.

**PDF available on [arXiv], [OpenReview], [infoscience].**\
Related: [code], [slides], [video].

[arXiv]: https://arxiv.org/abs/2012.15000
[OpenReview]: https://openreview.net/forum?id=B1e3OlStPB
[infoscience]: https://infoscience.epfl.ch
[code]: https://github.com/deepsphere/deepsphere-tf1
[slides]: https://doi.org/10.5281/zenodo.3777976
[video]: https://youtu.be/NC_XLbbCevk

## Compilation

Compile the latex source into a PDF with `make`.
Run `make clean` to remove temporary files and `make arxiv.zip` to prepare an archive to be uploaded on arxiv.

## Figures

All the figures, along with the code and data to reproduce them, are in the [`figures`](figures/) folder.
While the PDFs are stored, they can be regenerated with `make figures`.

## Reviews and rebuttal

The conference reviews and rebuttal are found in [`rebuttal.md`](rebuttal.md) and [openreview].

## History

* 2020-12-30: uploaded on arXiv (git tag `arxiv`)
* 2020-02-15: published at ICLR'20 (git tag `camera-ready`)
* 2019-11-12: updated with reviewers' feedback (git tag `rebuttal`)
* 2019-09-25: submitted to ICLR'20 (git tag `submitted`)
