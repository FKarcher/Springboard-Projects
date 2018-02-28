import pandas as pd

df = pd.read_csv('data/human_body_temperature.csv')

# Importing necessary modules
import matplotlib.pyplot as plt
import numpy as np

#Generating arrays for the ECDF (graphing original data)
ecdf_x=np.sort(df["temperature"])
ecdf_y=np.arange(1, len(ecdf_x)+1)/len(ecdf_x)

#Plotting the ECDF with an appropriate label and labelling the axes.
plt.plot(ecdf_x, ecdf_y, marker=".", linestyle="none", color="blue", label="Empirical CDF")
plt.xlabel("Temperature")
plt.ylabel("ECDF")

#Generating a sorted array of normally distributed values and the accompanying y axis values.
normal_samples=np.sort(np.random.normal(np.mean(df["temperature"]),np.std(df["temperature"]) , size=10000))
cdf_y=np.arange(1, len(normal_samples)+1)/len(normal_samples)

#Plotting the Theoretical CDF of the normally distributed data on top of the ECDF.
plt.plot(normal_samples, cdf_y, color="red", label="Theoretical CDF")
plt.legend(loc="upper left")

#Showing the Empirical and Theoretical CDFs on one graph.
plt.show()


#Actual sample mean
sample_mean=np.mean(df["temperature"])
proposed_mean=98.6
#Observed t value (difference in proposed population mean and actual sample mean)
actual_t_value=proposed_mean - sample_mean

#Assuming null hypothesis is true, sample mean should be 98.6, so we adjust the values.
df["temperature adjusted"]=df["temperature"] + proposed_mean - sample_mean

#Generating array to hold t values generated from bootstrap samples (bootstrap replicates)
t_values=np.empty(10000)

#Looping 10,000 times
for i in range(10000):
   # to generate bootstrap replicates and store them in the array
   simulated_mean=np.mean(np.random.choice(df["temperature adjusted"], len(df["temperature adjusted"])))
   t_values[i]=proposed_mean - simulated_mean

#Calculating the p value   
p_value=np.sum(t_values>actual_t_value)/len(t_values)

print("Actual t value: %f, p value: %f" % (actual_t_value, p_value))
plt.hist(t_values, bins=20, normed=True, label="Simulated t values")
plt.xlabel("t value")
plt.ylabel("Probability")
plt.axvline(x=actual_t_value, color="red", label="Actual t value")
plt.legend(loc="upper left")
plt.show()
