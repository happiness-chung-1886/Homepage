**Mixture-of-Experts Multi-Ring Detector PET Architecture (September 2026)**<br>
Inspired under Professor Jae Sung Lee, Minseok Yi<br>
AI Disclosure: Feedback recieved from ChatGPT<br>
I propose a PET architecture composed of multiple detector rings that have complementary performance characteristics. Based on the previous findings addressing the inherent trade-offs among different PET detector architectures (Lewellen, 2010; Onishi & Ota, 2025), the different detector rings could prioritize complementary functions, such as ultrafast timing resolution, detection sensitivity, energy resolution, or depth-of-interaction accuracy. <br>

For example, SiPM- and CMOS-based detector rings could be jointly employed to exploit complementary strengths in timing performance and fine-grained spatial sensing within the same PET imaging task. In addtion, increasing crystal length improves the interaction probability of an incident 511 keV gamma photon within the crystal and therefore PET sensitivity. However, a longer crystal also increases interaction-depth and scintillation-photon transit-time uncertainty, creating a trade-off between sensitivity and timing/DOI performance (Beheshti et al., 2025). Coincidence events generated from different detector-ring combinations would therefore carry different uncertainty profiles, which could be incorporated into event-specific TOF kernels or reconstruction models. This design aims to investigate whether a mixture-of-experts multi-ring detector PET system may achieve a better interpretations of patient information from the multi-aspect imaging boosting the performance of PET imaging further mitigating the inherent uncertainty of it. <br>

If this direction is forwarded, the novel detector specialization and imaging methodologies for the mixture-of-experts PET would be one of the underexplored research directions that may improve the precision of the entire PET imaging including multi-tracer PET imaging that also lead to better precision medicine as well. And lowering the relatively expensive cost for this implementation may be one of the promising direction as well. <br>

Reference<br>

Beheshti, A., Karimian, A., Arabi, H., & Goertzen, A. L. (2025). “A new design to improve time resolution in a time of flight brain PET using dual layer offset scintillator crystals.” Scientific Reports, 15, 15634. <br>

Onishi, Yuya, and Ryosuke Ota. "Alleviating the trade-off between coincidence time resolution and sensitivity using scalable TOF-DOI detectors." Physics in Medicine & Biology 70.6 (2025): 065003. <br>

Lewellen, Thomas K. "The challenge of detector designs for PET." American Journal of Roentgenology 195.2 (2010): 301-309. <br>

<br>

**Constructing Open Benchmark Datasets in Nuclear Medicine (July 2026 - August 2026)** <br>
Inspired under Professor Jae Sung Lee <br>
AI Disclosure: Feedback recieved from ChatGPT<br>

* ENHANCE.PET 1.6k: https://www.scidb.cn/en/detail?dataSetId=c06e548588694eca8477006e806ed70d <br>
* Myocardial perfusion scintigraphy image database: https://physionet.org/content/myocardial-perfusion-spect/1.0.0/<br>
* OASIS: https://sites.wustl.edu/oasisbrains/home/access/ <br>
* Open NeuroPET: https://openneuropet.github.io/?utm_source=chatgpt.com <br>
* TCIA cancer imaging archive: https://www.cancerimagingarchive.net/browse-collections/<br>
* Related Challenges: AutoPET, HECKTOR, PETRIC, UDPET<br>

Although there are pioneering studies that have advanced Nuclear Medicine as well, the shortage of benchmark datasets remains a bottleneck in advancing Nuclear Medicine and its harmonization with AI. The listed datasets can be used to construct the public benchmark datasets that are more easy to use to thoroughly evaluate the performances of various methodologies accross various tasks in nuclear medicine. In addition, there are available data from the publications that are related to the Nuclear Medicine as well. i hope there would be more of these kind of advancements as well! :D.  <br>

The task examples that are obtained from the ChatGPT are as follows: Acquisition (dose reduction, scan time reduction), Analysis (diagnosis, education, prognosis prediction and assessment, and treatment planning), Detector (detector optimization, DOI estimation, timing estimation, energy estimation), Digital Twins (precise simulation, device modeling), Enhancement (attenuation correction, denoising, motion correction, scatter correction, and super-resolution), Quantification (dosimetry, kinetic modeling, metabolic tumor volume (MTV) estimation, radiomics, SUV estimation, total lesion glycolysis (TLG) estimation), Reconstructions, Registration, Synthesis (cross-modality synthesis, data augmentation). Nuclear medicine tasks can be implemented using AI-based methods, such as classification, detection, generation, and segmentation. Conversely, the requirements of these tasks also drive new AI-based methods as well, of course. <br>

<br>

**Uncertainty-Aware Positron-Emission-Tomography (PET) 4D Video Super-Resolution (June 2026 - September 2026)**<br>
Inspired under Professor Bohyung Han, IEEE-NPSS Nuclear Engineering Summer School, Professor Abhijit Chaudhari, Sangjin Bae, Professor Kris Thielemans<br>
AI Disclosure: Feedback recieved from ChatGPT<br>

Positron Emission Tomography (PET) inherently reconstructs a radiotracer distribution from stochastic decay and detection events, making image formation a statistical inverse problem rather than a direct measurement process. While recent deep learning–based PET super-resolution methods have demonstrated promising visual improvements (Liu et al., 2026), concerns remain regarding quantitative reliability and the potential introduction of artificial uptake patterns. <br>

We hypothesize that these limitations can be substantially mitigated through large-scale data-driven efficient training (awaring how and when to scale) and physics-informed learning frameworks (Polson et al., 2026) that explicitly incorporate PET acquisition constraints, including detector physics, Time-of-Flight (TOF) information, attenuation, and scatter models to prevent the severe distortion. Rather than generating new anatomical or metabolic structures, the proposed approach aims to recover and enhance existing stochastic hypermetabolic signals while preserving quantitative biomarkers such as SUV. <br>

Future work can be expanded to uncertainty-aware and quantification-preserving PET resolution recovery beyond precision imaging considering the inherent stochastic nature of PET imaging, and building rigorous validation framework (Liu et al., 2026) with the ground truth images (reference images) that can be generalizable across diverse scanners, institutions, patient demographics, hyper-parameter settings, tracers to ensure clinical reliability efficiency. <br>

The evaluation framework may can be built is as follows: executing AI-based super-resolution in various timing resolutions (Thielemans et al., 2012) (for example: 500ps -> 200ps / 200ps -> 100ps / 100ps ->50ps) on the same TOF-PET image (Hinge et al., 2026) obtain from a single patient at the same status (within several hours or days based on affordability), powered by robust registration methods (Casamitjana et al., 2025, Li et al., 2026) then compare their consistency and performances. If the enhanced images are well aligned with the ground truth, we may can expect the trained model to be applied to the PET with the best timing resolution (based on the evaluation as an evidence) to obtain inexistent higher-resolution PET images beyond the "precision medicine" that requires existing exact ground truth. <br>

Reference <br>

Casamitjana, Adrià, et al. "USLR: An open-source tool for unbiased and smooth longitudinal registration of brain MRI." Medical image analysis 105 (2025): 103662. <br>

Hinge, Christian, et al. "A multimodal total-body dynamic [18F] FDG PET/CT/MRI dataset of 100 healthy humans." Scientific Data (2026). <br>

Lee, Junsung, et al. "Low-Resolution Editing is All You Need for High-Resolution Editing." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2026. <br>

Li, Xia, et al. "Continuous sPatial‐temporal deformable image registration and 4D frame interpolation." Medical Physics 53.1 (2026): e70248. <br>

Liu, Yan, et al. "NGSE-Corr: A technique for objective clinical evaluation of quantitative-imaging methods without a gold standard." IEEE Transactions on Medical Imaging (2026). <br>

Polson, Luke, Joseph Grudzinski, and Frederick Wilson. "Toward Reduced Patient Scan Times: Full Monte Carlo Torch® Recon for Lu-177 SPECT Enables Improved Precision Through Dual-Energy Window Integration." (2026): 262053-262053. <br>

Thielemans, Kris, et al. "STIR: software for tomographic image reconstruction release 2." Physics in medicine and biology 57.4 (2012): 867-883. <br>



<br>

**The Possibility of Medical Image Superresolution (May 2026)** <br>
Inspired under Professor Fei-Fei Li and Professor Simon Cherry <br>

Superesolutions in the natural images and PET images would share the common characteristic that they generate hardware that does not exist before. And i learned that the number of detectors in a PET is more than 500,000 (a lot more than i expected) according to the open lecture from Professor Simon Cherry ([https://www.kcl.ac.uk/events/inaugural-lecture-professor-simon-cherry](https://www.kcl.ac.uk/events/inaugural-lecture-professor-simon-cherry)). Then, the superresolution of a PET image that does not severely distort the initial shape looks quite possible. Thinking about modality translation research between CT and MRI are executed although they are different medical modalities, the superresolution conventionally regarded as impossible may also be possible. <br>

<br>

**One of the Future Directions of Theranostics (May 2026)**<br>
<img src="images/image68.jpg" height="200"><img src="images/image69.jpg" height="200"><br>
Inspired under SNMMI Patient Education Day <br>
AI Disclosure: image generated from ideogram <br>

I think one future direction of theranostics in nuclear medicine is the invention of a “single-agent theranostic” beyond ligand-matched theranostic pairs that enables simultaneous diagnosis via PET-related imaging and therapy.To achieve this goal, designing, constructing, and building a novel tracer that is effective for both imaging and therapeutic purposes could be a promising starting point. <br>

Such an approach may facilitate real-time treatment monitoring thereby reducing the time required for the entire clinical procedure potentially reducing unnecessary radiation exposure to normal organs while maintaining or boosting therapeutic efficacy.<br>
