"""Novel analysis techniques for mechanistic interpretability of refusal."""

from reverseorbitllm.analysis.cross_layer import CrossLayerAlignmentAnalyzer
from reverseorbitllm.analysis.logit_lens import RefusalLogitLens
from reverseorbitllm.analysis.whitened_svd import WhitenedSVDExtractor
from reverseorbitllm.analysis.activation_probing import ActivationProbe
from reverseorbitllm.analysis.defense_robustness import DefenseRobustnessEvaluator
from reverseorbitllm.analysis.concept_geometry import ConceptConeAnalyzer
from reverseorbitllm.analysis.alignment_imprint import AlignmentImprintDetector
from reverseorbitllm.analysis.multi_token_position import MultiTokenPositionAnalyzer
from reverseorbitllm.analysis.sparse_surgery import SparseDirectionSurgeon
from reverseorbitllm.analysis.causal_tracing import CausalRefusalTracer
from reverseorbitllm.analysis.residual_stream import ResidualStreamDecomposer
from reverseorbitllm.analysis.probing_classifiers import LinearRefusalProbe
from reverseorbitllm.analysis.cross_model_transfer import TransferAnalyzer
from reverseorbitllm.analysis.steering_vectors import (
    SteeringVectorFactory,
    SteeringHookManager,
)
from reverseorbitllm.analysis.sae_abliteration import (
    SparseAutoencoder,
    train_sae,
    identify_refusal_features,
    SAEDecompositionPipeline,
)
from reverseorbitllm.analysis.tuned_lens import TunedLensTrainer, RefusalTunedLens
from reverseorbitllm.analysis.riemannian_manifold import RiemannianManifoldAnalyzer
from reverseorbitllm.analysis.anti_ouroboros import AntiOuroborosProber
from reverseorbitllm.analysis.conditional_abliteration import ConditionalAbliterator
from reverseorbitllm.analysis.wasserstein_transfer import WassersteinRefusalTransfer
from reverseorbitllm.analysis.spectral_certification import (
    SpectralCertifier,
    CertificationLevel,
)
from reverseorbitllm.analysis.activation_patching import ActivationPatcher
from reverseorbitllm.analysis.wasserstein_optimal import WassersteinOptimalExtractor
from reverseorbitllm.analysis.bayesian_kernel_projection import BayesianKernelProjection

__all__ = [
    "CrossLayerAlignmentAnalyzer",
    "RefusalLogitLens",
    "WhitenedSVDExtractor",
    "ActivationProbe",
    "DefenseRobustnessEvaluator",
    "ConceptConeAnalyzer",
    "AlignmentImprintDetector",
    "MultiTokenPositionAnalyzer",
    "SparseDirectionSurgeon",
    "CausalRefusalTracer",
    "ResidualStreamDecomposer",
    "LinearRefusalProbe",
    "TransferAnalyzer",
    "SteeringVectorFactory",
    "SteeringHookManager",
    "SparseAutoencoder",
    "train_sae",
    "identify_refusal_features",
    "SAEDecompositionPipeline",
    "TunedLensTrainer",
    "RefusalTunedLens",
    "RiemannianManifoldAnalyzer",
    "AntiOuroborosProber",
    "ConditionalAbliterator",
    "WassersteinRefusalTransfer",
    "SpectralCertifier",
    "CertificationLevel",
    "ActivationPatcher",
    "WassersteinOptimalExtractor",
    "BayesianKernelProjection",
]
