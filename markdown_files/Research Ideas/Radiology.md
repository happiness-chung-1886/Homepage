**Training-Free Bounding-Box Annotation for the Pre-Trained Clinical Multi-Modal Models (June 2026)** <br>

While recent multimodal large language models (MLLMs) can generate clinical findings from medical scans, the evidence supporting each generated concept can be difficult to interpret due to ambiguity. Existing explainability methods typically visualize global saliency maps or segmentation masks that occlude underlying image structures. In this proposal, inspired by the previous work [1, 2, 3, 4, 5, 6], this study aims to explore a training-free evidence grounding framework for medical MLLMs that supports clinical findings. <br>

Specifically, we aim to annotate bounding boxes using concept-specific saliency maps obtained via backpropagation, based on the generated tokens, such as primary tumors, lymph node metastases, or hypermetabolic lesions. This approach establishes an explicit correspondence between generated medical findings and image regions without requiring additional training or annotation. <br>

This work hypothesizes that concept-specific evidence grounding can improve the interpretability and clinical trustworthiness of medical MLLMs while preserving the visibility of the original medical image compared with conventional segmentation-based visualization approaches. In addition, because segmentation-based approaches have limited label sets, this training-free bounding-box annotation approach can be generalized to environments where precise, complete labels are scarce. <br>

Reference
[1] Cao, Bingyi, et al. "TIPSv2: Advancing Vision-Language Pretraining with Enhanced Patch-Text Alignment." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2026.
[2] Zhu M, Liu M, Yuan H, Ning Y, Luo Z, Zhu T, et al. Attention guided fair artificial intelligence modeling for skin cancer diagnosis. npj Digital Medicine. 2026. doi:10.1038/s41746-026-02897-8.
[3] Blume, Ansel, et al. "PARTONOMY: Large Multimodal Models with Part-Level Visual Understanding." Advances in Neural Information Processing Systems 38 (2026): 34705-34734.
[4] Shlapentokh-Rothman, Michal, et al. "Region-based representations revisited." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.
[5] Wang, Lezi, et al. "Sharpen focus: Learning with attention separability and consistency." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2019.
[6] Le, Matthieu, et al. "Computationally efficient cardiac views projection using 3D convolutional neural networks." International Workshop on Deep Learning in Medical Image Analysis. Cham: Springer International Publishing, 2017.

<br>

**Multi-Modal Frequency Gradient Consensus for Robust Tumor Boundary Delineation (June 2026)** <br>

Background
Accurate tumor segmentation is a fundamental component of numerous clinical applications, including radiation therapy planning, nuclear medicine dosimetry, surgical navigation, and disease monitoring. Despite remarkable advances in medical image segmentation, most existing approaches rely on expert-drawn annotations as the ground truth for model development and evaluation. However, tumor boundaries are often inherently ambiguous, resulting in substantial inter-observer and intra-observer variability. Consequently, segmentation models may learn to replicate expert preferences rather than the underlying biological structures. This challenge motivates the exploration of alternative strategies for defining tumor boundaries that are less dependent on subjective annotations. <br>

Motivation
Biological structures frequently manifest as transitions in image characteristics rather than as explicitly defined contours. Different imaging modalities capture complementary aspects of tissue composition and pathology. For example, PET reflects metabolic activity, CT reveals anatomical density, and MRI provides detailed soft-tissue contrast and texture information. We hypothesize that true anatomical or pathological boundaries may correspond to locations where multiple imaging modalities simultaneously exhibit significant spatial or frequency-domain transitions. Instead of treating expert contours as the absolute truth, we investigate whether tumor boundaries can be objectively inferred from multi-modal image evidence itself. <br>

Proposed Method
This study proposes a Multi-Modal Frequency Gradient Consensus Framework for boundary discovery. Given co-registered PET, CT, and MRI scans, high-frequency structural information is first extracted from each modality using frequency-aware representations such as wavelet decomposition, Laplacian pyramids, or Fourier-domain filtering. PET in this procedure can function as marking where to focus on via illuminating hypermetabolism. Based on this illuminated candidate region, CT and MRI can compute spatial gradient maps to identify regions exhibiting rapid signal transitions. The modality-specific boundary responses are subsequently fused into a Boundary Consensus Map that highlights locations where multiple modalities simultaneously indicate structural changes. Finally, this consensus representation is integrated into a segmentation framework, such as active contours, level-set optimization, graph-based methods, or neural networks, to produce anatomically consistent segmentations while preserving uncertainty estimates in ambiguous regions. <br>

Expected Results
The proposed framework is expected to reduce dependence on subjective expert annotations by leveraging intrinsic imaging evidence from multiple modalities. By emphasizing boundary agreement across PET, CT, and MRI, the method may improve segmentation reproducibility and robustness, particularly in challenging cases involving infiltrative tumors, low-contrast lesions, or heterogeneous uptake patterns. Furthermore, the resulting boundary maps provide a transparent and interpretable explanation for segmentation decisions, potentially improving clinician trust and facilitating quality assurance. <br>

Potential Impact
This work has the potential to establish a new paradigm for medical image segmentation by shifting the focus from annotation imitation to frequency-based evidence-driven boundary discovery. In nuclear medicine, more reliable tumor delineation could improve voxel-level dosimetry and treatment response assessment. In radiation oncology, objective boundary identification may enhance target volume definition and reduce contouring variability across institutions. More broadly, the proposed framework could serve as a foundation for future multimodal medical segmentation. <br>

