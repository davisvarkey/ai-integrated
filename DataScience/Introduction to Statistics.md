# Introduction to Statistics

We all have used statistics in our day-to-day life. For example, when someone asks how much data you consume in your phone per day, your response could be “around 1.2GB per day” or “about 1-1.5GB per day”. How did you come up with this number? It’s unlikely that you are consuming 1.2 GB of data every day; rather, your usage could be along the following lines:

Day 1: 1.3 Gigabytes
Day 2: 1.1 Gigabytes
Day 3: 0.9 Gigabytes
Day 4: 2.5 Gigabytes
Day 5: 1.2 Gigabytes
Day 6: 1.0 Gigabytes    
Day 7: 1.3 Gigabytes
Day 8: 0.2 Gigabytes
Day 9: 1.1 Gigabytes
Day 10: 1.4 Gigabytes


We look at these numbers and observe that they are close to 1.2 GB; further, the usage lies between 1GB and 1.5GB almost every day. Your brain calculates the average (approx.) of all the numbers. You also saw that on day 4, the consumption is unusually high (2.5 GB), but since it happened only on one day, you leave it out (Outlier is the statistical term for it) 
So why is statistics important? It helps us make sense of the data. We can’t tell anyone how much data we consume each day, but we can give an estimate using statistics.  

Other examples:

How much does an audible book cost? - $5 
How many hours does a Data Scientist Work? - 9 hours a day 
Journey time between Los Angeles to San Diego by road - Around 6 hours

All these are estimates but not actual numbers. These estimates help us make better decisions. For example, if you know that the average journey time between Los Angeles to San Diego by road is 6 hours, you’ll most likely pack your stuff accordingly or mark good restaurants on the route for a break.

Statistical methods can be broadly classified into two parts - Descriptive Statistics and Inferential Statistics.


## Descriptive Statistics and Inferential Statistics

Descriptive statistics is the process of summarizing the information of a Dataset. Typically, a dataset is described using measures of central tendency such as its mean, median, and mode and measures of dispersion such as variance. You could also describe a dataset using charts like bar charts or boxplots, etc. Note that descriptive statistics do not include methods to infer anything about similar data. 


Inferential Statistics is the study of methods to make inferences from the sample collected. For, e.g., if you want to know specific characteristics about 25-year-olds living in the United States, like their height, marital status, salary, etc., It’s almost impossible to get these details of every 25-year-old in the United States. So, one way to go about it is to collect these details for a randomly selected group of 5000 or 10000 people of this age (perhaps through an online survey) and extrapolate the results for the United States.


Population vs. Sample:
Most of the time, it’s not possible to have all the data. For instance, as we discussed above, it’s not possible to collect the data of every 25-year-old person to get the average 25-year-old’s height. In this case, the population is every 25-year-old person in the USA, while our sample consisted of a randomly selected part of the population. 




Different colors in the population denote other characteristics of the population like gender, states, etc. 

Central Tendency

Let’s consider a dataset of employees working at Company X:



You can summarize this data using a frequency table.




You can summarise the data using measures of central tendency as well:



Mean: It’s the average of the data. For eg. Mean of the salary of the employees is 
($285 + $250 + $300 + $300 + $320 + $150 + $175 + $250 + $450)/9
= $242 

Similarly, the average age of the employees is: 30.66

Mode: The mode of a quantity or feature is its most frequently occurring value in the dataset. For example, the Mode of age of the employees is 28 (3 employees have the age 28 in the dataset)

Median: Median is the center value of the data when you sort the data into increasing/decreasing order. For example, to get the median salary, sort the salary in ascending order: $150, $175, $250, $250, $285, $300, $300, $320, $450
So the median is $285.

Also, the median value of the employee’s age is 28 
Note: If the data contains an even number of data points, there will be two values in the center. The average of the two center values will be called the median. 

Mean vs. Median:

Mean can get affected by Outliers, but Median can’t.
Example. A news channel invited a group of 8 individuals for a round table discussion on financial freedom. Their names and salaries (per month) are as follows: Amelia: $8000, Bill: $150000, Collin: $3000, Deren: $6500, Emma: $9000, Fred: $2000, Greg: $9500, Henry: $5500 


The average salary of the group is $193500/8 = $25187, approximately
However, notice that there is only one person with a salary higher than $25187. In other words, the mean salary of the group has been highly affected by the salary of Bill, and hence, it does not give a good insight into the group’s salary. 

On the other hand, the group’s median salary: ($6500 + $8000)/2 = $7250. 
Notice that the Median of the group’s salary is not affected by the salary of the Bill, and it gives a better picture of the group’s salary. Even if you multiply ill’s salary by 10, the median value will be the same, whereas your mean will change drastically.

In the previous scenario, suppose one more person joins the group in the middle of the conversation, and that person’s salary is unknown. In this case, the person’s salary will likely be close to the median than the mean. We’ll discuss this further when dealing with large datasets and studying missing value imputations.

  So, In general, for skewed data sets, the median is a better approximation than the mean for missing data points.

Do it Yourself: Create a random array of size 1000 consisting of integers from 100 to 200 in Python and calculate the mean, mode, and median of the data using NumPy.
Now let’s look at the dataset of the age of employees of company Y



If you see, the mean, median, and mode for the age of employees are the same for company X and company Y. The mean age of the employees of both companies is 30.66, Median is 28, and Mode is 28 (Note: It’s just a coincidence that median and mode both are 28).

However, we can see a difference between the employees of company X and company Y. The mean, median, and mode do not give us an idea about the variability of the data. Hence, we define another set of measures to understand its variability or spread.

Measures of Variability

Range: The difference between the highest and lowest values. 
Range of Company Y’s employee ages = (41-21) = 20 
Range of company X’s employee ages = (38-25 )= 13 

Variance: 
Sample variance = S2 = ∑(xi - x​​mean)²∕(N-1) 
N is the sample size of the data.

xmean is the mean of the sample. 

NOTE: For sample variance, the denominator term is n-1, whereas if you calculate the population variance, use n instead of n-1. The reason for dividing sample variance with n-1 instead of n is to make the sample variance an unbiased estimator of the population variance. Don’t worry if you are not familiar with the unbiased estimator; we’ll cover it later.

Standard deviation: The standard deviation of a sample is defined as the square root of its variance. 


