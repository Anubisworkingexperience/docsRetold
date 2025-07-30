from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """ Artificial general intelligence (AGI)—sometimes called human‑level intelligence AI—is a type of artificial intelligence that would match or surpass human capabilities across virtually all cognitive tasks.[1][2]

Some researchers argue that state‑of‑the‑art large language models (LLMs) already exhibit signs of AGI‑level capability, while others maintain that genuine AGI has not yet been achieved.[3] AGI is conceptually distinct from artificial superintelligence (ASI), which would outperform the best human abilities across every domain by a wide margin.[4] AGI is considered one of the definitions of strong AI.

Unlike artificial narrow intelligence (ANI), whose competence is confined to well‑defined tasks, an AGI system can generalise knowledge, transfer skills between domains, and solve novel problems without task‑specific reprogramming. The concept does not, in principle, require the system to be an autonomous agent; a static model—such as a highly capable large language model—or an embodied robot could both satisfy the definition so long as human‑level breadth and proficiency are achieved.[5]

Creating AGI is a primary goal of AI research and of companies such as OpenAI,[6] Google,[7] and Meta.[8] A 2020 survey identified 72 active AGI research and development projects across 37 countries.[9]

The timeline for achieving human‑level intelligence AI remains deeply contested. Recent surveys of AI researchers give median forecasts ranging from the late 2020s to mid‑century, while still recording significant numbers who expect arrival much sooner—or never at all.[10][11][12] There is debate on the exact definition of AGI and regarding whether modern LLMs such as GPT-4 are early forms of emerging AGI.[3] AGI is a common topic in science fiction and futures studies.[13][14]

Contention exists over whether AGI represents an existential risk.[15][16][17] Many AI experts have stated that mitigating the risk of human extinction posed by AGI should be a global priority.[18][19] Others find the development of AGI to be in too remote a stage to present such a risk.[20][21]

Terminology
AGI is also known as strong AI,[22][23] full AI,[24] human-level AI,[25] human-level intelligent AI, or general intelligent action.[26]

Some academic sources reserve the term "strong AI" for computer programs that will experience sentience or consciousness.[a] In contrast, weak AI (or narrow AI) is able to solve one specific problem but lacks general cognitive abilities.[27][23] Some academic sources use "weak AI" to refer more broadly to any programs that neither experience consciousness nor have a mind in the same sense as humans.[a]

Related concepts include artificial superintelligence and transformative AI. An artificial superintelligence (ASI) is a hypothetical type of AGI that is much more generally intelligent than humans,[28] while the notion of transformative AI relates to AI having a large impact on society, for example, similar to the agricultural or industrial revolution.[29]

A framework for classifying AGI by performance and autonomy was proposed in 2023 by Google DeepMind researchers.[30] They define five performance levels of AGI: emerging, competent, expert, virtuoso, and superhuman.[30] For example, a competent AGI is defined as an AI that outperforms 50% of skilled adults in a wide range of non-physical tasks, and a superhuman AGI (i.e. an artificial superintelligence) is similarly defined but with a threshold of 100%.[30] They consider large language models like ChatGPT or LLaMA 2 to be instances of emerging AGI (comparable to unskilled humans).[30] Regarding the autonomy of AGI and associated risks, they define five levels: tool (fully in human control), consultant, collaborator, expert, and agent (fully autonomous).[31]

Characteristics
Main article: Artificial intelligence
Various popular definitions of intelligence have been proposed. One of the leading proposals is the Turing test. However, there are other well-known definitions, and some researchers disagree with the more popular approaches.[b]

Intelligence traits
Researchers generally hold that a system is required to do all of the following to be regarded as an AGI:[33]

reason, use strategy, solve puzzles, and make judgments under uncertainty
represent knowledge, including common sense knowledge
plan
learn
communicate in natural language
if necessary, integrate these skills in completion of any given goal
Many interdisciplinary approaches (e.g. cognitive science, computational intelligence, and decision making) consider additional traits such as imagination (the ability to form novel mental images and concepts)[34] and autonomy.[35]

Computer-based systems that exhibit many of these capabilities exist (e.g. see computational creativity, automated reasoning, decision support system, robot, evolutionary computation, intelligent agent). There is debate about whether modern AI systems possess them to an adequate degree.[36]

Physical traits
Other capabilities are considered desirable in intelligent systems, as they may affect intelligence or aid in its expression. These include:[37]

the ability to sense (e.g. see, hear, etc.), and
the ability to act (e.g. move and manipulate objects, change location to explore, etc.)
This includes the ability to detect and respond to hazard.[38]

Although the ability to sense (e.g. see, hear, etc.) and the ability to act (e.g. move and manipulate objects, change location to explore, etc.) can be desirable for some intelligent systems,[37] these physical capabilities are not strictly required for an entity to qualify as AGI—particularly under the thesis that large language models (LLMs) may already be or become AGI. Even from a less optimistic perspective on LLMs, there is no firm requirement for an AGI to have a human-like form; being a silicon-based computational system is sufficient, provided it can process input (language) from the external world in place of human senses. This interpretation aligns with the understanding that AGI has never been proscribed a particular physical embodiment and thus does not demand a capacity for locomotion or traditional "eyes and ears".[38] It can be regarded as sufficient for an intelligent computer to interact with other systems, to invoke or regulate them, to achieve specific goals, including altering a physical environment, as HAL in 2001: A Space Odyssey was both programmed and tasked to.[39]

Tests for human-level AGI
Several tests meant to confirm human-level AGI have been considered, including:[40][41]

The Turing Test (Turing)

The Turing test can provide some evidence of intelligence, but it penalizes non-human intelligent behavior and may incentivize artificial stupidity.[42]
Proposed by Alan Turing in his 1950 paper "Computing Machinery and Intelligence", this test involves a human judge engaging in natural language conversations with both a human and a machine designed to generate human-like responses. The machine passes the test if it can convince the judge it is human a significant fraction of the time. Turing proposed this as a practical measure of machine intelligence, focusing on the ability to produce human-like responses rather than on the internal workings of the machine.[43]
Turing described the test as follows:
The idea of the test is that the machine has to try and pretend to be a man, by answering questions put to it, and it will only pass if the pretence is reasonably convincing. A considerable portion of a jury, who should not be expert about machines, must be taken in by the pretence.[44]

In 2014, a chatbot named Eugene Goostman, designed to imitate a 13-year-old Ukrainian boy, reportedly passed a Turing Test event by convincing 33% of judges that it was human. However, this claim was met with significant skepticism from the AI research community, who questioned the test's implementation and its relevance to AGI.[45][46]
In 2023, it was claimed that "AI is closer to ever" to passing the Turing test, though the article's authors reinforced that imitation (as "large language models" ever closer to passing the test are built upon) is not synonymous with "intelligence". Further, as AI intelligence and human intelligence may differ, "passing the Turing test is good evidence a system is intelligent, failing it is not good evidence a system is not intelligent."[47]
A 2024 study suggested that GPT-4 was identified as human 54% of the time in a randomized, controlled version of the Turing Test—surpassing older chatbots like ELIZA while still falling behind actual humans (67%).[48]
A 2025 pre‑registered, three‑party Turing‑test study by Cameron R. Jones and Benjamin K. Bergen showed that GPT-4.5 was judged to be the human in 73% of five‑minute text conversations—surpassing the 67% humanness rate of real confederates and meeting the researchers’ criterion for having passed the test.[49][50]
The Robot College Student Test (Goertzel)
A machine enrolls in a university, taking and passing the same classes that humans would, and obtaining a degree. LLMs can now pass university degree-level exams without even attending the classes.[51]
The Employment Test (Nilsson)
A machine performs an economically important job at least as well as humans in the same job. AIs are now replacing humans in many roles as varied as fast food and marketing.[52]
The Ikea test (Marcus)
Also known as the Flat Pack Furniture Test. An AI views the parts and instructions of an Ikea flat-pack product, then controls a robot to assemble the furniture correctly.[53]
The Coffee Test (Wozniak)
A machine is required to enter an average American home and figure out how to make coffee: find the coffee machine, find the coffee, add water, find a mug, and brew the coffee by pushing the proper buttons.[54] This has not yet been completed.
The Modern Turing Test (Suleyman)
An AI model is given $100,000 and has to obtain $1 million.[55][56]
AI-complete problems
Main article: AI-complete
A problem is informally called "AI-complete" or "AI-hard" if it is believed that in order to solve it, one would need to implement AGI, because the solution is beyond the capabilities of a purpose-specific algorithm.[57]

There are many problems that have been conjectured to require general intelligence to solve as well as humans. Examples include computer vision, natural language understanding, and dealing with unexpected circumstances while solving any real-world problem.[58] Even a specific task like translation requires a machine to read and write in both languages, follow the author's argument (reason), understand the context (knowledge), and faithfully reproduce the author's original intent (social intelligence). All of these problems need to be solved simultaneously in order to reach human-level machine performance.

However, many of these tasks can now be performed by modern large language models. According to Stanford University's 2024 AI index, AI has reached human-level performance on many benchmarks for reading comprehension and visual reasoning.[59]

History
Classical AI
Main articles: History of artificial intelligence and Symbolic artificial intelligence
Modern AI research began in the mid-1950s.[60] The first generation of AI researchers were convinced that artificial general intelligence was possible and that it would exist in just a few decades.[61] AI pioneer Herbert A. Simon wrote in 1965: "machines will be capable, within twenty years, of doing any work a man can do."[62]

Their predictions were the inspiration for Stanley Kubrick and Arthur C. Clarke's character HAL 9000, who embodied what AI researchers believed they could create by the year 2001. AI pioneer Marvin Minsky was a consultant[63] on the project of making HAL 9000 as realistic as possible according to the consensus predictions of the time. He said in 1967, "Within a generation... the problem of creating 'artificial intelligence' will substantially be solved".[64]

Several classical AI projects, such as Doug Lenat's Cyc project (that began in 1984), and Allen Newell's Soar project, were directed at AGI.

However, in the early 1970s, it became obvious that researchers had grossly underestimated the difficulty of the project. Funding agencies became skeptical of AGI and put researchers under increasing pressure to produce useful "applied AI".[c] In the early 1980s, Japan's Fifth Generation Computer Project revived interest in AGI, setting out a ten-year timeline that included AGI goals like "carry on a casual conversation".[68] In response to this and the success of expert systems, both industry and government pumped money into the field.[66][69] However, confidence in AI spectacularly collapsed in the late 1980s, and the goals of the Fifth Generation Computer Project were never fulfilled.[70] For the second time in 20 years, AI researchers who predicted the imminent achievement of AGI had been mistaken. By the 1990s, AI researchers had a reputation for making vain promises. They became reluctant to make predictions at all[d] and avoided mention of "human level" artificial intelligence for fear of being labeled "wild-eyed dreamer[s]".[72]

Narrow AI research
Main article: Artificial intelligence
In the 1990s and early 21st century, mainstream AI achieved commercial success and academic respectability by focusing on specific sub-problems where AI can produce verifiable results and commercial applications, such as speech recognition and recommendation algorithms.[73] These "applied AI" systems are now used extensively throughout the technology industry, and research in this vein is heavily funded in both academia and industry. As of 2018, development in this field was considered an emerging trend, and a mature stage was expected to be reached in more than 10 years.[74]

At the turn of the century, many mainstream AI researchers[75] hoped that strong AI could be developed by combining programs that solve various sub-problems. Hans Moravec wrote in 1988:

I am confident that this bottom-up route to artificial intelligence will one day meet the traditional top-down route more than half way, ready to provide the real-world competence and the commonsense knowledge that has been so frustratingly elusive in reasoning programs. Fully intelligent machines will result when the metaphorical golden spike is driven uniting the two efforts.[75]

However, even at the time, this was disputed. For example, Stevan Harnad of Princeton University concluded his 1990 paper on the symbol grounding hypothesis by stating:

The expectation has often been voiced that "top-down" (symbolic) approaches to modeling cognition will somehow meet "bottom-up" (sensory) approaches somewhere in between. If the grounding considerations in this paper are valid, then this expectation is hopelessly modular and there is really only one viable route from sense to symbols: from the ground up. A free-floating symbolic level like the software level of a computer will never be reached by this route (or vice versa) – nor is it clear why we should even try to reach such a level, since it looks as if getting there would just amount to uprooting our symbols from their intrinsic meanings (thereby merely reducing ourselves to the functional equivalent of a programmable computer).[76]

Modern artificial general intelligence research
The term "artificial general intelligence" was used as early as 1997, by Mark Gubrud[77] in a discussion of the implications of fully automated military production and operations. A mathematical formalism of AGI was proposed by Marcus Hutter in 2000. Named AIXI, the proposed AGI agent maximises "the ability to satisfy goals in a wide range of environments".[78] This type of AGI, characterized by the ability to maximise a mathematical definition of intelligence rather than exhibit human-like behaviour,[79] was also called universal artificial intelligence.[80]

The term AGI was re-introduced and popularized by Shane Legg and Ben Goertzel around 2002.[81] AGI research activity in 2006 was described by Pei Wang and Ben Goertzel[82] as "producing publications and preliminary results". The first summer school in AGI was organized in Xiamen, China in 2009[83] by the Xiamen university's Artificial Brain Laboratory and OpenCog. The first university course was given in 2010[84] and 2011[85] at Plovdiv University, Bulgaria by Todor Arnaudov. MIT presented a course on AGI in 2018, organized by Lex Fridman and featuring a number of guest lecturers.

As of 2023, a small number of computer scientists are active in AGI research, and many contribute to a series of AGI conferences. However, increasingly more researchers are interested in open-ended learning,[86][3] which is the idea of allowing AI to continuously learn and innovate like humans do.

Feasibility

Surveys about when experts expect artificial general intelligence[25]
As of 2023, the development and potential achievement of AGI remains a subject of intense debate within the AI community. While traditional consensus held that AGI was a distant goal, recent advancements have led some researchers and industry figures to claim that early forms of AGI may already exist.[87] AI pioneer Herbert A. Simon speculated in 1965 that "machines will be capable, within twenty years, of doing any work a man can do". This prediction failed to come true. Microsoft co-founder Paul Allen believed that such intelligence is unlikely in the 21st century because it would require "unforeseeable and fundamentally unpredictable breakthroughs" and a "scientifically deep understanding of cognition".[88] Writing in The Guardian, roboticist Alan Winfield claimed the gulf between modern computing and human-level artificial intelligence is as wide as the gulf between current space flight and practical faster-than-light spaceflight.[89]

A further challenge is the lack of clarity in defining what intelligence entails. Does it require consciousness? Must it display the ability to set goals as well as pursue them? Is it purely a matter of scale such that if model sizes increase sufficiently, intelligence will emerge? Are facilities such as planning, reasoning, and causal understanding required? Does intelligence require explicitly replicating the brain and its specific faculties? Does it require emotions?[90]

Most AI researchers believe strong AI can be achieved in the future, but some thinkers, like Hubert Dreyfus and Roger Penrose, deny the possibility of achieving strong AI.[91][92] John McCarthy is among those who believe human-level AI will be accomplished, but that the present level of progress is such that a date cannot accurately be predicted.[93] AI experts' views on the feasibility of AGI wax and wane. Four polls conducted in 2012 and 2013 suggested that the median estimate among experts for when they would be 50% confident AGI would arrive was 2040 to 2050, depending on the poll, with the mean being 2081. Of the experts, 16.5% answered with "never" when asked the same question but with a 90% confidence instead.[94][95] Further current AGI progress considerations can be found above Tests for confirming human-level AGI.

A report by Stuart Armstrong and Kaj Sotala of the Machine Intelligence Research Institute found that "over [a] 60-year time frame there is a strong bias towards predicting the arrival of human-level AI as between 15 and 25 years from the time the prediction was made". They analyzed 95 predictions made between 1950 and 2012 on when human-level AI will come about.[96]

In 2023, Microsoft researchers published a detailed evaluation of GPT-4. They concluded: "Given the breadth and depth of GPT-4’s capabilities, we believe that it could reasonably be viewed as an early (yet still incomplete) version of an artificial general intelligence (AGI) system."[97] Another study in 2023 reported that GPT-4 outperforms 99% of humans on the Torrance tests of creative thinking.[98][99]

Blaise Agüera y Arcas and Peter Norvig wrote in 2023 that a significant level of general intelligence has already been achieved with frontier models. They wrote that reluctance to this view comes from four main reasons: a "healthy skepticism about metrics for AGI", an "ideological commitment to alternative AI theories or techniques", a "devotion to human (or biological) exceptionalism", or a "concern about the economic implications of AGI".[100]

2023 also marked the emergence of large multimodal models (large language models capable of processing or generating multiple modalities such as text, audio, and images).[101]

In 2024, OpenAI released o1-preview, the first of a series of models that "spend more time thinking before they respond". According to Mira Murati, this ability to think before responding represents a new, additional paradigm. It improves model outputs by spending more computing power when generating the answer, whereas the model scaling paradigm improves outputs by increasing the model size, training data and training compute power.[102][103]

An OpenAI employee, Vahid Kazemi, claimed in 2024 that the company had achieved AGI, stating, "In my opinion, we have already achieved AGI and it's even more clear with O1." Kazemi clarified that while the AI is not yet "better than any human at any task", it is "better than most humans at most tasks." He also addressed criticisms that large language models (LLMs) merely follow predefined patterns, comparing their learning process to the scientific method of observing, hypothesizing, and verifying. These statements have sparked debate, as they rely on a broad and unconventional definition of AGI—traditionally understood as AI that matches human intelligence across all domains. Critics argue that, while OpenAI's models demonstrate remarkable versatility, they may not fully meet this standard. Notably, Kazemi's comments came shortly after OpenAI removed "AGI" from the terms of its partnership with Microsoft, prompting speculation about the company's strategic intentions.[104]

Timescales

AI has surpassed humans on a variety of language understanding and visual understanding benchmarks.[105] As of 2023, foundation models still lack advanced reasoning and planning capabilities, but rapid progress is expected.[106]
Progress in artificial intelligence has historically gone through periods of rapid progress separated by periods when progress appeared to stop.[91] Ending each hiatus were fundamental advances in hardware, software or both to create space for further progress.[91][107][108] For example, the computer hardware available in the twentieth century was not sufficient to implement deep learning, which requires large numbers of GPU-enabled CPUs.[109]

Elon Musk believes that the automation of society will require governments to adopt a universal basic income.[188]
"""
print(summarizer(ARTICLE, max_length=300, min_length=30, do_sample=False))
# >>> [{'summary_text': 'Liana Barrientos, 39, is charged with two counts of "offering a false instrument for filing in the first degree" In total, she has been married 10 times, with nine of her marriages occurring between 1999 and 2002. She is believed to still be married to four men.'}]
