# Arxiv-Tools


### Usage ArxivLinksToCSV.py

1. **List of arXiv URLs**: Update the list of arXiv URLs in the script.

```python
arxiv_urls = [
    'https://arxiv.org/abs/1606.03498',
    'https://arxiv.org/abs/1706.08500',
    'https://arxiv.org/abs/1801.01401'
]
```

2. **Run the script**: Execute the script to fetch paper details and save them into a CSV file.

```sh
python fetch_arxiv_papers.py
```

The script will save the paper details in a file named `arxiv_papers.csv`.

### Output

The output CSV file `arxiv_papers.csv` will have the following columns:

- Title
- Link
- Date
- Authors
- Abstract

### Example Output

|Title|Link|Date|Authors|Abstract|
|---|---|---|---|---|
|Improved Techniques for Training GANs|https://arxiv.org/abs/1606.03498|10 Jun 2016|Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, Xi Chen|We present a variety of new architectural features and training procedures that we apply to the generative adversarial networks \(GANs\) framework\. We focus on two applications of GANs: semi-supervised learning, and the generation of images that humans find visually realistic\. Unlike most work on generative models, our primary goal is not to train a model that assigns high likelihood to test data, nor do we require the model to be able to learn well without using any labels\. Using our new techniques, we achieve state-of-the-art results in semi-supervised classification on MNIST, CIFAR-10 and SVHN\. The generated images are of high quality as confirmed by a visual Turing test: our model generates MNIST samples that humans cannot distinguish from real data, and CIFAR-10 samples that yield a human error rate of 21\.3%\. We also present ImageNet samples with unprecedented resolution and show that our methods enable the model to learn recognizable features of ImageNet classes\.|
|GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium|https://arxiv.org/abs/1706.08500|26 Jun 2017|Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, Sepp Hochreiter|Generative Adversarial Networks \(GANs\) excel at creating realistic images with complex models for which maximum likelihood is infeasible\. However, the convergence of GAN training has still not been proved\. We propose a two time-scale update rule \(TTUR\) for training GANs with stochastic gradient descent on arbitrary GAN loss functions\. TTUR has an individual learning rate for both the discriminator and the generator\. Using the theory of stochastic approximation, we prove that the TTUR converges under mild assumptions to a stationary local Nash equilibrium\. The convergence carries over to the popular Adam optimization, for which we prove that it follows the dynamics of a heavy ball with friction and thus prefers flat minima in the objective landscape\. For the evaluation of the performance of GANs at image generation, we introduce the "Fréchet Inception Distance" \(FID\) which captures the similarity of generated images to real ones better than the Inception Score\. In experiments, TTUR improves learning for DCGANs and Improved Wasserstein GANs \(WGAN-GP\) outperforming conventional GAN training on CelebA, CIFAR-10, SVHN, LSUN Bedrooms, and the One Billion Word Benchmark\.|
|Demystifying MMD GANs|https://arxiv.org/abs/1801.01401|4 Jan 2018|Mikołaj Bińkowski, Danica J\. Sutherland, Michael Arbel, Arthur Gretton|We investigate the training and performance of generative adversarial networks using the Maximum Mean Discrepancy \(MMD\) as critic, termed MMD GANs\. As our main theoretical contribution, we clarify the situation with bias in GAN loss functions raised by recent work: we show that gradient estimators used in the optimization process for both MMD GANs and Wasserstein GANs are unbiased, but learning a discriminator based on samples leads to biased gradients for the generator parameters\. We also discuss the issue of kernel choice for the MMD critic, and characterize the kernel corresponding to the energy distance used for the Cramer GAN critic\. Being an integral probability metric, the MMD benefits from training strategies recently developed for Wasserstein GANs\. In experiments, the MMD GAN is able to employ a smaller critic network than the Wasserstein GAN, resulting in a simpler and faster-training algorithm with matching performance\. We also propose an improved measure of GAN convergence, the Kernel Inception Distance, and show how to use it to dynamically adapt learning rates during GAN training\.|

