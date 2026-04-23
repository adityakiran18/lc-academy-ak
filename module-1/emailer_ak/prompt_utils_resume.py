
#--------------------------------------------------------------------------------
job_url = """
https://cvshealth.wd1.myworkdayjobs.com/en-US/CVS_Health_Careers/job/MA---Wellesley/Senior-Data-Scientist---Agentic-AI---Decision-Intelligence_R0889533
"""
#--------------------------------------------------------------------------------
jd_text = """

Senior Data Scientist - Agentic AI & Decision Intelligence


R0889533
We’re building a world of health around every individual — shaping a more connected, convenient and compassionate health experience. At CVS Health®, you’ll be surrounded by passionate colleagues who care deeply, innovate with purpose, hold ourselves accountable and prioritize safety and quality in everything we do. Join us and be part of something bigger – helping to simplify health care one person, one family and one community at a time.


Requisition Job Description

Position Summary
We are seeking a Sr. Data Scientist – Agentic AI & Decision Intelligence to pioneer the next generation of analytics and data driven decision-making. This role will focus on building and scaling agentic AI frameworks, conversational analytics, and decision intelligence systems that transform how our business interacts with data. You will design and execute a customer-centric analytics strategy powered by AI agents, LLMs, and generative AI, ensuring insights are not just delivered, but acted upon. This is a highly visible role where you will contribute to the vision, strategy, and own the execution of AI-driven decision systems, positioning the organization at the forefront of intelligent business analytics.

Required Qualifications

3+ years of experience in advanced analytics, decision science, applied AI/ML
Strong programming skills in Python and SQL, with experience deploying AI systems in cloud environments (GCP, AWS, or Azure).
Deep expertise in at least one area of advanced modeling: predictive analytics, reinforcement learning, NLP, or causal inference.
Proven ability to translate complex AI concepts into business impact, including stakeholder alignment and business value sizing.
Experience leading end-to-end AI-driven solution delivery: from data foundation to model orchestration to front-end adoption.
Hands-on experience with LLMs, generative AI, or conversational AI frameworks (e.g., LangChain, RAG).
Strong communication, storytelling, and customer engagement skills, with a passion for building solutions that are intuitive and impactful.

Preferred Qualifications

Experience implementing agentic AI systems for conversational analytics, autonomous reporting, or decision support.
Familiarity with Vertex AI and Google Cloud Platform, or equivalent enterprise AI platforms.
Familiarity with BI tools (Tableau, Looker, Power BI) and analytics engineering (Snowflake, modern warehouses).
Background in healthcare or pharmacy analytics, with a strong interest in improving outcomes through intelligent decision systems.
Experience with UI/UX design, customer journey mapping, and design thinking (Figma experience is a plus).
Knowledge of data observability, governance, and AI ethics to ensure trustworthy, transparent decision intelligence systems.

Education

Bachelor's degree or equivalent work experience in Mathematics, Statistics, Computer Science, Business Analytics, Economics, Physics, Engineering, or related discipline. 

Master’s degree or PhD preferred

Anticipated Weekly Hours

40
Time Type

Full time
Pay Range

The typical pay range for this role is:

$111,240.00 - $222,480.00

"""

#--------------------------------------------------------------------------------
project_experience = """
I am using the STAR method to describe the projects.

S (situation)
T (Task)
A (Action)
R (Result)

—- project--------------

❼ Developed an automated A/B test analyzing suite powered by multi-Agentic AI

model. This suite analyzed A/B test data and generated actionable insights.

The solution drove a projected $7M annual incremental revenue.



SITUATION:

  Our internal experience serving engine is called DAPI (Decision API). It takes in the user context and realtime shows it an experience. DAPI learns to show the optimal experiences by using the reward using RL. The live test performance is shown on a dashboard which has all the various charts and visuals. The analysts analyze these plots and come up with actions such as adding a new feature or adding/removing an experience. Now the pain point here is that the process is very manual. This manual process significantly inhibited scalability across multiple use cases, necessitating automation



TASK:

  Now we have to build an Agentic model that takes in all the charts and various analyses to come up with a report and actionable recommendations



ACTION:

  We used an Agentic framework, orchestrated by LangGraph. The graph takes in the data analyses and visuals as inputs. The graph features various LLM-nodes, each designed to capture different aspects of the analyses (e.g., Bandit vs. holdout, week-over-week, asset-level, feature-level). Inputs are passed between these nodes as needed. Each node functions as a subgraph, containing further 'What' and 'Why' LLM-	nodes. 'What'-nodes focus on factual observations, while 'Why'-nodes provide reasoning for connections and explain the Bandit performance. The main advantages of LangGraph came in the form of 

RAG 

HITL

For RAG, we used pinecone vectors of the Documentation pages of DAPI. Whenever any LLM doesn’t understand any terminology given in the HITL or how DAPI works, it can refer to the RAG vectors.

For the HITL, within each subgraph, after the What and Why LLM-node are evaluated, the model prompts the HITL to enter any feedback. Then we use a feedback separator (another LLM call) that separates the HITL feedback and breaks it apart and passes it onto the What/Why nodes.

 The State messages are very easily passable between the nodes.



The model was used by the analysts who interacted with it and rated it on certain predefined benchmark questions. We designed an LLM evaluation judge system which compared the manual vs LLM outputs and grade them and call out any incorrect responses. The qualifying was when each node hit over 90% accuracy. Then we generalized the codebase so that it is usable across other businesses.



RESULT:

   In the evaluations, the model hit 100% on TIER1 tasks and over 90% on TIER2 tasks (reasoning tasks). The model reduced analyst time by 65%. Upon imposing certain assumptions, we projected the impact of full rollout to $7MM annual incremental lift to the company.



—-Next project--------------

❼ Utilized AI and unsupervised learning to discover audience segments from web

traffic data. The model’s vast adoption led to significant time-savings.

SITUATION: 

    There is a lot of rich session data of users browsing through our pages. So understanding the users’ interests so that we can design experiences that they lie and engage more with, is critical. However there was no automated process in place. We just had  analysts manually segmenting them based on empirical observations and domain experience. So the manual effort was a painpoint



TASK: 

    So now the task is to automate the process of intaking the session data and coming up with useful segments and user insights that will help create better experiences. 



ACTION:

    I used an Agentic AI model powered by LangGraph. The graph takes in the site on which we want to segment the audiences. 

It takes screenshots of the page and observes all the site UI elements. These are used when recommending experiences

 It runs interviews to generate hypotheses from business documentation 

Creative + realistic + skeptic   

Then it pulls in the data using SQL and comes up with data-driven segments and personas.

Data ingestion

Data cleaning 

Feature engineering 

Model selection

We club both the personas and shortlist to topN personas

For the chosen personas, the agent asks for user feedback. If they are distinct and realistic

It creates data ledger where it assigns the data points to their clusters

For hypothesis personas, 

wIthin each perona, pick keystone, 

define the properties of that persona

Define the behaviors

Finally the personas are saved into a pdf





RESULT:

The model received wide spread attention among the analyst across various businesses

It led to a time-savings of 65% compared to the manual efforts.


—-Next project--------------

❼ Designed a revenue-optimized content recommendation engine that led to a 13%

increase in Ad revenue while maintaining key page engagement metrics.

ss

SITUATION:

   The BAU contention recommendation engine was only using content similarity of the recommendation wrt the landing page. Because of that we were leaving out showing other recommendation pages which were almost equally similar but fetched more revenue.



TASK:

    The task is to develop a recommender system or ranking system which takes into account both the contextual similarity and also its average revenue per page (RPV)



ACTION

    I formulated an objective function which is directly proportional to the RPV of a candidate page and inversely proportional to the distance between the vector embeddings of the candidate and landing page. The function was inspired by the Gravitational inverse square law. 

For the embeddings I used the SpaCy universal sentence encoder from Hugging face. I also tried the BERT sentence encoder. The objective function had 2 parameters/dials that increased the emphasis on the RPV and the vector distance. The optimization problem was formulated as a minimax saddle point problem where we maximize the RPV while we minimize the vector distance. The optimal model parameters were found using a Bayesian grid search. The simulations showed promising lifts in the RPV and almost-zero drop in the contextual similarity score. The method was A/B tested thoroughly using best Experimentation practices to get statistically significant lift results.



RESULT:

    The business was very impressed by the model performance and readily adopted it. It led to a 13% increase in the RPV which is a massive win for a high revenue business like Healthline. Eventually 7 other businesses like CNET, Bankrate, Edu, The Points GUY, etc.,  have also adopted, leading to great wins and promoted me to a senior Data Scientist.

 



—-Next project--------------

❼ Applied PID-based controlling mechanism to predict optimal budgets in Ad

campaigns.

    Used a control theory inspired mechanism to control the budgets for the Google MCV tool. The tool tuned the 3 parameters using the feedback loop and Zieglers-Nichols method. The model was an experimental project. The pain point was that the budget adjustments were being done manually and it was educative guesses taking a lot of time as there were a lot of Ad-campaigns. So we needed this PID model to improve the accuracy and efficiency.

The model was developed and it led to an increased revenue due to making optimal budget bid adjustments and achieving increased leads, and also cutting down analyst time.



—-These are tiny one-off projects. Use them ONLY IF they align strongly with the JD--------------

- built a user propensity model, which took all the user attributes and applied an XGBoost regressor  on top to predict the likelihood of a user clicking

- worked on an LLM-finetuning; We had an AI-powered phonecall IVR system. To finetune that I took a LLAMA-3 base model and finetuned it with human analyst conversations from the past. Used PEFT (LoRA). Used responsible-AI practices.

#####################################################
"""