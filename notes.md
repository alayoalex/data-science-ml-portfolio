# Study Notes

## Notes from [Book: Python Machine Learning by Sebastina Raschka]

#### Unsupervised Learning
- Clustering
- Dimensionality reduction

#### Supervised Learning
- Classification (discrete classes)
- Regression (Continuos values)

#### Reinforcement Learning
- System (agent) that improve its performance based on interactions with environment. For example a `Chess Engine` where the environment is the state of the board and the reward is win.

#### Workflow in predictive modeling
1. Preprocessing: Getting data into shape
    - Feature Extraction and Scaling
    - Feature Selection
    - Dimentionality Reduction
    - Sampling
    - Training Set and Test Set (and Validation Set)
2. Learning: Algorithm
    - Model Selection
    - Cross Validation
    - Performance Metrics
    - Hyperparamenter Optimization
3. Evaluation: Final Model
4. Prediction

* One-vs-All(OvA) technique or One-vs-Rest(OvR) is used to multi-class classification.

* Convergence is one of the biggest problems of perceptron . It only converges if the two classes can pe separeted by a linear hyperplane.
#

## Notes from [Course: Introduction to Data Science]

*Data Science*: Scientific method to study data. Storage, Debugging or Cleaning, Analysis.

`Big data`: Hadoop (clusters)
- Storage a great amount of data
- Process data
    1. Map Reduce (batch)
    2. Apache Spark (real time)
- Clean data (R, Python)

* Have data --> Make questions to data (interesting questions)

Relational Databases
SQL, Schemas, RDBMS
Datawarehouse (EDW)
ETL {Extract, Transform, Load}

EDWs are expensive, Hadoop replaces it.

Most companies don't have a Big Data problem

Big Data four Vs:
- Volumen
- Variety
- Velocity
- Veracity

#### A Data Scientist is a person who build systems to find pattern in data.
- Build a model
- Deliver results to an user

#### Typical year of a Data Scientist

1. Develop relationships with other people in the enterprice.
2. Evangelize a data culture inside the company.
3. Build tools for internal usage.
4. Build systems and features for external users.
5. Build and maintain ETL engineer systems.

#### Tools:
- Math: Statitics. Machine learning. Optimization. Linear Algebra.
- Engineer: Python, R, Scala, Cloud.

## Typical Workflow
1. Ask a question
2. Gather data
3. Clean data
4. Sleep with data (inspect, visualize, explore)
5. Build a model
6. Validate the model
7. Publish results
8. Automatize. Make that machines do everything

#

## Notes from [Article: Practical advice for analysis of large, complex data sets](https://www.unofficialgoogledatascience.com/2016/10/practical-advice-for-analysis-of-large.html)

#### Data Science daily work

1. Make sense of confusing results
2. Measure new phenomena from logged behavior
3. Validate analysis done by others
4. Interpretate metrics of user behavior

#### Data Analysts must be:

- Carefull
- Methodical

#### The advice is organized into three general areas:

* `Technical`: Ideas and techniques for how to manipulate and examine your data.
* `Process`: Recommendations on how you approach your data, what questions to ask, and what things to check.
* `Social`: How to work with others and communicate about your data and insights.

#### `Technical`

- Look at your distributions
- Consider the outliers
- Report noise/confidence
- Look at examples
- Slice your data
- Consider practical significance
- Check for consistency over time

#### `Process`

- Separate Validation, Description, and Evaluation

I think about about exploratory data analysis as having 3 interrelated stages:

1. `Validation or Initial Data Analysis`: Do I believe data is self-consistent, that the data was collected correctly, and that data represents what I think it does? This often goes under the name of “sanity checking”. For example, if manual testing of a feature was done, can I look at the logs of that manual testing? For a feature launched on mobile devices, do my logs claim the feature exists on desktops?

2. `Description`: What’s the objective interpretation of this data? For example, “Users do fewer queries with 7 words in them?”, “The time page load to click (given there was a click) is larger by 1%”, and “A smaller percentage of users go to the next page of results.”

3. `Evaluation`: Given the description, does the data tell us that something good is happening for the user, for Google, for the world? For example, “Users find results faster” or “The quality of the clicks is higher.”

- Confirm expt/data collection setup
- Check vital signs
- Standard first, custom second
- Measure twice, or more
- Check for reproducibility
- Check for consistency with past measurements
- Make hypotheses and look for evidence
- Exploratory analysis benefits from end to end iteration

#### `Social`

- Data analysis starts with questions, not data or a technique
- Acknowledge and count your filtering
- Ratios should have clear numerator and denominators
- Educate your consumers
- Be both skeptic and champion
- Share with peers first, external consumers second
- Expect and accept ignorance and mistakes

## Closing thoughts

No short list of advice can be complete even when we break through the barrier of the Top 10 List format (for those of you who weren’t counting, there are 24 here). As you apply these ideas to real problems, you’ll find the habits and techniques that are most important in your domain, the tools that help you do those analyses quickly and correctly, and the advice you wish were on this list. Make sure you share what you’ve learned so we can all be better data scientists.

# 

## Notes from [Article: Key Metrics for Data Science Team Success](https://towardsdatascience.com/key-metrics-for-data-science-team-success-822da77f509c)

How data science team leaders can measure team performance and demonstrate success for the C-suite.

A recent survey from Wakefield Research found that 71% of data executives say their company leadership expects revenue growth from their investment in data science. Senior leaders don’t just want incremental growth from these programs — 25% of data science leaders say their company leadership expects double-digit growth from data science, adding pressure to deliver quickly.

But a good data science program can take months or years to get a flywheel of innovation cranking away — so how do you show consistent results each quarter to demonstrate you’re not only discovering useful insights today, you’re also building an analytics machine that will add value for many years?

#### `Demonstrate velocity`

Make your process repeatable and trackable in important to building a high-velocity data team. Leaders need to take a systematic approach to managing data science.

#### `Deliver ROI`

Many executive stops data sciecne program if maodel fail or cut back investment if adata model fails.

#### `Grow your team`

Recruitment and retention will be ongoin issues, and if you want to build a fundation for significant result, yu need a strong, consistent team.

## Closing Words

If you build a program that continues to accelerate with repeatable processes and reusable assets, keeps the C-suite informed and understanding of the big picture, and helps your team feel integrated and effective, then you can build a team that will make a major impact and deliver significant, measurable, results.

#

## Notes from [Article: The First Rule of Machine Learning: Start without Machine Learning](https://eugeneyan.com/writing/first-rule-of-ml/)

Applying machine learning effectively is tricky. 

- You need data. 
- You need a robust pipeline to support your data flows. 
- And most of all, you need high-quality labels. 

As a result, most of the time, my first iteration doesn’t involve machine learning at all.

Rule #1: [Don’t be afraid to launch a product without machine learning](https://developers.google.com/machine-learning/guides/rules-of-ml)

`Machine learning is cool, but it requires data. Theoretically, you can take data from a different problem and then tweak the model for a new product, but this will likely underperform basic heuristics. If you think that machine learning will give you a 100% boost, then a heuristic will get you 50% of the way there.`

I’d first try really hard to see if I could solve it without machine learning :D. I’m all about trying the less glamorous, easy stuff first before moving on to any more complicated solutions. — [Vicki Boykis, ML Engineer @ Tumblr](https://applyingml.com/mentors/vicki-boykis/#imagine-youre-given-a-new-unfamiliar-problem-to-solve-with-machine-learning-how-would-you-approach-it)

#### What should we start with then?

Regardless of whether you’re using simple rules or deep learning, it helps to have a decent understanding of the data. Thus, grab a sample of the data to run some statistics and visualize! (Note: This mainly applies to tabular data. Other data such as images, text, audio, etc. can be tricker to run aggregate statistics on.)

- Simple correlations help with figuring out the relationships between each feature and the target variable.
- Scatter plots are a favorite for visualizing numerical values.
- If either variable is categorical, I’ve found box plots to work well.

With an understanding of the data, we can then start by solving the problem with heuristics. Here are some examples of using heuristics to solve common problems (you’ll be surprised how difficult they are to beat):

1. `Recommendations`: Recommend top-performing items from the previous period; can also be segmented by categories (e.g., genres, brands). If you have customer behavior, you can compute aggregated statistics on co-interactions to calculate item similarity for i2i recommendations (see Alibaba’s Swing Algorithm here).

2. `Product classification`: Regex-based rules on product titles. Here’s an example from Walmart’s product classifier (Section 4.5): If product title contains “ring”, “wedding band”, “diamond. *bridal”, etc., classify it in the ring category.

3. `Review spam identification`: Rules based on the count of reviews from the same IP, time the review was made (e.g., odd timing like 3 am), similarity (e.g., edit distance) between the current review and other reviews made on the same day.

#### When should we use machine learning then?

After you have a non-ML baseline that performs reasonably well, and the effort of maintaining and improving that baseline outweighs the effort of building and deploying an ML-based system.

Rule #3: Choose machine learning over a complex heuristic.

`A simple heuristic can get your product out the door. A complex heuristic is unmaintainable. Once you have data and a basic idea of what you are trying to accomplish, move on to machine learning… and you will find that the machine­-learned model is easier to update and maintain.`

Having robust data pipelines and high-quality data labels also suggests you’re ready for machine learning. 

#### But what if I need to use ML, just for the sake of it?

Hmm, that’s a tough position to be in. How do you balance solving the problem and serving customers, vs. wasting a ton of time and effort just for the sake of it? I don’t have an answer to that, but I’ll leave you with this genius tip from Brandon Rohrer.

#

## Notes from [Article: The Data Science Interview Process at Shopee Singapore](https://towardsdatascience.com/the-lessons-i-learned-from-failing-the-job-interviews-at-shopee-singapore-dd24b9f2bf3d)

For example, while explaining my image captioning project, he asked me how I evaluate the accuracy of my model. In my reply, I told him I used BLEU for evaluation. Then he went on to ask why I didn’t use Meteor or CiDER for the evaluation as well.

Some people may find it difficult to understand why a data scientist needs to learn how to deploy the app. I believe that most companies would expect you to manage the entire data science product pipeline yourself unless you were working in a dedicated team where you’d be given a specific pipeline to focus on. Additionally, knowing how everything works helps us identify any problems along the pipeline quickly. Hence, you should be familiar with the whole data science pipeline if you want to stay competitive.

How I collected and used the data
What I did to preprocess the data
Which models I have experimented with and why I chose the models for the final production
How I selected the metrics and why
What I did to deploy the model
How did I do error analysis and how did I improve the models
What was the end-user feedback like
What I did to design my MLOps


#