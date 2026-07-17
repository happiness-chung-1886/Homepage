**Constructing Open Benchmark Datasets in Nuclear Medicine (July 2026)** <br>
Inspired under Professor Jae Sung Lee <br>
AI Disclosure: Feedback recieved from ChatGPT<br>
* ENHANCE.PET 1.6k: https://www.scidb.cn/en/detail?dataSetId=c06e548588694eca8477006e806ed70d <br>
* Myocardial perfusion scintigraphy image database: https://physionet.org/content/myocardial-perfusion-spect/1.0.0/<br>
* OASIS: https://sites.wustl.edu/oasisbrains/home/access/ <br>
* TCIA cancer imaging archive: https://www.cancerimagingarchive.net/browse-collections/<br>
* Related Challenges: AutoPET, HECKTOR, PETRIC<br>

Although there are pioneering studies that have advanced Nuclear Medicine as well, the shortage of benchmark datasets remains a bottleneck in advancing Nuclear Medicine and its harmonization with AI. The listed datasets can be used to construct the public benchmark datasets that are more easy to use to thoroughly evaluate the performances of various methodologies accross various tasks in nuclear medicine. In addition, there are available data from the publications that are related to the Nuclear Medicine as well. i hope there would be more of these kind of advancements as well! :D.  <br>

The task examples that are obtained from the ChatGPT are as follows: Acquisition (dose reduction, scan time reduction), Analysis (diagnosis, education, prognosis prediction and assessment, and treatment planning), Detector (Detector optimization, DOI estimation, Timing estimation, Energy estimation), Digital Twins (precise simulation and virtual scanner modeling), Enhancement (attenuation correction, denoising, motion correction, scatter correction, and super-resolution), Quantification (dosimetry, kinetic modeling, metabolic tumor volume (MTV) estimation, SUV estimation, total lesion glycolysis (TLG) estimation), Reconstructions, Registration, Synthesis (cross-modality synthesis, data augmentation). The tasks can be implemented via AI-based methods as well, such as classification, detection, generation, and segmentation. <br>

<br>

**Uncertainty-Aware Positron-Emission-Tomography (PET) 4D Video Super-Resolution (June 2026)**<br>
Inspired under Professor Bohyung Han, IEEE-NPSS Nuclear Engineering Summer School <br>
AI Disclosure: Feedback recieved from ChatGPT<br>
Positron Emission Tomography (PET) inherently reconstructs a radiotracer distribution from stochastic decay and detection events, making image formation a statistical inverse problem rather than a direct measurement process. While recent deep learning–based PET super-resolution methods have demonstrated promising visual improvements, concerns remain regarding quantitative reliability and the potential introduction of artificial uptake patterns. <br>
We hypothesize that these limitations can be substantially mitigated through large-scale data-driven efficient training (awaring how and when to scale) and physics-informed learning frameworks that explicitly incorporate PET acquisition constraints, including detector physics, Time-of-Flight (TOF) information, attenuation, and scatter models to prevent the severe distortion. Rather than generating new anatomical or metabolic structures, the proposed approach aims to recover and enhance existing stochastic hypermetabolic signals while preserving quantitative biomarkers such as SUV. <br>
Future work can be expanded to uncertainty-aware and quantification-preserving PET resolution recovery beyond precision imaging considering the inherent stochastic nature of PET imaging, and building rigorous validation framework with the ground truth images (reference images) that can be generalizable across diverse scanners, institutions, patient demographics, hyper-parameter settings, tracers to ensure clinical reliability efficiency. <br>
The evaluation framework may can be built is as follows: executing AI-based super-resolution in various timing resolutions (for example: 500ps -> 200ps / 200ps -> 100ps / 100ps ->50ps) on the same TOF-PET image obtain from a single patient at the same status (within several hours or days based on affordability), then compare their consistency and performances. If the enhanced images are well aligned with the ground truth, we may can expect the trained model to be applied to the PET with the best timing resolution (based on the evaluation as an evidence) to obtain inexistent higher-resolution PET images beyond the "precision medicine" that requires existing exact ground truth. <br>

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
