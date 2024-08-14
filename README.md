# Patterns-of-Life Simulation

This is a clone of the Patterns-of-Life simulation project. The original project is located at the master branch of [https://github.com/gmuggs/pol](https://github.com/gmuggs/pol). I develope new features and customize the simulation based on my research needs here.

# Download Dataset: [OSF](https://osf.io/dg6t3/)
## Dataset Instructions
- There are four folders, corresponding to three different types of selection outliers: 1) centralized (think: random), 2) infectious (anomalous agents infect other agents to become anomalous using an infectious disease model with a few randomly selected seed agents), and 3) location (an infected location makes agents anomalous. Think of the John Snow's Infected Well in the 1850s London Cholera Outbreak)
  - You can pick any/all of these. Say you pick centralized.
- Inside the Centralized folder, you find many subfolders. Each is a dataset. The folder describes the dataset parameters.
  - The prefix "Atlanta"/"Berlin" means that the Atlanta, GA or Berlin, Germany region was simulated.
  - The String "hunger" / "interest" / "social" / "work" / "combined" outlier describe different types of anomalies:
    - hunger outliers have a vastly increased appetite while anomalous. They will need to go home or to restaurants to eat much more frequently.
     - interest outliers can be ignored. Those didn't work well and will be removed from the paper.
    -  social outliers: While anomalous, these agents change their logic of choosing recreational sites: Instead of the normal logic to choose recreational sites to meet friends, these agents will go to random places. These are social outliers because they don't meet their usual friends, but instead, meet random folks.
    -  work outliers: These agents stop going to work while anomalous.
combined: Has all of the above.
  - You can pick any/all of these. Let's say that you go to the "atlanta_work_outliers" folder.
- Inside each folder, you can find data for a unique simulation. Each simulation has 1000 agents for 4 weeks of train and a variable number of test (depending on the type of anomalies - 2 weeks for centralized/random, longer for the infectious disease as it takes time to spread)
  - You can find train and test data for the following data types: 1) trajectories, 2) staypoints, 3) social links.
   - For example,
     - the zip-file trajectories_train will contain the trajectory data for the 4 weeks train period.
     - the zip-file trajectories_test will contain the trajectory data for the 2 weeks (since we're in the centralized folder) test data.
- The ground truth of anomalies can be found in the same folder in the file "labels.json"
   - For each type of anomalies, we have three levels: "Red", "Orange", and "Yellow" which describes the severity of the outlierness. Details in the paper. For example, Red-Appetite agents will eat like crazy and should be easy to detect. Yellow agents only have a somewhat increased appetite and may change behavior less severely and may be more difficult to detect. Orange is between yellow and red.
  - The labels.json file tells us which agent is which type of outlier using a two digit integer: The first digit is the type of outlier (hunger/social/work), the second digit is the degree/color of outlier (red/orange/yellow). For example, the line "  "223": "31"," in the json file means that Agent 223 is a Type 3 anomalies (work type) with a severity of 1 (Yellow).
    - The first digit is necessary, as the "combined" outlier datasets have all types of anomalies, and thus, may have a "13" (Hunger-Type, Red Severity) and "31" (Work Anomaly, Red Severity)


# Quick Start


## How to compile and build a jar file
For the first time to install the dependencies, run the following command:
```
bash sh.mvn.sh full
```
Later, you can run the following command to build a jar file:
```
bash sh.mvn.sh
```

## How to run a simulation

```
cd life
bash sh.live.sh
```
