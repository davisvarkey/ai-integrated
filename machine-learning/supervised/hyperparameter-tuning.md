# Tuning hyperparameters
Steps for tuning hyperparameters:
1. Define a hyperparameter search space.
2. Configure hyperparameter sampling.
3. Select an early-termination policy.
4. Run a sweep job.

## Define a hyperparameter search space
The set of hyperparameter values tried during hyperparameter tuning is known as the search space. The definition of the range of possible values that can be chosen depends on the type of hyperparameter.

### Discrete hyperparameters
Some hyperparameters require discrete values - in other words, you must select the value from a particular finite set of possibilities. You can define a search space for a discrete parameter using a Choice from a list of explicit values, which you can define as a Python list (Choice(values=[10,20,30])), a range (Choice(values=range(1,10))), or an arbitrary set of comma-separated values (Choice(values=(30,50,100)))

You can also select discrete values from any of the following discrete distributions:

QUniform(min_value, max_value, q): Returns a value like round(Uniform(min_value, max_value) / q) * q
QLogUniform(min_value, max_value, q): Returns a value like round(exp(Uniform(min_value, max_value)) / q) * q
QNormal(mu, sigma, q): Returns a value like round(Normal(mu, sigma) / q) * q
QLogNormal(mu, sigma, q): Returns a value like round(exp(Normal(mu, sigma)) / q) * q
