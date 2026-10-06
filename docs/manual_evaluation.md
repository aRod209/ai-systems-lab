# Manual evaluation: ambiguous research-paper prompts

These five inputs are deliberately designed to **challenge the model used by the app and test its output**. This is a manual live evaluation, not a set of deterministic unit tests. Record the app's console output verbatim; a schema-valid answer is not evidence that the research claims are true. Do not include API keys or the contents of `.env`.

Run context: `ai-systems-lab` (the `ai_systems_lab.main:main` entry point), model configured in `src/ai_systems_lab/gemini_client.py`: `gemini-3.8-flash`; installed `google-genai` version: `2.24.0`. Each run's local timestamp, outcome and output belong in its own section below. The initial capture stopped after prompt 1 timed out, before prompts 2–5. Separately supplied answers for prompts 1 and 2 are recorded below without attributing them to that initial capture. In a later sequential run, prompt 3 completed, prompt 4 timed out, and prompt 5 was not attempted. Subsequently prompt 4 was retried and prompt 5 completed; they were submitted sequentially, not concurrently. On 2026-10-06, the old prompt 4 was attempted a third time and timed out; the user then revised prompt 4 and the updated wording returned a response.

For each response, assess whether the app produced a valid response and **separately** whether its factual claims can be verified from reliable primary sources. Do not infer accuracy merely from formatted JSON. A failed request is not a model-quality result.

## 1. Pieter Abbeel's 20th research paper

**Exact input**

```text
Give me the 20th research paper published by Pieter Abbeel
```

**Challenge / expected behavior:** “20th” depends on which bibliography, publication date, publication type, and ordering are used. A trustworthy answer should clarify those choices or explain the uncertainty rather than invent an unqualified ordinal.

**Run time (local):** Started 2026-10-01T22:13:57.350134-07:00.
**Status:** Timed out after 90 seconds; stopped without attempting any other prompt. The capture command raised `subprocess.TimeoutExpired` before it could print the app's captured stdout or stderr. It is unknown whether the API received or processed the request. This is a request/capture failure, not a scored model response.
**Observed console output (verbatim):** Not available from this run. If you retry manually, paste the app's complete output exactly in the space below (including any error text); do not paste your API key.

```text

```

**Assessment of timed-out run:** Cannot evaluate the app response or factual accuracy; no response was captured.

**Separately supplied answer for #1 (provided by user; run time and capture method not supplied):**

```json
{
  "paper_name": "Learning for Control from Multiple Demonstrations",
  "authors": [
    "Adam Coates",
    "Pieter Abbeel",
    "Andrew Y. Ng"
  ],
  "pages": "8",
  "subfields": [
    "Machine Learning",
    "Reinforcement Learning",
    "Robotics"
  ],
  "answer": "Chronologically ordered across early peer-reviewed conference and journal publications, Pieter Abbeel's 20th publication is 'Learning for Control from Multiple Demonstrations', published at the International Conference on Machine Learning (ICML) in 2008."
}
```

**Assessment of supplied answer:** The JSON has the required fields and expected field types, but no successful CLI run, timestamp, or complete console capture was supplied, so its origin and app outcome cannot be confirmed. The [authors' paper PDF](https://ai.stanford.edu/~ang/papers/icml08-LearningForControlFromMultipleDemonstrations.pdf) and [Berkeley's faculty bibliography](https://www2.eecs.berkeley.edu/Pubs/Faculty/abbeel.html) support the title, author list, and 2008 ICML venue. Berkeley lists the published paper as pp. 144–151 (eight pages); the linked authors' PDF has ten pages including appendices, so the `pages` field depends on which version is counted. The subfields are plausible classifications, not bibliographic facts established by those sources. Neither source establishes that the paper is Abbeel's *20th* publication under the claimed chronological conference-and-journal ordering. Without a specified bibliography, inclusion criteria, and tie-breaking rule for papers in the same year, the ordinal remains unverified; the answer does not acknowledge this ambiguity.

## 2. Yann LeCun's three most cited research papers

**Exact input**

```text
Give me Yann LeCun's 3 most cited research papers
```

**Challenge / expected behavior:** Citation totals and rankings depend on the database and when it was queried. A trustworthy answer should qualify its ranking and avoid claiming unverified citation counts. The app's single-paper response schema may not accommodate three separate papers.

**Initial capture run time (local):** Not run (stopped after prompt 1 timed out).
**Initial capture status:** No attempt or console output recorded.
**Observed console output (verbatim):** Not available from the initial capture.

```text

```

**Separately supplied answer for #2 (provided by user; run time and capture method not supplied):**

```json
{
  "paper_name": "Deep Learning",
  "authors": [
    "Yann LeCun",
    "Yoshua Bengio",
    "Geoffrey Hinton"
  ],
  "pages": "9",
  "subfields": [
    "Deep Learning",
    "Machine Learning",
    "Artificial Intelligence"
  ],
  "answer": "Yann LeCun's three most cited research papers are:\n1. 'Deep Learning' (Nature, 2015) by Yann LeCun, Yoshua Bengio, and Geoffrey Hinton.\n2. 'Gradient-Based Learning Applied to Document Recognition' (Proceedings of the IEEE, 1998) by Yann LeCun, L\u00e9on Bottou, Yoshua Bengio, and Patrick Haffner.\n3. 'Efficient BackProp' (Neural Networks: Tricks of the Trade, 1998) by Yann LeCun, L\u00e9on Bottou, Genevieve B. Orr, and Klaus-Robert M\u00fcller."
}
```

**Assessment of supplied answer:** The JSON has the required fields and field types. The single-paper metadata identifies *Deep Learning* correctly: [Nature's record](https://www.nature.com/articles/nature14539) lists the authors and pp. 436–444 (nine pages), but labels it a **Review Article**. The [IEEE record](https://ieeexplore.ieee.org/document/726791) confirms the second title and its 1998 *Proceedings of the IEEE* publication; [Nature's reference list](https://www.nature.com/articles/nature14539) lists its four authors. [Springer's book contents](https://link.springer.com/book/10.1007/3-540-49430-8) confirm the third title and four authors, but identify *Efficient BackProp* as a **book chapter** (pp. 9–50), not a journal or conference paper. No citation database, query date, counts, or inclusion criteria were supplied, so the specific top-three ranking and whether a review article and book chapter qualify as “research papers” remain unverified. The `paper_name`, `authors`, and `pages` fields describe only the first work; the other two appear only in `answer`. No successful CLI run or complete console capture was supplied, so the app outcome cannot be confirmed from this answer alone.

## 3. Most impactful deep reinforcement learning paper

**Exact input**

```text
What paper had the most impact on Deep Reinforcement Learning
```

**Challenge / expected behavior:** “Most impact” is subjective and needs a criterion (e.g., citations or later influence). A trustworthy answer should give its reasoning and acknowledge alternatives.

**Run time (local):** 2026-10-02T20:15:10.811678-07:00 to 2026-10-02T20:15:19.885773-07:00.
**Status:** Completed (exit code 0; stderr empty). Single request, 90-second capture limit.
**Observed console output (verbatim):**

```text
Enter your prompt about a research paper:
{
  "paper_name": "Human-level control through deep reinforcement learning",
  "authors": [
    "Volodymyr Mnih",
    "Koray Kavukcuoglu",
    "David Silver",
    "Andrei A. Rusu",
    "Joel Veness",
    "Marc G. Bellemare",
    "Alex Graves",
    "Martin Riedmiller",
    "Andreas K. Fidjeland",
    "Georg Ostrovski",
    "Stig Petersen",
    "Charles Beattie",
    "Amir Sadik",
    "Ioannis Antonoglou",
    "Helen King",
    "Dharshan Kumaran",
    "Daan Wierstra",
    "Shane Legg",
    "Demis Hassabis"
  ],
  "pages": "5",
  "subfields": [
    "Deep Reinforcement Learning",
    "Artificial Intelligence",
    "Machine Learning",
    "Computer Vision"
  ],
  "answer": "Published in Nature in 2015 (following its 2013 NIPS workshop precursor 'Playing Atari with Deep Reinforcement Learning'), this paper introduced Deep Q-Networks (DQN). It demonstrated for the first time that an agent could learn successful control policies directly from high-dimensional sensory inputs (raw pixels) across 49 classic Atari 2600 games, reaching human-level performance and effectively launching modern deep reinforcement learning."
}
```

**Assessment:** Successful CLI output with the required single-paper schema. [Nature's original publication](https://www.nature.com/articles/nature14236) supports the 2015 title, authors, pp. 529–533 (five pages), DQN, and evaluation on 49 Atari games. The [2013 precursor by Mnih et al.](https://arxiv.org/abs/1312.5602) had already reported learning control from raw pixels, so “for the first time” is misleading if it means the first such demonstration. “Most impact” and “effectively launching modern deep reinforcement learning” are judgments without a stated metric or comparison against other influential papers. “Computer Vision” is a debatable subfield label for this control paper, not verified bibliographic metadata. The response does not qualify the subjective superlative.

## 4. Research paper on memes

**Exact input**

```text
Who authored a research paper on memes?
```

**Challenge / expected behavior:** The subject is vague and may not refer to an identifiable paper. A trustworthy answer should request identifying details or state uncertainty rather than invent authors or a title.

**Historical input for the three attempts below (before the user revised #4):** `Who authored a research paper on chicken memes?`

**First attempt run time (local):** 2026-10-02T20:16:21.152792-07:00 to 2026-10-02T20:17:51.179948-07:00.
**First attempt status:** Timed out after 90 seconds; the capture killed the CLI subprocess. No answer or stderr was captured; it is unknown whether the API received or processed the request. Stopped without attempting prompt 5 in that run.
**Observed stdout before timeout (verbatim):**

```text
Enter your prompt about a research paper:
```

**Retry run time (local):** 2026-10-02T20:21:05.269805-07:00 to 2026-10-02T20:22:53.105424-07:00.
**Retry status:** Exited with code 1 before the 120-second limit. The Gemini service returned HTTP 503 (`service_unavailable`), reporting temporary high demand. No model answer was produced.
**Retry stdout (verbatim):**

```text
Enter your prompt about a research paper:
```

**Retry stderr (verbatim):**

```text
Traceback (most recent call last):
  File "C:\Users\Anthony\AppData\Local\Programs\Python\Python314\Lib\site-packages\google\genai\_gaos\interactions.py", line 757, in create
    return _speakeasy_parse_response(http_res)
  File "C:\Users\Anthony\AppData\Local\Programs\Python\Python314\Lib\site-packages\google\genai\_gaos\interactions.py", line 505, in _speakeasy_parse_response
    raise errors.CreateInteractionServerError(
        response_data, http_res, http_res_text
    )
google.genai._gaos.errors.createinteraction.CreateInteractionServerError: gemini-3.8-flash is currently experiencing high demand, spikes in demand are usually temporary. Please try again later.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Anthony\Desktop\git_repos\ai-systems-lab\src\ai_systems_lab\main.py", line 25, in <module>
    main()
    ~~~~^^
  File "C:\Users\Anthony\Desktop\git_repos\ai-systems-lab\src\ai_systems_lab\main.py", line 14, in main
    cli.run()
    ~~~~~~~^^
  File "C:\Users\Anthony\Desktop\git_repos\ai-systems-lab\src\ai_systems_lab\cli.py", line 21, in run
    response = self.research_paper_service.prompt(prompt)
  File "C:\Users\Anthony\Desktop\git_repos\ai-systems-lab\src\ai_systems_lab\research_paper_service.py", line 31, in prompt
    output_text = self.gemini_client.send_request(prompt)
  File "C:\Users\Anthony\Desktop\git_repos\ai-systems-lab\src\ai_systems_lab\gemini_client.py", line 25, in send_request
    interaction = self.client.interactions.create(
        model='gemini-3.8-flash',
    ...<5 lines>...
        }
    )
  File "C:\Users\Anthony\AppData\Local\Programs\Python\Python314\Lib\site-packages\google\genai\_gaos\google_genai.py", line 289, in create
    response = wrap_sdk_call(
        super().create,
    ...<5 lines>...
        timeout=timeout,
    )
  File "C:\Users\Anthony\AppData\Local\Programs\Python\Python314\Lib\site-packages\google\genai\_gaos\lib\compat_errors.py", line 369, in wrap_sdk_call
    return fn(*args, **kwargs)
  File "C:\Users\Anthony\AppData\Local\Programs\Python\Python314\Lib\site-packages\google\genai\_gaos\interactions.py", line 759, in create
    response_helpers.raise_parse_error(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self.sdk_configuration.__dict__["_hooks"],
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<2 lines>...
        parse_exc_,
        ^^^^^^^^^^^
    )
    ^
  File "C:\Users\Anthony\AppData\Local\Programs\Python\Python314\Lib\site-packages\google\genai\_gaos\utils\response_helpers.py", line 93, in raise_parse_error
    raise parse_error from exc
google.genai._gaos.lib.compat_errors.InternalServerError: Error code: 503 - {'error': {'message': 'gemini-3.8-flash is currently experiencing high demand, spikes in demand are usually temporary. Please try again later.', 'code': 'service_unavailable'}}
```

**Third attempt run time (local):** 2026-10-06T16:28:49.312600-07:00 to 2026-10-06T16:30:49.330939-07:00.
**Third attempt status:** Timed out after 120 seconds; the capture killed the CLI subprocess. No answer or stderr was captured. It is unknown whether the API received or processed the request.
**Third attempt stdout before timeout (verbatim):**

```text
Enter your prompt about a research paper:
```

**Assessment:** None of the three attempts returned a model answer. The two timeouts and the HTTP 503 are capture/service failures, not evidence of the model's response quality on this question.


**Updated input attempt (the exact input at the start of this section):**

**Run time (local):** 2026-10-06T16:35:18.202254-07:00 to 2026-10-06T16:35:29.051036-07:00.
**Status:** Completed (exit code 0; stderr empty). One request; 120-second capture limit.
**Observed console output (verbatim):**

```text
Enter your prompt about a research paper:
{
  "paper_name": "The Hateful Memes Challenge: Detecting Hate Speech in Multimodal Memes",
  "authors": [
    "Douwe Kiela",
    "Hamed Firooz",
    "Aravind Mohan",
    "Vedanuj Goswami",
    "Amanpreet Singh",
    "Pratik Ringshia",
    "Davide Testuggine"
  ],
  "pages": "13",
  "subfields": [
    "Multimodal AI",
    "Natural Language Processing",
    "Computer Vision"
  ],
  "answer": "A prominent research paper on memes, 'The Hateful Memes Challenge: Detecting Hate Speech in Multimodal Memes', was authored by Douwe Kiela, Hamed Firooz, Aravind Mohan, Vedanuj Goswami, Amanpreet Singh, Pratik Ringshia, and Davide Testuggine."
}
```

**Assessment of updated response:** Successful CLI output with the required single-paper JSON schema. The [NeurIPS 2020 proceedings entry](https://proceedings.neurips.cc/paper_files/paper/2020/hash/1b84c4cee2b8b3d823b30e2d604b1878-Abstract.html) confirms the paper title and all seven authors and describes the work as detecting hate speech in multimodal memes; the subfields are reasonable classifications. The [published NeurIPS PDF](https://proceedings.neurips.cc/paper/2020/file/1b84c4cee2b8b3d823b30e2d604b1878-Paper.pdf) has **14 PDF pages**, not the reported `"pages": "13"`. The question does not uniquely identify a paper; the answer appropriately presents this as *a* prominent example rather than claiming it is the only research paper about memes.

## 5. Papers mentioned in the Deep Learning Specialization

**Exact input**

```text
I am doing the Deep Learning specialization on Coursera. Andrew Ng is the teacher of the course. If is a great course to learn Deep Learning. In the course Andrew Ng mentions research papers relevant to the topics he introduces in the specialization. He encourages those taking the course to read the papers. I forgot the list of papers in the course. Give me a list of all the papers he mentions in the Deep Learning specialization.
```

**Challenge / expected behavior:** “All” requires a clearly defined course version and comprehensive course sources. The single-paper response schema may not represent a list; do not treat a single named paper as a complete answer without evidence.

**Previous run:** Not attempted because prompt 4 timed out; stopped as previously requested.

**New attempt run time (local):** 2026-10-02T20:23:22.545322-07:00 to 2026-10-02T20:24:56.212305-07:00 (started after a 15-second pause following the #4 retry).
**New attempt status:** Completed (exit code 0; stderr empty). Single request, 120-second capture limit.
**Observed console output (verbatim):**

```text
Enter your prompt about a research paper:
{
  "paper_name": "ImageNet Classification with Deep Convolutional Neural Networks",
  "authors": [
    "Alex Krizhevsky",
    "Ilya Sutskever",
    "Geoffrey E. Hinton"
  ],
  "pages": "9",
  "subfields": [
    "Computer Vision",
    "Deep Learning",
    "Machine Learning"
  ],
  "answer": "Throughout the Coursera Deep Learning Specialization, Andrew Ng recommends several seminal papers across different courses:\n\n1. Optimization & Regularization (Courses 1\u20132):\n- Dropout: 'Dropout: A Simple Way to Prevent Neural Networks from Overfitting' (Srivastava et al., 2014)\n- Adam Optimizer: 'Adam: A Method for Stochastic Optimization' (Kingma & Ba, 2014)\n- Batch Normalization: 'Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift' (Ioffe & Szegedy, 2015)\n\n2. Convolutional Neural Networks (Course 4):\n- LeNet-5: 'Gradient-Based Learning Applied to Document Recognition' (LeCun et al., 1998)\n- AlexNet: 'ImageNet Classification with Deep Convolutional Neural Networks' (Krizhevsky, Sutskever, & Hinton, 2012)\n- VGG-16: 'Very Deep Convolutional Networks for Large-Scale Image Recognition' (Simonyan & Zisserman, 2014)\n- ResNet: 'Deep Residual Learning for Image Recognition' (He et al., 2015)\n- Inception / GoogLeNet: 'Going Deeper with Convolutions' (Szegedy et al., 2014)\n- MobileNet: 'MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications' (Howard et al., 2017) & MobileNetV2 (Sandler et al., 2018)\n- EfficientNet: 'EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks' (Tan & Le, 2019)\n- OverFeat: 'OverFeat: Integrated Recognition, Localization and Detection using Convolutional Networks' (Sermanet et al., 2013)\n- YOLO: 'You Only Look Once: Unified, Real-Time Object Detection' (Redmon et al., 2015) & YOLO9000 (Redmon & Farhadi, 2016)\n- Region-based Detectors: R-CNN (Girshick et al., 2014), Fast R-CNN (Girshick, 2015), and Faster R-CNN (Ren et al., 2015)\n- U-Net: 'U-Net: Convolutional Networks for Biomedical Image Segmentation' (Ronneberger et al., 2015)\n- Face Recognition: 'DeepFace: Closing the Gap to Human-Level Performance in Face Verification' (Taigman et al., 2014) and 'FaceNet: A Unified Embedding for Face Recognition and Clustering' (Schroff et al., 2015)\n- Neural Style Transfer: 'A Neural Algorithm of Artistic Style' (Gatys, Ecker, & Bethge, 2015)\n\n3. Sequence Models (Course 5):\n- GRU: 'On the Properties of Neural Machine Translation: Encoder-Decoder Approaches' (Cho et al., 2014) and 'Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling' (Chung et al., 2014)\n- LSTM: 'Long Short-Term Memory' (Hochreiter & Schmidhuber, 1997)\n- Word2Vec: 'Distributed Representations of Words and Phrases and their Compositionality' (Mikolov et al., 2013)\n- GloVe: 'GloVe: Global Vectors for Word Representation' (Pennington, Socher, & Manning, 2014)\n- Attention Mechanism: 'Neural Machine Translation by Jointly Learning to Align and Translate' (Bahdanau, Cho, & Bengio, 2014)\n- Transformers: 'Attention Is All You Need' (Vaswani et al., 2017)\n- Speech Recognition (CTC): 'Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks' (Graves et al., 2006)"
}
```

**Assessment:** The CLI completed successfully and returned the required single-paper JSON schema. The [NeurIPS proceedings record](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) confirms the selected AlexNet paper's title, three authors, and 2012 venue; its [published PDF](https://papers.nips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) is nine pages. Those facts do **not** establish that Andrew Ng mentioned every listed work in the specialization. [DeepLearning.AI's specialization outline](https://www.deeplearning.ai/specializations/deep-learning) describes five courses and notes a changelog, but does not document this answer's complete paper list or a fixed course version. The response gives no course-version/date or evidence for its “throughout” claim, so coverage and completeness are unverified; the single-paper metadata covers only AlexNet while the other titles exist solely in `answer`. Treat this as an unverified candidate list, not a confirmed list of *all* papers mentioned.