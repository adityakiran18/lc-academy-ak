



jd_text = """
Senior Associate, Data Scientist - AI Software Engineering
Data is at the center of everything we do. As a startup, we disrupted the credit card industry by individually personalizing every credit card offer using statistical modeling and the relational database, cutting edge technology in 1988! Fast-forward a few years, and this little innovation and our passion for data has skyrocketed us to a Fortune 200 company and a leader in the world of data-driven decision-making.

As a Data Scientist at Capital One, you’ll be part of a team that’s leading the next wave of disruption at a whole new scale, using the latest in computing and machine learning technologies and operating across billions of customer records to unlock the big opportunities that help everyday people save money, time and agony in their financial lives.

Team Description

The AI Foundations – AI Software Engineering Data Science team designs, builds, and delivers state-of-the-art, scalable AI architectures that transform how software is developed at Capital One. We partner closely with product and engineering teams to create multi-agent solutions across the software development lifecycle—including code generation, migration, troubleshooting, root-cause analysis, and documentation—leveraging technologies such as LangGraph, MCP, agent-to-agent protocols, and advanced model customization techniques.

Role Description

In this role, you will:

Partner with a cross-functional team of data scientists, software engineers, and product managers to deliver a product customers love

Leverage a broad stack of technologies — Python, Conda, AWS, H2O, Spark, and more — to reveal the insights hidden within huge volumes of numeric and textual data

Build machine learning models through all phases of development, from design through training, evaluation, validation, and implementation

Flex your interpersonal skills to translate the complexity of your work into tangible business goals

The Ideal Candidate is:

Innovative. You continually research and evaluate emerging technologies. You stay current on published state-of-the-art methods, technologies, and applications and seek out opportunities to apply them.

Creative. You thrive on bringing definition to big, undefined problems. You love asking questions and pushing hard to find answers. You’re not afraid to share a new idea.

Technical. You’re comfortable with open-source languages and are passionate about developing further. You have hands-on experience developing data science solutions using open-source tools and cloud computing platforms.

Statistically-minded. You’ve built models, validated them, and backtested them. You know how to interpret a confusion matrix or a ROC curve. You have experience with clustering, classification, sentiment analysis, time series, and deep learning.

A data guru. “Big data” doesn’t faze you. You have the skills to retrieve, combine, and analyze data from a variety of sources and structures. You know understanding the data is often the key to great data science.

Basic Qualifications:

Currently has, or is in the process of obtaining one of the following with an expectation that the required degree will be obtained on or before the scheduled start date:

A Bachelor's Degree in a quantitative field (Statistics, Economics, Operations Research, Analytics, Mathematics, Computer Science, or a related quantitative field) plus 2 years of experience performing data analytics

A Master's Degree in a quantitative field (Statistics, Economics, Operations Research, Analytics, Mathematics, Computer Science, or a related quantitative field) or an MBA with a quantitative concentration

Preferred Qualifications: 

Master’s Degree in “STEM” field (Science, Technology, Engineering, or Mathematics), or PhD in “STEM” field (Science, Technology, Engineering, or Mathematics)

Experience working with AWS

Experience building production-grade agentic platforms, including RAG and graph-augmented systems, MCP or tool-calling integrations

Demonstrated expertise in advanced model customization techniques—such as fine-tuning, parameter-efficient tuning (LoRA/QLoRA), reinforcement learning, or preference optimization

Prior research and publications in AI/ML conferences 

Capital One will consider sponsoring a new qualified applicant for employment authorization for this position.

The minimum and maximum full-time annual salaries for this role are listed below, by location. Please note that this salary information is solely for candidates hired to perform work within one of these locations, and refers to the amount Capital One is willing to pay at the time of this posting. Salaries for part-time roles will be prorated based upon the agreed upon number of hours to be regularly worked.

McLean, VA: $135,600 - $154,800 for Sr Assoc, Data Science
New York, NY: $148,000 - $168,900 for Sr Assoc, Data Science
San Jose, CA: $148,000 - $168,900 for Sr Assoc, Data Science
  """


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