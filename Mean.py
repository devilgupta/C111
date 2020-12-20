import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()

#fig=ff.create_distplot([data],["Math Scores"],show_hist=False)
#fig.show()

mean=statistics.mean(data)
std=statistics.stdev(data)
print("The mean of the data is:", mean)
print("the standard deviation of the data is:", std)

def random_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    setofmeans=random_mean(100)
    mean_list.append(setofmeans)

mean=statistics.mean(mean_list)
std=statistics.stdev(mean_list)
print("The mean of the sampling distribution is:", mean)
print("the standard deviation of the sampling distribution is:", std)

#fig=ff.create_distplot([mean_list],["Student marks"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="MEAN"))
#fig.show()

df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()
meanofsample1=statistics.mean(data)
print("Mean of sample one is:",meanofsample1)
first_sd_start,first_sd_end=mean-std,mean+std
print("Standard deviation 1",first_sd_start,first_sd_end)
fig=ff.create_distplot([mean_list],["Student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 END"))
fig.show()

df=pd.read_csv("data2.csv")
data=df["Math_score"].tolist()
meanofsample2=statistics.mean(data)
print("Mean of sample two is:",meanofsample2)
second_sd_start,second_sd_end=mean-std,mean+std
print("Standard deviation 2",second_sd_start,second_sd_end)
fig=ff.create_distplot([mean_list],["Student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 END"))
fig.show()

df=pd.read_csv("data3.csv")
data=df["Math_score"].tolist()
meanofsample3=statistics.mean(data)
print("Mean of sample three is:",meanofsample3)
third_sd_start,third_sd_end=mean-std,mean+std
print("Standard deviation 3",third_sd_start,third_sd_end)
fig=ff.create_distplot([mean_list],["Student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 3 END"))
fig.show()

z_score=(meanofsample1-mean)/std
print("the z score of sample 1 is:",z_score)

z_score=(meanofsample2-mean)/std
print("the z score of sample 2 is:",z_score)

z_score=(meanofsample3-mean)/std
print("the z score of sample 3 is:",z_score)