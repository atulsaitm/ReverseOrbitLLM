"""ReverseOrbitLLM — Master Ablation Suite for HuggingFace transformers."""

__version__ = "0.1.2"

# Lazy imports for the main pipeline classes
__all__ = [
    "AbliterationPipeline",
    "InformedAbliterationPipeline",
    "set_seed",
    "run_sweep",
    "SweepConfig",
    "SweepResult",
    "save_contribution",
    "load_contributions",
    "aggregate_results",
    "TourneyRunner",
    "TourneyResult",
    "get_adaptive_recommendation",
    "AdaptiveRecommendation",
    "RemoteRunner",
    "RemoteConfig",
]


def __getattr__(name):
    if name == "AbliterationPipeline":
        from reverseorbitllm.abliterate import AbliterationPipeline
        return AbliterationPipeline
    if name == "InformedAbliterationPipeline":
        from reverseorbitllm.informed_pipeline import InformedAbliterationPipeline
        return InformedAbliterationPipeline
    if name == "set_seed":
        from reverseorbitllm.reproducibility import set_seed
        return set_seed
    if name == "run_sweep":
        from reverseorbitllm.sweep import run_sweep
        return run_sweep
    if name == "SweepConfig":
        from reverseorbitllm.sweep import SweepConfig
        return SweepConfig
    if name == "SweepResult":
        from reverseorbitllm.sweep import SweepResult
        return SweepResult
    if name == "save_contribution":
        from reverseorbitllm.community import save_contribution
        return save_contribution
    if name == "load_contributions":
        from reverseorbitllm.community import load_contributions
        return load_contributions
    if name == "aggregate_results":
        from reverseorbitllm.community import aggregate_results
        return aggregate_results
    if name == "TourneyRunner":
        from reverseorbitllm.tourney import TourneyRunner
        return TourneyRunner
    if name == "TourneyResult":
        from reverseorbitllm.tourney import TourneyResult
        return TourneyResult
    if name == "get_adaptive_recommendation":
        from reverseorbitllm.adaptive_defaults import get_adaptive_recommendation
        return get_adaptive_recommendation
    if name == "AdaptiveRecommendation":
        from reverseorbitllm.adaptive_defaults import AdaptiveRecommendation
        return AdaptiveRecommendation
    if name == "RemoteRunner":
        from reverseorbitllm.remote import RemoteRunner
        return RemoteRunner
    if name == "RemoteConfig":
        from reverseorbitllm.remote import RemoteConfig
        return RemoteConfig
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
